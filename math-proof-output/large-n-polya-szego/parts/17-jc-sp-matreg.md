# JC_SP_MATREG: Typed Material Spectral and Corner Regularity

## Local Summary
- Statement: superseded by JC_SP_MATFLUX
- Dependencies: Definitions
- Current obstruction: the compatible trace spaces and the two-family corner extraction map require a fresh fixed-order claim audit.
- Proof status: todo
- Next action: Stage 4 audit of the typed lifting, weak conormal, sector extraction, and common/jump conventions
- Local Context Packet: this statement + the completed ray \(Y_t,B_t\) + the active finite-bridge image + the compatible trace quotient norm + PSF-02--PSF-05 and PSF-07; no atom identity or uniform estimate is assumed.

## Statement
<!-- math-proof-ledger: {"object":"P_t_Y","kind":"local-only","depends_on":["Q8"],"reason":"the completed scalar's perturbed polygon family"} -->
<!-- math-proof-ledger: {"object":"P_t_B","kind":"local-only","depends_on":["Q8"],"reason":"the completed scalar's base polygon family"} -->
<!-- math-proof-ledger: {"object":"T_t_epsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"piecewise-affine material maps for the two families"} -->
<!-- math-proof-ledger: {"object":"X_epsilon","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"compatible global material trace spaces"} -->
<!-- math-proof-ledger: {"object":"L_epsilon","kind":"local-only","depends_on":["X_epsilon"],"reason":"bounded right inverses of the global trace"} -->
<!-- math-proof-ledger: {"object":"a_t_epsilon","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"pulled-back stiffness forms"} -->
<!-- math-proof-ledger: {"object":"m_t_epsilon","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"pulled-back mass forms"} -->
<!-- math-proof-ledger: {"object":"lambda_t_epsilon","kind":"local-only","depends_on":["a_t_epsilon","m_t_epsilon"],"reason":"first eigenvalues of the two material families"} -->
<!-- math-proof-ledger: {"object":"u_t_epsilon","kind":"local-only","depends_on":["a_t_epsilon","m_t_epsilon"],"reason":"normalized positive first eigenfunctions"} -->
<!-- math-proof-ledger: {"object":"S_t_epsilon","kind":"local-only","depends_on":["a_t_epsilon","m_t_epsilon","lambda_t_epsilon","u_t_epsilon"],"reason":"reduced resolvents"} -->
<!-- math-proof-ledger: {"object":"Lambda_t_epsilon_red","kind":"local-only","depends_on":["S_t_epsilon","L_epsilon"],"reason":"typed pole-free reduced-DtN blocks"} -->
<!-- math-proof-ledger: {"object":"c_i_epsilon","kind":"local-only","depends_on":["u_t_epsilon"],"reason":"leading sector amplitudes"} -->
<!-- math-proof-ledger: {"object":"e_i_epsilon","kind":"local-only","depends_on":["c_i_epsilon"],"reason":"leading material conormal coefficients"} -->
<!-- math-proof-ledger: {"object":"a_t","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"parser alias for the two pulled-back stiffness forms"} -->
<!-- math-proof-ledger: {"object":"S_t","kind":"local-only","depends_on":["a_t"],"reason":"parser alias for the two reduced resolvents"} -->
<!-- math-proof-ledger: {"object":"omega_i","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"common labelled interior angle"} -->
<!-- math-proof-ledger: {"object":"eta","kind":"local-only","depends_on":["omega_i"],"reason":"normalized angular coordinate in one material sector"} -->
<!-- math-proof-ledger: {"object":"c_i","kind":"local-only","depends_on":["u_t_epsilon"],"reason":"parser alias for the two leading sector amplitudes"} -->
<!-- math-proof-ledger: {"object":"e_i","kind":"local-only","depends_on":["c_i"],"reason":"parser alias for the two leading conormal coefficients"} -->
<!-- math-proof-ledger: {"object":"epsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"branch label ranging over Y and B"} -->
<!-- math-proof-ledger: {"object":"\\varepsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"displayed branch label ranging over Y and B"} -->

For every \(K'<\infty\), there is \(N_{K'}\) such that the following holds
for \(N\ge N_{K'}\) and every \(q=(d,w)\) in the finite-bridge image with
\(\mathcal N_N(q)\le K'a^5\).

For \(0\le t\le1\), let
\[
 P_t^Y=P_{\alpha_t}(Y_t),\qquad P_t^B=P_{\alpha_t}(B_t)
\]
be the two polygon families appearing in the exact completed scalar.  Write
\(\varepsilon\in\{Y,B\}\).  Triangulate each \(P_0^\varepsilon\) from its
fixed interior origin to its labelled sides, and let
\(T_t^\varepsilon:P_0^\varepsilon\to P_t^\varepsilon\) be the corresponding
label-preserving piecewise-affine material map.  Put
\[
 \mathcal H_\varepsilon=H_0^1(P_0^\varepsilon).
\]

Let
\[
 \mathcal X_\varepsilon
 =\operatorname{Tr}H^1(P_0^\varepsilon)
\]
carry the quotient norm
\[
 \|f\|_{\mathcal X_\varepsilon}
 =\inf\{\|F\|_{H^1(P_0^\varepsilon)}:\operatorname{Tr}F=f\},
\]
Its Hilbert dual is denoted by \(\mathcal X_\varepsilon^*\).  Thus, under
labelled side coordinates, \(\mathcal X_\varepsilon\) is the compatible
global boundary-trace subspace, not the whole product of independent
edgewise \(H^{1/2}\) spaces.  Fix a bounded right inverse
\[
 L_\varepsilon:\mathcal X_\varepsilon\longrightarrow
 H^1(P_0^\varepsilon)
\]
of the trace.  Also put
\[
 \mathcal S_\varepsilon=\prod_{i=1}^N H^{1/2}(0,1)
\]
for strong open-side conormal data; no lifting is asserted on
\(\mathcal S_\varepsilon\).

Let \(a_t^\varepsilon,m_t^\varepsilon\) be the pulled-back stiffness and
mass forms.  In addition to their restrictions on
\(\mathcal H_\varepsilon\), use
\(\widetilde A_t^\varepsilon,\widetilde M_t^\varepsilon:
H^1(P_0^\varepsilon)\to\mathcal H_\varepsilon^*\) for the same forms with
the trial slot extended to \(H^1\).  Let
\((\lambda_t^\varepsilon,u_t^\varepsilon)\) be the positive,
\(m_t^\varepsilon\)-normalized first eigenpair.  Define
\[
 \Pi_t^\varepsilon F
 =F-F(u_t^\varepsilon)m_t^\varepsilon(u_t^\varepsilon,\cdot)
\]
and let \(S_t^\varepsilon:\mathcal H_\varepsilon^*\to
\mathcal H_\varepsilon\) be the inverse of
\(A_t^\varepsilon-\lambda_t^\varepsilon M_t^\varepsilon\) on the
\(m_t^\varepsilon\)-orthogonal complement, preceded by
\(\Pi_t^\varepsilon\).

The weak material conormal and pole-free reduced solution are
\[
 \langle\Gamma_t^\varepsilon,f\rangle
 =a_t^\varepsilon(u_t^\varepsilon,L_\varepsilon f)
  -\lambda_t^\varepsilon
   m_t^\varepsilon(u_t^\varepsilon,L_\varepsilon f),
\]
\[
 v_t^\varepsilon(f)
 =L_\varepsilon f
  -S_t^\varepsilon\Pi_t^\varepsilon
   (\widetilde A_t^\varepsilon
    -\lambda_t^\varepsilon\widetilde M_t^\varepsilon)L_\varepsilon f.
\]
The first formula is independent of the chosen lift because the difference
of two lifts lies in \(\mathcal H_\varepsilon\).  Define
\[
 \langle\Lambda_t^{\varepsilon,\mathrm{red}}f,g\rangle
 =a_t^\varepsilon(v_t^\varepsilon(f),L_\varepsilon g)
  -\lambda_t^\varepsilon
   m_t^\varepsilon(v_t^\varepsilon(f),L_\varepsilon g).
\]

Let \(\omega_i(t)\in(0,\pi)\) be the common interior angle of
\(P_t^Y\) and \(P_t^B\) at the labelled vertex \(i\), and set
\(\beta_i(t)=\pi/\omega_i(t)>1\).  In physical polar distance \(r\) from
that vertex and normalized angular coordinate
\(\eta=\theta/\omega_i(t)\), define \(c_i^\varepsilon(t)\) to be the leading
sector coefficient in
\[
 u_t^\varepsilon(r,\eta)
 =c_i^\varepsilon(t)r^{\beta_i(t)}\sin(\pi\eta)
  +o(r^{\beta_i(t)}).
\]
Define \(e_i^\varepsilon(t)=\beta_i(t)c_i^\varepsilon(t)\); the fixed
orientation signs on the two incident sides are not included in
\(e_i^\varepsilon\).  Finally set
\[
 A_i^{\mathrm c}=\frac{c_i^Y+c_i^B}{2},\quad
 A_i^{\mathrm j}=c_i^Y-c_i^B,\qquad
 E_i^{\mathrm c}=\frac{e_i^Y+e_i^B}{2},\quad
 E_i^{\mathrm j}=e_i^Y-e_i^B.
\]
These formulas, rather than an unnamed endpoint convention, define the
ordered coefficient vector in
\[
 \mathcal C_N
 =\mathbb R_\beta^N\times\mathbb R_A^{2N}\times\mathbb R_E^{2N}.
\]

Then:

1. for both \(\varepsilon=Y,B\), the maps
   \[
   t\mapsto
   (a_t^\varepsilon,m_t^\varepsilon,
    \widetilde A_t^\varepsilon,\widetilde M_t^\varepsilon,
    \lambda_t^\varepsilon,u_t^\varepsilon,S_t^\varepsilon)
   \]
   are \(C^3\) in their displayed scalar, form, vector, and bounded-operator
   topologies;
2. \(t\mapsto\Gamma_t^\varepsilon\) is \(C^3\) into
   \(\mathcal X_\varepsilon^*\), and
   \(t\mapsto\Lambda_t^{\varepsilon,\mathrm{red}}\) is \(C^3\) into
   \(\mathcal B(\mathcal X_\varepsilon,\mathcal X_\varepsilon^*)\);
3. the pulled-back open-side conormal traces are \(C^3\) into
   \(\mathcal S_\varepsilon\), and the displayed map into
   \(\mathcal C_N\) is \(C^3\); more precisely, for a fixed cutoff
   \(\chi\) at each material vertex, subtracting the two oriented profiles
   \[
   \pm e_i^\varepsilon(t)\chi(r)r^{\beta_i(t)-1}
   \]
   leaves a \(C^3\) map into the corresponding edgewise
   \(H^{1/2}\) spaces; and
4. all derivatives through order three agree with the common material weak
   formulation.  Derivatives of the endpoint profiles are the ordinary
   \(H^{1/2}\)-valued derivatives generated by
   \(r^{\beta_i(t)-1}(\log r)^j\), \(0\le j\le3\).  Any later Eulerian
   endpoint distribution must be defined in JC_SP_LEDGER as the pushforward
   of these fixed-material derivatives; no additional distribution is
   asserted here.

The assertion is pointwise on each active completed ray.  It gives no
constant uniform in a collapsing side ratio and asserts neither the QRCI atom
identity nor its natural-energy estimate.

## Dependencies

- Definitions supplies \(\alpha_t,Y_t,B_t\), the exact completed scalar, the
  finite-bridge image, and the active material ray.
- Convexity and the finite-bridge bound give genuine nondegenerate labelled
  triangles and \(\inf_{i,t}(\beta_i(t)-1)>0\) for the fixed ray.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — first type-check the compatible trace quotient and the two-family material maps; then prove form/eigenpair/resolvent regularity, sector coefficient extraction, and the edgewise fractional-Sobolev endpoint profile estimates as one coherent mechanism.
- Key obstacle: \(C^3(H_0^1)\) eigenpair dependence must be upgraded to a \(C^3\) leading sector coefficient without using an incompatible product-edge lifting.
- Needed dependencies: the closed active ray, simplicity of each first eigenvalue, a fixed material sector at each labelled vertex, and the exact two-family definitions above.
- Failure trigger: interface mismatch if the quotient trace, strong side trace, or leading sector coefficient does not support the displayed \(C^3\) topology; statement likely false if a legal fixed ray loses the leading expansion.

## Experiments and Edge Cases
Status: todo

### Check 1: incompatible product-edge lifting
- Model: two adjacent unit intervals meeting at one vertex, with boundary values \(1\) and \(0\) at the common endpoint.
- Method: experiments/check_jc_sp_matreg_trace.py evaluates the exact truncated cross-edge \(H^{1/2}\) integral after unfolding the two intervals.
- Result: each edge datum is separately in \(H^{1/2}\), while the cross-edge integral diverges logarithmically; the old product space was too large and the replacement quotient trace space excludes this datum.
- Interpretation: supports the replacement interface by refuting precisely the larger old lifting domain.

### Check 2: reduced spectral block
- Model: the exact rotating \(2\times2\) simple eigenpair in experiments/check_jc_sp_reg_toy.py.
- Method: differentiate the projected resolvent and reduced Schur block three times.
- Result: every denominator is a power of the positive spectral gap.
- Interpretation: supports the fixed-domain spectral mechanism but not sector extraction.

### Check 3: endpoint profile threshold
- Model: \(\chi(r)r^\gamma(\log r)^j\), with \(\gamma=\beta-1>0\) and \(0\le j\le3\).
- Method: experiments/check_jc_sp_matreg_trace.py verifies the third exponent derivative and the exact dyadic ratio; the one-dimensional \(H^{1/2}\) difference quotient supplies the dyadic majorant.
- Result: for fixed \(\gamma>0\), dyadic scaling gives a convergent series
  bounded by a constant times
  \(\sum_{k\ge0}2^{-2\gamma k}(1+k)^{2j}\); cross-scale terms obey the same
  geometric bound, so the profile lies in \(H^{1/2}(0,1)\).
- Interpretation: supports the endpoint topology pointwise on each fixed active ray; it gives no uniform bound as \(\gamma\downarrow0\).

## Counterexample Search
Status: todo

Test the replacement against cross-edge jumps, an angle tending to \(\pi\)
along a fixed ray, a triangle Jacobian tending to zero, and a first-eigenvalue
collision.  The last three are excluded only if compactness of the closed
active ray supplies a strictly positive ray-dependent margin.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: stopped by independent Stage 4 counterexample search
Recent failed attempt: interface mismatch — the fixed-side scalar conormal
coefficient needs the factor
\((\ell_t/\ell_0)^{\beta-1}\), while the weak flux-density pullback needs
\((\ell_t/\ell_0)^\beta\); one endpoint coefficient per vertex and branch
cannot encode both incident side ratios.
Superseded attempts: A8 replaced the ill-typed JC_SP_REG interface.

## Local Audit
Status: failed

## Route Correction

Trigger: independent fixed-side-coordinate attack of the endpoint profile
(Attack A9).

Failure: the statement did not choose scalar versus flux-density pullback and
omitted the incident-side length-ratio factors.

Failure type: interface mismatch.

Replacement: JC_SP_MATFLUX distinguishes the two pullbacks and uses four
common/jump endpoint coordinates per vertex.

Stale Scope: only JC_SP_MATREG; JC_SP_LEDGER is rewired to the replacement.
