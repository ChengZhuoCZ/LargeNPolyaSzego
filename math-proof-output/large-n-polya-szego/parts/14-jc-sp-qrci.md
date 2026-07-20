# JC_SP_QRCI: Exact Completed Third-Jet Identity

## Local Summary
- Statement: superseded by JC_SP_REG and JC_SP_LEDGER
- Dependencies: Definitions
- Current obstruction: the polygonal spectral third material derivative has not been written as one gauge-invariant disjoint full-cell ledger containing every corner, endpoint, metric, ground-state, area, and base descendant exactly once.
- Proof status: todo
- Next action: use replacement rows JC_SP_REG and JC_SP_LEDGER
- Local Context Packet: this statement + completed-scalar definitions + finite-bridge image + exact terminal/complement cancellation + promoted attack A6 + PSF-01--PSF-05 and PSF-07; no uniform estimate is part of this child.

## Statement
For every \(K'<\infty\), there is \(N_{K'}\) such that, for
\(N\ge N_{K'}\) and every \(q=(d,w)\) in the finite-bridge image with
\(\mathcal N_N(q)\le K'a^5\), the real map
\[
t\longmapsto\mathbf A_N(tq),\qquad 0\le t\le1,
\]
is three times continuously differentiable.

Put
\[
\alpha_t=\alpha_*+td,\quad
Y_t=h_{\alpha_t}\mathbf1+J_{\alpha_t}(c_{\alpha_t}+tw),\quad
B_t=h_{\alpha_t}\mathbf1,\quad
C_t=J_{\alpha_t}c_{\alpha_t},\quad
W_t=tJ_{\alpha_t}w.
\]
For a scalar family \(F\) along a material path \(X_t\), define
\[
\mathfrak D_t^3F[X_t]
=D^3F(X_t)[X_t',X_t',X_t']
+3D^2F(X_t)[X_t',X_t'']
+DF(X_t)[X_t'''].
\]
Then the completed third derivative obeys the exact chain-rule identity
\[
\begin{aligned}
D^3\mathbf A_N(tq)[q,q,q]
={}&\mathfrak D_t^3\Phi[\alpha_t,Y_t]
-\mathfrak D_t^3\Phi[\alpha_t,B_t]\\
&+\frac{d^3}{dt^3}\mathcal G^{\mathrm{JP}}_{\alpha_t}(C_t)
-\frac12\frac{d^3}{dt^3}
  \mathcal G^{\mathrm{JP}}_{\alpha_t}(W_t)\\
&+12\kappa\left(a\sum_i d_i^3+t\sum_i d_i^4\right)
=:\mathfrak Q_N(t;q).
\end{aligned}
\]
Moreover, the two \(\Phi\) material derivatives in this display admit one
explicit gauge-invariant full-cell expansion in which:

1. terminal two-ray and annular-complement powers are recombined before
   differentiation;
2. endpoint and nonendpoint descendants, same-cell, adjacent-cell, and
   first-separation pairs form a disjoint complete ledger;
3. moving ground-state, reduced-DtN, area, fixed-rank, quotient-transport,
   corrector, metric, and base-subtraction terms occur exactly once; and
4. every endpoint or corner differentiation is justified in the common
   material chart of the finite-bridge image.

The complete expansion must be written term by term in the Proof and checked
for omission and duplication before it is denoted by
\(\mathfrak Q_N(t;q)\) and imported by JC_SP_EST. Merely naming the
right-hand side does not establish this child. This child asserts the identity
and its regularity only; it asserts no uniform bound for its blocks.

## Dependencies

- Definitions supplies the completed scalar, material ray, quotient
  transport, disk corrector, natural energy, radius, and finite-bridge image.
- The exact terminal/complement algebra
  \(A^2\vartheta^{2\beta}K_\beta+
  A^2(1-\vartheta^{2\beta})K_\beta=A^2K_\beta\)
  is a calibration identity, not a substitute for the complete ledger.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — construct a common material pullback for every full cell, prove third differentiability there, differentiate the exact completed scalar, and only then collapse the terminal/complement and pair ledgers.
- Key obstacle: polygonal corners make the scalar radial \(H^{1/2}\) path nondifferentiable, so the identity must use a physical material chart with all endpoint descendants retained.
- Needed dependencies: exact material reduced-DtN representation, corner power expansion with complement, differentiability of the simple ground state under the common pullback, and differentiated formulas for \(h_\alpha,J_\alpha,c_\alpha,\mathcal G_\alpha^{\mathrm{JP}}\).
- Failure trigger: missing hypothesis if \(C^3\) requires unrecorded corner regularity; interface mismatch if any derivative lies outside the common scalar; statement likely false if a legal completed ray makes the material third derivative fail to exist.

## Experiments and Edge Cases
Status: todo

No child-specific check has yet been promoted. Stage 4 must distinguish exact
existence of the derivative from the later uniform estimate.

### Check 1: terminal-complement identity
- Model: one homogeneous corner channel with moving amplitude, exponent, and cutoff radius.
- Method: PSF-04, PSF-05, and PSF-07; experiments/check_jc_sp_qrci_corner.py combines the terminal and annular-complement powers by exact symbolic algebra before taking three material derivatives.
- Result: \(A^2\vartheta^{2\beta}K_\beta+A^2(1-\vartheta^{2\beta})K_\beta=A^2K_\beta\), and the residual remains identically zero after three derivatives.
- Interpretation: supports the full-cell resummation mechanism but is inconclusive for the complete pair ledger; next action audit \(C^3\) material regularity and every omitted descendant.

### Check 2: corner and material C3 calibration
- Model: a convex wedge singularity \(r^{\beta(t)}\sin(\beta(t)\theta)\), \(\beta(t)>1\), transported by a nondegenerate affine material triangle \(F_t=I+tH\).
- Method: PSF-02, PSF-03, PSF-05, and PSF-07; experiments/check_jc_sp_qrci_corner.py verifies exactly that \(\int_0^1r^{p-1}(-\log r)^m\,dr=m!/p^{m+1}\) through \(m=6\), and differentiates \(\det(F_t)F_t^{-1}F_t^{-T}\) three times.
- Result: the worst squared-gradient term created by three exponent derivatives is integrable uniformly down to \(\beta=1\), with sixth log moment \(45/8\); every pole in the pulled-back coefficient derivatives is a power of \(\det F_t\), so a fixed active material triangle has \(C^3\) coefficients.
- Interpretation: supports \(C^3\) form-level eigenpair regularity on each active completed ray, but does not supply the global reduced-DtN and pair ledger; next action independently test simplicity, side collapse, resonance, and omitted distributions.

### Check 3: independent boundary-regularity probe
- Model: the whole JC_SP_QRCI target on a fixed material triangulation, including the normalized ground state, reduced resolvent/DtN data, corner coefficients, endpoint traces, and endpoint distributions.
- Method: author:agent:qrci_stage4_probe | phase:committed-route repair | PSF-01--PSF-05 and PSF-07 | test alternating, localized, highest-frequency, near-side-collapse, and corner-resonance families and require an objective boundary/regularity trigger for any split.
- Result: verdict:split. Form-level \(C^3\) of the simple first eigenpair survives all tested families, but it does not justify three termwise derivatives of the reduced-DtN, corner coefficient, endpoint trace, and endpoint distribution data in any named weighted trace space. The minimal child is JC_SP_REG; the residual finite ownership identity is JC_SP_LEDGER.
- Interpretation: supports a strict boundary-regularity split and supersedes the compound JC_SP_QRCI row; next action execute Stage 3 correction and audit JC_SP_REG first.

## Counterexample Search
Status: in-progress

The independent falsification families are:

- alternating and highest-frequency support modes, whose radial-chart jump
  refutes that chart but is removed by a vertex-fixing material pullback;
- one side tending to zero across a sequence of active paths, which may destroy
  uniform constants but not \(C^3\) existence on any fixed closed active
  segment, since its minimum side length remains positive;
- corner-exponent resonance, which cannot cross the next integer on the
  super-near large-\(N\) fan because every interior exponent remains in a fixed
  interval just above \(1\); and
- eigenvalue collision, excluded at the first Dirichlet eigenvalue by
  positivity and simplicity on every connected convex polygon.

None refutes form-level \(C^3\). The bounded independent route probe instead
confirmed that endpoint distributions and corner/trace data require a named
weighted-space regularity interface before the full-cell ownership identity
can be audited.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: A7 | author:agent:qrci_stage4_probe | interface mismatch — boundary and corner data need an explicit \(C^3\) topology before ledger assembly
Superseded attempts: A6 in the stale compound JC_SP row exposed the identity-versus-estimate interface

## Local Audit
Status: in-progress

- Required depth: D3 audit-ready identity and regularity proof.
- Statement strength: JC_SP_QRCI asserts only \(C^3\) existence and the exact
  common-scalar ledger needed by its direct dependent. It does not assert the
  uniform \(r_N\mathcal N_N\) estimate, a holomorphic tube, or a full operator
  modulus.
- Checklist: PSF-01 is deferred to JC_SP_EST except for keeping the finite
  ledger independent of \(N\); PSF-02--PSF-05 and PSF-07 apply in Checks 1--2
  and the independent search; PSF-06 and PSF-08 are not local to this child.
- Experiments: Check 1 verifies only the exact full-cell cancellation.
- Edge cases: Check 2 treats corner logarithms and the common affine material
  chart without claiming a uniform side-ratio estimate.
- Independent counterexample search: completed; no form-level \(C^3\)
  counterexample is found, but the boundary data require a separate interface.
- Dependency check: Definitions now gives the exact completed scalar, finite
  bridge image, material ray, quotient transport, and corrector. JC_SP_EST,
  JC_CL, JC_PL, and the theorem are not assumed.
- Notation check: \(\alpha_t,Y_t,B_t,C_t,W_t,\mathfrak D_t^3\), and
  \(\mathfrak Q_N\) are local to this part; the global symbols agree with
  definitions-and-notation.md.
- Citation need: none at this stage. Form-level \(C^3\) regularity can be
  proved locally by a fixed-domain variational implicit-function argument,
  while the QRCI ledger is project-specific.
- Adaptive Decomposition Gate: Check 3 exposes a new boundary/regularity
  interface between form-level eigenpair smoothness and differentiability of
  the actual reduced-DtN, corner, trace, and endpoint data.
- Audit outcome: superseded by the boundary-regularity split recorded in
  Check 3; preaudit_lint.py was clean before the split.

## Route Correction
Trigger: Check 3 exposed the boundary and weighted-trace regularity required to differentiate reduced-DtN, corner, trace, and endpoint data before the atom ledger is formed.
Failure: form-level \(C^3\) of the pulled-back first eigenpair does not itself justify the three boundary and corner differentiations asserted by the compound identity row.
Failure type: interface mismatch
Replacement: JC_SP_REG supplies the explicit weighted trace/corner regularity and JC_SP_LEDGER supplies the residual atom-indexed full-cell identity.
Stale Scope: only the compound JC_SP_QRCI row; the frozen theorem, selected completed-action family, branch cutoff, JC_SP_EST, JC_CL, and retained bridges remain live.
