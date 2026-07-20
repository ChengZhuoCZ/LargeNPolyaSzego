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
- LaTeX entry-point SHA256: `ee689b0fc43cb650f29efd5fc939efed4623473441f66e5079a490aa8756f21c`
- Proof source tree SHA256: `a161ad8535ee421ad581046f170f513447aa2f10d6b431543868e55f20d47e6e`
- Compiled PDF SHA256: `928ef6b3044cf83202c6d140ed91cd4975b824f02aba7b70e3640d3a569af7fe`
- LaTeX recorder SHA256: `7ee4b7d64c6e53e86e02b47983d552df2a30db8c11b3c897289835b8366f3788`
- Build result: modular 19-part source, 178 pages; no undefined references, undefined citations,
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
