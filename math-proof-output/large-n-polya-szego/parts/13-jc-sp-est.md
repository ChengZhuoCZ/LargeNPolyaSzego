# JC_SP_EST: Uniform QRCI Estimate

## Local Summary
- Statement: Uniform natural-energy bound for the exact completed QRCI third-jet identity
- Dependencies: JC_SP_LEDGER
- Current obstruction: no uniform source-by-source bound is known for the resummed polygonal spectral, endpoint, moving-ground-state, metric, gauge, base, and lower-row blocks.
- Proof status: todo
- Next action: wait for the exact JC_SP_LEDGER identity, then audit the residual estimate
- Local Context Packet: the statement below + the proved JC_SP_MATFLUX and JC_SP_LEDGER packages when available + completed-coordinate definitions + PSF-01--PSF-05 and PSF-07; unrecombined radial or full-vector estimates are excluded.

## Statement
For every \(K'<\infty\), there exist \(C_{K'}<\infty\) and \(N_{K'}\)
such that the following holds for \(N\ge N_{K'}\). Let \(q=(d,w)\) lie in
the finite-bridge image and satisfy
\[
\mathcal N_N(q)\le K'a^5.
\]
Let \(\mathfrak Q_N(t;q)\) be the exact disjoint full-cell expression supplied
by JC_SP_LEDGER, so that
\[
D^3\mathbf A_N(tq)[q,q,q]=\mathfrak Q_N(t;q),
\qquad 0\le t\le1.
\]
Then
\[
\left|\mathfrak Q_N(t;q)\right|
\le C_{K'}r_N(q)\mathcal N_N(q),
\qquad 0\le t\le1,
\]
with constants independent of \(N\), the completed ray, and all side-length
ratios admitted by the finite-bridge image.

## Dependencies

- JC_SP_LEDGER supplies the exact common completed scalar derivative and a
  disjoint complete full-cell formula for \(\mathfrak Q_N(t;q)\).
- Definitions supplies \(a,\mathcal N_N,r_N,\mathbf A_N,J_\alpha,c_\alpha\)
  and the finite-bridge image.

## Proof Strategy
Status: todo
- Plan: Kind: residual — bound the already-resummed QRCI blocks in the natural energy, preserving full-cell and endpoint cancellations before applying Cauchy--Schwarz or Schur estimates.
- Key obstacle: unrecombined full-vector Hessian bounds lose \(a^{-2}\) on alternating support data, while termwise terminal estimates create artificial logarithms.
- Needed dependencies: exact block formulas and regularity from JC_SP_QRCI; ratio-free reduced-DtN, endpoint, ground-state, metric, corrector, and gauge bounds.
- Failure trigger: constant-estimate insufficient if any genuine block is larger than \(Cr_N\mathcal N_N\); interface mismatch if the JC_SP_QRCI ledger omits or duplicates a descendant.

## Experiments and Edge Cases
Status: todo

No check has yet been promoted. Stage 4 must separately test alternating,
localized, and highest-frequency rays against the explicit QRCI blocks.

### Check 1: inherited cubic-scale calibration
- Model: localized balanced fan data and highest-frequency support data normalized by \(\mathcal N_N(q)\asymp a^5\).
- Method: PSF-01, PSF-04, and PSF-07; compare the exact fan third jet and the required \(r_N\mathcal N_N\) scale without using an unrecombined spectral bound.
- Result: both families have target size \(O(a^{11/2})\); no estimate for the spectral QRCI blocks is obtained.
- Interpretation: inconclusive; next action audit the explicit JC_SP_QRCI block ledger before testing this residual bound.

## Counterexample Search
Status: todo

Search the explicit identity for an uncancelled inverse-angle, endpoint
logarithm, or high-frequency multiplier on exact active rays.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo
