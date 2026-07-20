# Large-\(N\) Pólya--Szegő proof DAG

> **Status:** conditional proof / active frontier. This repository does **not**
> claim an unconditional proof of the convex large-\(N\) polygonal
> Pólya--Szegő theorem.

This is the cleaned revision-24 proof package. Historical stage snapshots,
duplicate builds, numerical scratch files, and superseded proof drafts have
been omitted.

## Current theorem

The assembled theorem is conditional on the pathwise LCA payment `JC-PL`:

> Assume `JC-PL`. Then, for all sufficiently large \(N\), the regular
> \(N\)-gon uniquely minimizes the first Dirichlet eigenvalue among convex
> \(N\)-gons of fixed area, up to congruence.

The exact dependency frontier is:

```mermaid
flowchart TD
  F["Closed foundations"] --> E["JP-EH + JP-NS + JP-DE"]
  E --> A["JC-ALG + JC-TL + JC-AR (closed)"]
  A --> PL["JC-PL (open)"]
  PL --> C["JP-JC"]
  C --> N["NR → J0 → G0 → MAIN"]
```

`JC-PL` contains two still-unproved subcontracts:

- `JC-SP`: uniform continuity of the completed-action Hessian in the natural
  energy on the super-near chart;
- `JC-CL`: coarse/far localization, including the regular monotone-transport
  coercivity problem and the nonregular original-path row.

## Files

- [`proof/conditional-proof.tex`](proof/conditional-proof.tex): standalone
  LaTeX source for the complete conditional assembly.
- [`proof/conditional-proof.pdf`](proof/conditional-proof.pdf): compiled proof.
- [`proof/conditional-proof.fls`](proof/conditional-proof.fls): LaTeX recorder.
- [`proof-audit.md`](proof-audit.md): concise status, citation, compilation,
  and integrity audit.
- [`dag/proof-dag.json`](dag/proof-dag.json): machine-readable conceptual DAG.
- [`wrong-routes.md`](wrong-routes.md): concise record of retracted, disproved,
  or inactive routes.

## Build

From the repository root:

```powershell
cd proof
latexmk -pdf -no-shell-escape -recorder -file-line-error \
  -interaction=nonstopmode -halt-on-error conditional-proof.tex
```

The source is self-contained and has no local `\input` dependencies.
