# JC_SP_REG: Boundary and Corner Regularity

## Local Summary
- Statement: superseded by JC_SP_MATREG
- Dependencies: Definitions
- Current obstruction: form-level eigenpair smoothness has not been upgraded to the boundary, corner, reduced-resolvent, and endpoint data required by the QRCI ledger.
- Proof status: todo
- Next action: Stage 4 claim audit of the exact spaces and endpoint pairings
- Local Context Packet: this statement + completed-ray definitions + fixed material triangulation + convex-corner exponent range + promoted attack A7 + PSF-02--PSF-05 and PSF-07; no ledger identity or uniform estimate is assumed.

## Statement
<!-- math-proof-ledger: {"object":"P_t","kind":"local-only","depends_on":["Q8"],"reason":"polygon along the active completed ray inside this part"} -->
<!-- math-proof-ledger: {"object":"T_t","kind":"local-only","depends_on":["Q8"],"reason":"piecewise-affine material map used only by this regularity claim"} -->
<!-- math-proof-ledger: {"object":"a_t","kind":"local-only","depends_on":["T_t"],"reason":"pulled-back stiffness form"} -->
<!-- math-proof-ledger: {"object":"m_t","kind":"local-only","depends_on":["T_t"],"reason":"pulled-back mass form"} -->
<!-- math-proof-ledger: {"object":"lambda_t","kind":"local-only","depends_on":["a_t","m_t"],"reason":"first eigenvalue along the local ray"} -->
<!-- math-proof-ledger: {"object":"u_t","kind":"local-only","depends_on":["a_t","m_t"],"reason":"normalized first eigenfunction along the local ray"} -->
<!-- math-proof-ledger: {"object":"S_t","kind":"local-only","depends_on":["a_t","m_t","lambda_t","u_t"],"reason":"reduced resolvent in this part"} -->
<!-- math-proof-ledger: {"object":"A_t","kind":"local-only","depends_on":["a_t"],"reason":"operator induced by the local stiffness form"} -->
<!-- math-proof-ledger: {"object":"M_t","kind":"local-only","depends_on":["m_t"],"reason":"operator induced by the local mass form"} -->
<!-- math-proof-ledger: {"object":"Pi_t","kind":"local-only","depends_on":["u_t","m_t"],"reason":"local ground-state projection"} -->
<!-- math-proof-ledger: {"object":"L","kind":"local-only","depends_on":[],"reason":"fixed boundary lifting convention for this part"} -->
<!-- math-proof-ledger: {"object":"Lambda_t_red","kind":"local-only","depends_on":["A_t","M_t","S_t","Pi_t","L"],"reason":"pole-free reduced-DtN block"} -->
For every \(K'<\infty\), there is \(N_{K'}\) such that the following holds
for \(N\ge N_{K'}\) and every \(q=(d,w)\) in the finite-bridge image with
\(\mathcal N_N(q)\le K'a^5\).

Let \(P_t\) be the polygon represented by \(tq\). Triangulate \(P_0\) from its
fixed interior origin to its sides and let \(T_t:P_0\to P_t\) be the
vertex-fixing piecewise-affine material map. On
\(\mathcal H=H_0^1(P_0)\), let \(a_t,m_t\) be the pulled-back stiffness and
mass forms, let \((\lambda_t,u_t)\) be the positive \(m_t\)-normalized first
eigenpair, and let \(S_t\) be the reduced resolvent on the
\(m_t\)-orthogonal complement of \(u_t\).

After identifying every open side with \((0,1)\), put
\[
\mathcal T_N^+=\prod_{i=1}^N H^{1/2}(0,1),
\qquad
\mathcal T_N^-=\prod_{i=1}^N H^{-1/2}(0,1)
\]
for strong and weak material side data.

Write \(A_t,M_t:\mathcal H\to\mathcal H^*\) for the form operators and
\[
\Pi_tF=F-F(u_t)m_t(u_t,\cdot).
\]
Fix one bounded material boundary lifting
\(L:\mathcal T_N^+\to H^1(P_0)\). For \(f\in\mathcal T_N^+\), define the
pole-free reduced solution and reduced-DtN block by
\[
v_t(f)=Lf-S_t\Pi_t(A_t-\lambda_tM_t)Lf,
\]
\[
\langle\Lambda_t^{\mathrm{red}}f,g\rangle
=a_t(v_t(f),Lg)-\lambda_tm_t(v_t(f),Lg),
\qquad g\in\mathcal T_N^+.
\]
The \(m_t\)-orthogonality built into \(S_t\) fixes the ground-state ambiguity;
this displayed choice of \(L\) and projection is the reduced-DtN convention
used by JC_SP_LEDGER.

Let
\[
\mathcal C_N
=\mathbb R_\beta^N\times\mathbb R_A^{2N}\times\mathbb R_E^{2N}
\]
have the explicitly ordered coordinates
\[
\bigl(\beta_i,\ A_i^{\mathrm c},A_i^{\mathrm j},\
E_i^{\mathrm c},E_i^{\mathrm j}:1\le i\le N\bigr),
\]
where \(A_i^{\mathrm c},A_i^{\mathrm j}\) are the common/jump corner
amplitudes and \(E_i^{\mathrm c},E_i^{\mathrm j}\) are the renormalized
endpoint coefficients used by the terminal/complement blocks. Their material
derivatives through order three are the derivatives of this \(C^3\)
coefficient map, not additional coordinates.

1. \(t\mapsto(a_t,m_t,\lambda_t,u_t,S_t)\) is \(C^3\) in
   \[
   \mathcal B(\mathcal H,\mathcal H^*)^2
   \times\mathbb R\times\mathcal H
   \times\mathcal B(\mathcal H^*,\mathcal H);
   \]
2. the pulled-back ground-state conormal trace and the displayed coefficient
   vector are \(C^3\) maps into \(\mathcal T_N^+\) and
   \(\mathcal C_N\), respectively;
3. the displayed reduced-DtN block is \(C^3\) as a map into
   \(\mathcal B(\mathcal T_N^+,\mathcal T_N^-)\), and all third material
   derivatives of the corner-power,
   annular-complement, and endpoint-pairing expressions used by
   JC_SP_LEDGER exist in their displayed operator or finite-dimensional
   topologies; and
4. these derivatives equal the derivatives obtained from the common material
   weak formulation, including every logarithmic exponent derivative and
   endpoint distribution.

The assertion is pointwise in each active ray. It does not claim constants
uniform in a side ratio tending to zero and does not assert the later QRCI
identity or its natural-energy bound.

## Dependencies

- Definitions supplies the completed ray, active finite-bridge image, exact
  scalar, quotient transport, and disk corrector.
- Convexity gives corner exponent \(\beta_i(t)>1\); on the super-near branch
  these exponents remain in one interval just above \(1\).

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — construct the common piecewise-affine pullback, prove \(C^3\) form and reduced-resolvent dependence by an implicit-function argument, then obtain side traces and corner coefficients from the convex polygonal elliptic decomposition in fixed material coordinates.
- Key obstacle: form-level \(C^3\) does not automatically provide endpoint distributions or differentiable corner coefficients.
- Needed dependencies: nondegenerate material triangles on the closed active ray, simplicity of the first eigenvalue, convex-corner \(H^2\) regularity, and a coefficient extraction map stable under three material derivatives.
- Failure trigger: missing hypothesis if a required trace is not defined in the stated space; interface mismatch if an endpoint distribution needs data outside \(\mathcal T_N^+\times\mathcal T_N^-\times\mathcal C_N\); statement likely false if a legal active ray loses \(C^3\) boundary data.

## Experiments and Edge Cases
Status: done

### Check 1: model corner and material pullback
- Model: a convex wedge power with exponent \(\beta>1\) and a nondegenerate affine material triangle.
- Method: PSF-02, PSF-03, PSF-05, and PSF-07; exact symbolic log-moment and pulled-back coefficient differentiation in experiments/check_jc_sp_qrci_corner.py.
- Result: third exponent derivatives remain energy-integrable as \(\beta\downarrow1\), and all material coefficient poles are powers of the triangle Jacobian.
- Interpretation: supports the stated spaces for the model term but is inconclusive for actual reduced-DtN and coefficient extraction; next action audit every map in the statement.

### Check 2: simple eigenpair and reduced Schur block
- Model: a rotating \(2\times2\) simple eigenpair with positive spectral gap, coupled to a two-dimensional boundary block.
- Method: PSF-04, PSF-05, and PSF-07; experiments/check_jc_sp_reg_toy.py constructs the exact reduced resolvent and reduced boundary Schur block and differentiates it three times symbolically.
- Result: the reduced resolvent identity holds exactly; every possible denominator in the third reduced-DtN derivative is a power of the positive spectral gap.
- Interpretation: supports the projected reduced-DtN convention and identifies the spectral gap as the only finite-dimensional regularity obstruction; next action test whether geometry or corner extraction introduces a new obstruction.

### Check 3: independent degeneration search
- Model: alternating, localized, and highest-frequency completed rays, together with prospective side collapse, corner resonance, and first-eigenvalue collision.
- Method: PSF-01--PSF-05 and PSF-07; combine the retained activity estimate \(\lvert\Delta\ell_i\rvert=O_{K'}(a^{3/2})\) with reference sides \(\ell_i\asymp a\), the convex exponent formula \(\beta_i=\pi/(\pi-\alpha_i)\), and simplicity of the positive first Dirichlet eigenfunction.
- Result: for large \(N\), every finite-bridge ray has side lengths comparable to \(a\), exponents in a fixed interval immediately above \(1\), and a simple first eigenvalue. Thus side collapse, integer exponent crossing, and eigenvalue collision are outside this target; the high-frequency families alter norms but not existence of the displayed maps.
- Interpretation: supports the exact scope of JC_SP_REG but does not prove \(C^3\) corner-coefficient extraction; next action prove that extraction from the fixed material sector expansion.

## Counterexample Search
Status: done

Check 3 is the independent counterexample search. It excludes the canonical
geometric and spectral degenerations from the finite-bridge image. The only
unresolved falsifier is failure of \(C^3\) coefficient extraction or endpoint
pairing despite a \(C^3\) form eigenpair; Stage 5 must derive those maps from a
fixed material sector expansion rather than infer them from \(H_0^1\)
smoothness.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: stopped by the Stage 5 strategy gate
Recent failed attempt: interface mismatch — the product-edge space has no
global \(H^1\) right inverse, the displayed lifted operator is ill-typed, and
one polygon family does not define the two common/jump coefficient channels.
Superseded attempts: A7 in the stale JC_SP_QRCI row exposed this interface

## Route Correction

Trigger: the first Stage 5 proof-strategy type check of the boundary lifting,
extended form operator, and coefficient extraction map (Attack A8).

Failure: the asserted product-edge lifting and one-family coefficient vector
are not well-defined as written.

Failure type: interface mismatch.

Replacement: JC_SP_MATREG uses the compatible global trace space, extended
trial-slot forms, and both completed-scalar polygon families.

Stale Scope: only JC_SP_REG; JC_SP_LEDGER is rewired to the replacement and
remains unproved.

## Local Audit
Status: in-progress

- Required depth: D3 audit-ready regularity proof.
- Statement strength: the claim freezes only the form, reduced-resolvent,
  reduced-DtN, open-side trace, corner amplitude, and renormalized endpoint
  maps imported by JC_SP_LEDGER. It asserts neither the ledger identity nor
  any \(N\)-uniform natural-energy estimate.
- Checklist: PSF-01 affects later constants but not pointwise existence;
  PSF-02--PSF-05 and PSF-07 are exercised in Checks 1--3; PSF-06 and PSF-08
  are not local to this child.
- Experiments: Checks 1--2 verify the model corner integrability, material
  coefficient regularity, spectral projection, and reduced Schur mechanism.
- Edge cases: Check 3 shows that side collapse, corner resonance, and first
  eigenvalue multiplicity are outside the finite-bridge image.
- Independent counterexample search: Check 3 finds no counterexample; the
  still-unproved coefficient extraction is a proof obligation, not evidence.
- Dependency check: Definitions supplies the completed ray and material
  scalar. No ledger atom, uniform estimate, coarse bound, parent action, or
  theorem conclusion is assumed.
- Notation check: \(\mathcal H,A_t,M_t,\Pi_t,S_t,L,
  \Lambda_t^{\mathrm{red}},\mathcal T_N^\pm,\mathcal C_N\) are defined in
  this part and mirrored in definitions-and-notation.md where shared.
- Citation need: none. The proof can use a local fixed-domain
  implicit-function argument and the explicit separated expansion on each
  convex material sector; no external boundary theorem is imported.
- Adaptive Decomposition Gate: A7 already isolates this boundary package.
  The four displayed maps share one common fixed-domain regularity mechanism,
  and no further objective split is visible before a coherent proof attempt.
- Audit outcome: viable pending preaudit_lint.py and final Stage 4 validation.
