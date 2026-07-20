# Maintenance workflow

## Authoritative files

- `dag/proof-dag.json` owns node IDs, dependency edges, and statuses.
- `proof/parts/*.tex` owns the mathematical text of each assembled module.
- `proof/conditional-proof.tex` owns assembly order and the conditional main
  theorem statement.
- `docs/proof-audit.md` records the current build and integrity audit.
- `docs/wrong-routes.md` records why discarded routes must not be reintroduced.

README prose and the PDF are projections of these sources; they are not status
authorities.

## Naming

Proof modules use `NN-nodeid-description.tex`:

- `NN` is the two-digit topological reading order;
- `nodeid` is the stable DAG/label namespace, in lowercase in filenames;
- `description` is a short kebab-case mathematical role.

Do not renumber a module unless the assembly order changes. Do not rename a DAG
node merely for prose style: IDs are stable interfaces used by labels and audit
records.

## Updating a proof node

1. Edit one file under `proof/parts/` and keep its public statement and imported
   dependency interfaces explicit.
2. If an edge or status changes, update `dag/proof-dag.json` in the same commit.
3. Update `docs/wrong-routes.md` only when a route is rigorously retracted,
   disproved, or replaced; do not paste exploratory logs into it.
4. Run `python scripts/check_repo.py`.
5. Compile from `proof/`:

   ```powershell
   latexmk -pdf -no-shell-escape -recorder -file-line-error `
     -interaction=nonstopmode -halt-on-error conditional-proof.tex
   ```

6. Confirm that the log has no undefined references/citations, duplicate
   labels, fatal errors, or pending rerun warning.
7. Recompute SHA-256 for `conditional-proof.tex`, `conditional-proof.pdf`, and
   `conditional-proof.fls`, then update `docs/proof-audit.md`.

## Status boundary

The repository currently proves a conditional theorem. `JC-PL` is open and
`JP-JC`, `NR`, `J0`, `G0`, and `MAIN` remain dependent. Do not use
“unconditional proof”, close a dependent node, or remove the assumption from
the first theorem until `JC-PL` and its `JC-SP`/`JC-CL` subcontracts have been
proved and independently re-audited.

Numerical searches may guide future work but may not discharge a proof node.
Only exact arguments or explicitly documented rigorous certificates may change
a node from open/dependent to closed.
