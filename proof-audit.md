# Proof Audit Report

## Completed

- Formalized theorem: conditional on the pathwise LCA payment `JC-PL`, stated
  explicitly in the first theorem of `proof/conditional-proof.tex`.
- Blueprint/global audit: revision 24 retains 29 conceptual nodes and 19
  assembly modules; 21 nodes are closed, 2 retained, 1 open, and 5 dependent.
- Local proof audits: the frozen revision-24 assembly records a positive audit
  for conditional-frontier consistency only; it records no unconditional-main-
  theorem pass.
- Constant closure: all constants used by the stated conditional implication
  are inherited from the frozen revision-24 assembly; `JC-PL` is assumed, not
  silently discharged.
- Experiments and counterexample checks: numerical explorations are not used as
  proof premises. Exact counterexamples and retractions affecting route choice
  are summarized in `wrong-routes.md`.
- LaTeX compilation: compiled with `latexmk`.
- LaTeX source SHA256: `997f88176635bfc46a834d1385f01d2ddeb074b4fafd638fde0bfbde8e472d65`
- Compiled PDF SHA256: `0b2576c8251e4fcf2edf2adb565b8d5f7b2fa084fae1d0fc8ee36ac2df86212b`
- LaTeX recorder SHA256: `0422a7a61d193c043c13462876219b7877c535e8aa339fd1f988561dece87e3b`
- Build result: 178 pages; no undefined references, undefined citations,
  multiply defined labels, LaTeX/package errors, fatal errors, or pending rerun
  warnings. Eighteen nonfatal overfull-box warnings remain.

## Blocked/Gaps

- None for the stated conditional theorem. The unconditional theorem is not
  claimed: `JC-PL` remains unproved, with open subcontracts `JC-SP` and `JC-CL`.

## Citation Checks

- `BL76`: H. J. Brascamp and E. H. Lieb, *Journal of Functional Analysis* 22
  (1976), 366--389; cited for log-concavity of the first Dirichlet ground state
  on a bounded convex domain. The bibliographic record and application are
  inherited from revision 24; this packaging pass added the missing explicit
  `\cite{BL76}` but did not perform a new literature audit.

## Certificate Checks

- No external executable certificate is a premise of the published conditional
  implication. Exact rational inequalities retained by the assembly are printed
  in the LaTeX source; exploratory numerical scripts and reports were excluded
  from this clean repository.

## Proof Chain

Closed foundations imply `JP-EH + JP-NS + JP-DE`, then the closed
`JC-ALG + JC-TL + JC-AR` block; assuming `JC-PL` yields
`JP-JC → NR → J0 → G0 → MAIN`.
