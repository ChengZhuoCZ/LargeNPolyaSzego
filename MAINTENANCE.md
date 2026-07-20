# Maintenance workflow

## Authoritative ownership

- `math-proof-output/large-n-polya-szego/proof-blueprint.md` owns the frozen
  theorem, current route screen, dependency edges, node risk/status/audit, and
  certificate plan.
- `definitions-and-notation.md` owns shared notation and the `PSF-*` failure
  checklist.
- Each current claim has one canonical Markdown file under `parts/`; its full
  statement and proof text live there.
- `literature-review.md` owns full citation records. The blueprint citation
  table is only its route-active projection.
- `source/conditional-assembly/` and `source/revision-24-proof-dag.json` are
  retained migration evidence. They do not own current workflow status.
- `scratch/route-history.md` records old failures. It cannot discharge a node.

## Directory and naming rules

- The proof workspace stays at `math-proof-output/large-n-polya-szego/`.
- Canonical parts use `NN-short-name.md`; workflow IDs remain stable even when
  prose labels improve.
- Do not create `proof.tex`, `proof.pdf`, `proof.fls`, or `proof-audit.md` before
  the math-proof workflow reaches the corresponding final stages.
- Exploratory calculations belong under `experiments/` or `scratch/` and must
  remain labeled heuristic unless promoted through the Certificate Plan.
- Do not add a second authoritative DAG. The JSON file under `source/` checks
  only the retained revision-24 TeX assembly.

## Updating a current node

1. Read the target part's `Local Summary` and `Local Context Packet` first.
2. Change the full claim/proof in its Markdown part. Change an edge, status, or
   route only through the matching blueprint transaction.
3. Preserve the theorem freeze. A changed theorem requires an explicit
   Statement Change Log entry and user permission.
4. Run the math-proof checker after every structural edit. Use
   `workflow_transition.py` for every transition it supports; do not hand-edit
   a persisted intermediate state.
5. If retained TeX is edited, update its JSON projection and conditional audit
   in the same change, compile it, and run the repository-level conditional
   assembly checker.
6. A node becomes proved only after the required local audit receipt(s) bind
   the current checker-generated packet. Checker success alone is not proof.

## Standard validation

```powershell
$skillRoot = 'C:\Users\cheng\.codex\skills\math-proof'
$workspace = 'math-proof-output\large-n-polya-szego'
python "$skillRoot\scripts\workspace_doctor.py" check $workspace
python "$skillRoot\scripts\check_blueprint.py" --stage auto `
  "$workspace\proof-blueprint.md"
python scripts\check_conditional_assembly.py
```

Inspect any workspace certificate script before adding `--run-certificates`.

## Current status boundary

`JC_PL` and `T` are `todo`. The revision-24 source proves only the conditional
implication from `JC_PL` through the downstream assembly. Do not remove that
assumption, mark a downstream theorem proved, or record a subagent PASS until
the current semantic packets have received the required independent audits.
