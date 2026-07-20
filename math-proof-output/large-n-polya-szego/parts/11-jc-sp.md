# JC_SP: Super-Near Completed Jet

## Local Summary
- Statement: superseded by JC_SP_EST and JC_SP_QRCI
- Dependencies: Definitions
- Current obstruction: the full-cell QRCI identity and its uniform operator bounds have not been proved after all terminal, complement, endpoint, moving-metric, and ground-state terms are combined.
- Proof status: todo
- Next action: use replacement rows JC_SP_QRCI and JC_SP_EST
- Local Context Packet: this statement + completed-coordinate definitions + the exact terminal/complement resummation + promoted split evidence A5 + PSF-01--PSF-05 and PSF-07; no scalar radial \(H^{1/2}\) shortcut.

## Statement
For every \(K'<\infty\), there exist constants \(C_{K'}<\infty\) and
\(N_{K'}\), independent of the smallest positive fan angle and all adjacent
angle and side ratios, such that the following holds. Let \(N\ge N_{K'}\),
\(a=2\pi/N\), and let \(q=(d,w)\) be the completed coordinate associated by
the retained finite bridge to an active normalized support path, with
\[
\mathcal N_N(q)
=a^2\sum_i d_i^2+\mathcal G^{\mathrm{JP}}_{\alpha_*}(w)
\le K'a^5.
\]
Then the exact completed scalar \(\mathbf A_N\), with all moving-fan,
disk-corrector, quotient-transport, ground-state, metric, area,
base-subtraction, terminal, nonterminal, and lower-row terms retained, is
three times differentiable on the real segment \(tq\), \(0\le t\le1\), and
\[
\left|D^3\mathbf A_N(tq)[q,q,q]\right|
\le C_{K'}r_N(q)\mathcal N_N(q),
\qquad
r_N(q)=\frac{\|d\|_\infty}{a}
+a^{-2}\mathcal G^{\mathrm{JP}}_{\alpha_*}(w)^{1/2}.
\]
The constants must be uniform in \(N\) and all no-ratio degenerations.

## Dependencies

- Definitions supplies \(a,\mathcal N_N,r_N\), the completed scalar, and the
  no-ratio convention.
- The retained finite bridge supplies the completed-coordinate chart,
  full-segment activity, and \(r_N(q)\le C_{K'}a^{1/2}\).
- The retained JC--AR interface supplies
  \(\frac12D^2\mathbf A_N(0)[q,q]\ge\mu_0\mathcal N_N(q)\), with
  \(\mu_0>0\) uniform. This base Hessian is used only after the JC_SP estimate.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — derive a source-by-source resummed completed-jet scalar identity before taking absolute values. Terminal and annular-complement descendants must be recombined into full-cell amplitudes, followed by Schur or energy bounds for the genuine completed kernel.
- Key obstacle: polygonal vertex jumps make the scalar radial \(H^{1/2}\) analytic shortcut false, and separate estimates create artificial \(\beta\log\vartheta\) losses.
- Needed dependencies: uniform bounds for the resummed reduced-DtN block, endpoint descendants, true moving ground-state multiplier, \(J_\alpha,c_\alpha\), moving metric, and base subtraction.
- Failure trigger: constant-estimate insufficient if any bound is worse than \(r_N(q)\mathcal N_N(q)\); interface mismatch if a material derivative lies outside the completed scalar; statement likely false if an exact active completed ray violates the displayed jet estimate.

## Experiments and Edge Cases
Status: in-progress

### Check 1: exact full-cell resummation
- Model: one moving corner channel with analytic amplitude \(A(t)\), exponent \(\beta(t)\), cutoff \(\vartheta(t)\), and exact full-cell coefficient \(K_{\beta(t)}\), together with the pure fan fourth-defect row.
- Method: PSF-04, PSF-05, and PSF-07; experiments/check_jc_sp_scaling.py uses exact symbolic differentiation to combine the terminal term \(A^2\vartheta^{2\beta}K_\beta\) with its annular complement before differentiating, and separately differentiates \(\frac\kappa2\mathcal J_4(\alpha_*+td)\) three times.
- Result: the terminal-plus-complement residual and its third derivative vanish identically; the fan row is exactly \(12\kappa(a\sum_i d_i^3+t\sum_i d_i^4)\).
- Interpretation: supports the required order of operations and the claimed fan-row scale, but proves neither the other endpoint descendants nor the polygonal spectral row; next action test edge scaling and independent adversarial rays.

### Check 2: super-near edge scaling
- Model: pure-fan, pure-support, alternating, localized, and highest-frequency completed rays satisfying \(\mathcal N_N(q)\le K'a^5\), including rays directed toward the boundary \(d_i=-a\).
- Method: PSF-01, PSF-02, and PSF-03; use the exact fourth-defect lower bound and the retained metric bridge, then check the whole affine completed path rather than an auxiliary physical chord. For the fan third jet use \(\lvert a\sum d_i^3+t\sum d_i^4\rvert\le(\|d\|_\infty a+\|d\|_\infty^2)\sum d_i^2\).
- Result: \(r_N(q)\le C_{K'}a^{1/2}\), so for large \(N\) every fan angle on this branch is \(a(1+O_{K'}(a^{1/2}))\); an actual collapsing-angle degeneration cannot occur inside JC_SP. When \(r_N(q)\le1\), the fan third jet is bounded by \(24\kappa r_N(q)a^2\sum_i d_i^2\). The retained bridge proves activity of the exact completed path, including alternating and localized support data.
- Interpretation: supports the scope and scaling of JC_SP and shows that its no-ratio uniformity is confined to a quasiuniform super-near ball; next action search the completed scalar, rather than the fan geometry, for an inverse-angle or logarithmic obstruction.

### Check 3: independent committed-route repair
- Model: the whole compound JC_SP target on alternating, localized balanced, and highest-frequency completed rays at \(\mathcal N_N(q)\asymp a^5\).
- Method: author:agent:jc_sp_stage4_probe | phase:committed-route repair | PSF-01--PSF-05 and PSF-07 | attempt the whole target using only its frozen statement, Definitions, and direct dependencies, and require a concrete Adaptive Decomposition Gate trigger for any split.
- Result: verdict:split. The rays match the required \(a^{11/2}\) cubic scale and give no fan-row counterexample, but the direct interface contains neither the \(C^3\) full-cell identity nor the disjoint complete derivative ledger needed before uniform estimates. The minimal regularity/mechanism child is JC_SP_QRCI; the residual estimate is JC_SP_EST.
- Interpretation: supports the strict reduction \(\mathrm{JC\_SP\_QRCI}\Rightarrow\mathrm{JC\_SP\_EST}\) and supersedes the compound JC_SP row; next action execute Stage 3 route correction without changing the frozen theorem or selected route family.

## Counterexample Search
Status: in-progress

The independent search uses alternating, one-cell localized, and
highest-frequency quotient rays. The alternating family gives the exact jump
\[
J_i=\frac{w_{i+1}-w_i}{\cos(a/2)}
\]
and therefore an infinite scalar radial \(H^{1/2}\) seminorm; this refutes only
the radial-chart shortcut. The localized and highest-frequency families expose
the known \(a^{-2}\) loss in an unrecombined full-vector Hessian estimate.
Neither calculation is an exact counterexample to the completed scalar
third-jet estimate because both discard the terminal/complement and endpoint
chain-rule cancellations that define the target. The search is therefore
inconclusive, and failure to find a counterexample is not evidence for JC_SP.
The independent committed-route probe found no counterexample but confirmed
that none of these rays can be evaluated without first proving the exact
full-cell \(C^3\) identity. This is recorded as Check 3 and is a structural
split, not evidence that either replacement row is true.

## Proof
Status: todo

No proof is claimed. If the displayed third-jet estimate holds, Taylor
integration and the retained positive base Hessian give
\[
\mathbf A_N(q)
\ge\left(\mu_0-\frac{C_{K'}}2r_N(q)\right)\mathcal N_N(q)\ge0
\]
for sufficiently large \(N\).

## Proof Attempt Log
Active attempt: none
Recent failed attempt: A6 | author:agent:jc_sp_stage4_probe | interface mismatch — the compound row lacks a direct \(C^3\) full-cell identity before its uniform estimate
Superseded attempts: the original single-row JC_SP formulation is preserved above as audit provenance

## Local Audit
Status: todo

- Required depth: D3 audit-ready local proof; D1 calibration is not a proof.
- Statement strength: the displayed real diagonal third-jet estimate is the
  weakest currently recorded sufficient modulus for Taylor absorption. The
  uniform operator modulus and complex-tube Cauchy bound in the retained source
  are strictly stronger and are not part of JC_SP.
- Checklist: PSF-01 through PSF-05 and PSF-07 apply and are exercised above;
  PSF-06 belongs to the later global localization assembly; PSF-08 belongs to
  the parent theorem and equality audit.
- Experiments: Check 1 supports only the exact resummation mechanism.
- Edge cases: Check 2 verifies the energy scaling, the exact admissible path,
  and the fact that the super-near branch is automatically quasiuniform.
- Independent counterexample search: completed; the fixed adversarial families
  kill two shortcuts and calibrate the target scale but do not decide the
  completed scalar.
- Dependency check: the target statement uses Definitions and the already
  retained finite bridge/activity to specify its domain. JC--AR is needed only
  after the third-jet estimate, when Taylor absorption converts it to
  nonnegativity; neither JC_PL nor JC_CL is assumed. The retained source
  explicitly closes both the bridge/activity and the all-character JC--AR
  base Hessian before stating JC--SP.
- Notation check: \(a,\mathcal N_N,r_N,\mathbf A_N,d,w\) agree with
  definitions-and-notation.md and the retained completed normal form.
- Citation need: none; JC_SP is a project-specific analytic estimate and cannot
  be discharged by the verified quantitative Faber--Krahn citation.
- Adaptive Decomposition Gate: no further child interface is justified before
  the exact QRCI differentiation localizes a genuine independent regularity,
  boundary, citation, or quantifier obstruction.
- Audit outcome: superseded by the exact regularity/mechanism split recorded in
  Check 3; preaudit_lint.py was clean before the split.

## Route Correction
Trigger: Check 3 exposed an independent regularity and exact-complete-pair mechanism interface before any uniform estimate can be audited.
Failure: the compound JC_SP row combines existence of the \(C^3\) completed full-cell identity with the separate task of bounding that identity, while its declared direct dependency supplied neither interface.
Failure type: interface mismatch
Replacement: JC_SP_QRCI supplies the exact \(C^3\) identity and JC_SP_EST supplies its uniform \(r_N\mathcal N_N\) estimate.
Stale Scope: only the compound JC_SP row; the frozen theorem, JC_PL branch decomposition, JC_CL, retained base Hessian, and finite bridge remain live.
