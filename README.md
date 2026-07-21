# Large-N polygonal Pólya–Szegő proof DAG

> **Status:** `math-proof` Stage 5 (Local Proof). The active target is
> `JC_CL_RL`. The repository does **not** claim that the main theorem is proved.

The canonical proof workspace is
`math-proof-output/large-n-polya-szego/`. Its state is owned by
`proof-blueprint.md`; this README is only a navigation aid.

## Repository layout

```text
.
├── README.md
├── MAINTENANCE.md
├── math-proof-output/
│   └── large-n-polya-szego/
│       ├── proof-blueprint.md          # theorem freeze, route screen, DAG, status
│       ├── definitions-and-notation.md # shared notation and failure checklist
│       ├── literature-review.md        # authoritative citation records
│       ├── parts/                      # one canonical Markdown file per DAG node
│       ├── experiments/                # reproducible checks; heuristic unless promoted
│       └── scratch/
│           ├── attack-ledger.json      # machine-readable failed-attack ledger
│           ├── route-history.md        # compact rejected-route summary
│           ├── route-scouting.md       # route-selection evidence
│           └── crux-dossiers/          # retained route probes and kill certificates
├── legacy/
│   └── revision-24/                    # noncanonical conditional assembly evidence
│       ├── conditional-assembly/
│       ├── conditional-frontier-audit.md
│       └── proof-dag.json
└── scripts/
    └── check_legacy_conditional_assembly.py
```

The active workspace contains only current proof state, proof-node Markdown,
reproducible checks, and the compact route-failure record required by the
workflow. Revision-24 LaTeX is isolated under `legacy/`: it records the old
conditional implication from `JC_PL` to the theorem, but owns no current status
and is not an unconditional proof.

## Current proof chain

```text
super-near:
JC_SP_MATFLUX + JC_SP_COORD -> JC_SP_SRC -> JC_SP_EST

coarse:
JC_CL_RL -> JC_CL_CIRC_RES -> JC_CL_PROF -> JC_CL_RES

assembly:
JC_SP_EST + JC_CL_RES -> JC_PL -> T
```

Already audited locally: `JC_SP_MATFLUX`, `JC_SP_COORD`.

Current bottleneck: `JC_CL_RL`, the real-line monotone-displacement coercivity
estimate. All statuses and dependency edges must be read from the blueprint.

## Validation

From the repository root:

```powershell
$skillRoot = 'C:\Users\cheng\.codex\skills\math-proof'
$workspace = 'math-proof-output\large-n-polya-szego'
python "$skillRoot\scripts\workspace_doctor.py" check $workspace
python "$skillRoot\scripts\check_blueprint.py" --stage auto `
  "$workspace\proof-blueprint.md"
python scripts\check_legacy_conditional_assembly.py
```

These commands validate structure and evidence consistency, not mathematical
truth. Read `MAINTENANCE.md` before changing a statement, route, edge, status,
or audit receipt.
