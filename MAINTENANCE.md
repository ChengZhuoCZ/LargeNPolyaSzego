# Maintenance workflow

## Authoritative ownership

- `math-proof-output/large-n-polya-szego/proof-blueprint.md` owns the frozen
  theorem, Route Screen, dependency edges, risks, statuses, audits, and
  Certificate Plan.
- `definitions-and-notation.md` owns shared notation and the `PSF-*` checklist.
- Every current or stale DAG row has one canonical Markdown file in `parts/`;
  its full local statement and proof history live there.
- `literature-review.md` owns full citation records. The blueprint Citation
  Cache is only its route-active projection.
- `scratch/route-history.md` is the human-readable rejected-route summary;
  `scratch/attack-ledger.json` is the machine-readable attack history.
- `legacy/revision-24/` is read-only migration evidence. It does not own
  current workflow status and cannot discharge a current DAG node.

## Directory and naming rules

- Keep the active workspace at `math-proof-output/large-n-polya-szego/`.
- Canonical parts use `NN-short-name.md`; workflow IDs remain stable even if a
  prose title improves.
- Do not create `proof.tex`, `proof.pdf`, `proof.fls`, or `proof-audit.md` before
  the workflow reaches Stage 7.
- Put reproducible calculations in `experiments/`; keep exploratory material,
  failed mechanisms, and route probes in `scratch/`.
- Do not add a second authoritative DAG. `legacy/revision-24/proof-dag.json`
  validates only the legacy conditional LaTeX assembly.
- Do not move failed-route mathematics back into current parts unless a formal
  route correction promotes it.

## Updating a current node

1. Read the target part's `Local Summary` and `Local Context Packet` first.
2. Edit the full claim or proof only in that part. Change edges, statuses, or
   routes only through the applicable `math-proof` transaction.
3. Preserve the theorem freeze. Any theorem change needs user permission and a
   Statement Change Log entry.
4. Use `workflow_transition.py` for every supported transition; do not hand-edit
   a persisted intermediate state.
5. Regenerate the relevant semantic packet after any mathematical edit. A node
   becomes proved only after the required independent audit receipt or exact
   certificate binds that packet.
6. If legacy LaTeX is intentionally edited, update its manifest and legacy
   audit in the same change, compile it, and run the legacy assembly checker.

## Standard validation

```powershell
$skillRoot = 'C:\Users\cheng\.codex\skills\math-proof'
$workspace = 'math-proof-output\large-n-polya-szego'
python "$skillRoot\scripts\workspace_doctor.py" check $workspace
python "$skillRoot\scripts\check_blueprint.py" --stage auto `
  "$workspace\proof-blueprint.md"
python scripts\check_legacy_conditional_assembly.py
git diff --check
```

Inspect any certificate script before adding `--run-certificates`.

### Workspace-doctor parser note

The current `workspace_doctor.py` release reports `machine-specific absolute
path` on several portable mathematical strings, including TeX maps such as
`L:\mathcal T\to H`, ratios such as `C/N` and `R/2`, and canonical subagent
identifiers beginning with `/root/`.  These are parser false positives, not
filesystem dependencies.  Until the upstream detector distinguishes those
tokens, preserve the hash-bound proof text and require all of the following on
resume: inspect the doctor's complete file list, confirm that no real host or
temporary path occurs, pass the plain blueprint checker, validate the attack
ledger hashes, pass the legacy assembly checker, and pass `git diff --check`.
Do not rewrite audited mathematics merely to suppress this diagnostic.

## Current status boundary

The current stage is Stage 5 with active target `JC_CL_RL`. The locally audited
nodes are `JC_SP_MATFLUX` and `JC_SP_COORD`; all other non-stale nodes remain
open exactly as recorded in the blueprint. The legacy revision-24 assembly is
conditional on `JC_PL` and must never be presented as an unconditional proof.
