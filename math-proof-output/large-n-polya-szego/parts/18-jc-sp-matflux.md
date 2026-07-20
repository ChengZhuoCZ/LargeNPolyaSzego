# JC_SP_MATFLUX: Typed Material Flux and Corner Regularity

## Local Summary
- Statement: C3 two-family material spectral, compatible-trace, scalar-conormal, weak-flux, reduced-DtN, and incidence-level corner regularity
- Dependencies: Definitions
- Current obstruction: none
- Proof status: done
- Next action: none
- Local Context Packet: the frozen statement above; (H2) convex genuine
  polygonality; (Q8) one fixed finite-bridge completed ray; Definitions'
  \(\alpha_t,Y_t,B_t\) material chart; the compatible quotient trace and
  scalar/flux pullbacks; PSF-02--PSF-05 and PSF-07.  There is no citation or
  certificate, and no atom identity, endpoint pushforward, uniform estimate,
  coarse bound, parent action, or theorem conclusion is assumed.

## Statement
<!-- math-proof-ledger: {"object":"P_t_Y","kind":"local-only","depends_on":["Q8"],"reason":"perturbed completed-scalar polygon family"} -->
<!-- math-proof-ledger: {"object":"P_t_B","kind":"local-only","depends_on":["Q8"],"reason":"base completed-scalar polygon family"} -->
<!-- math-proof-ledger: {"object":"epsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"branch label Y or B"} -->
<!-- math-proof-ledger: {"object":"T_t_epsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"label-preserving piecewise-affine material maps"} -->
<!-- math-proof-ledger: {"object":"X_epsilon","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"compatible global material trace spaces"} -->
<!-- math-proof-ledger: {"object":"L_epsilon","kind":"local-only","depends_on":["X_epsilon"],"reason":"bounded right inverses of the global trace"} -->
<!-- math-proof-ledger: {"object":"a_t","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"two pulled-back stiffness forms"} -->
<!-- math-proof-ledger: {"object":"m_t","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"two pulled-back mass forms"} -->
<!-- math-proof-ledger: {"object":"lambda_t","kind":"local-only","depends_on":["a_t","m_t"],"reason":"two first eigenvalues"} -->
<!-- math-proof-ledger: {"object":"u_t","kind":"local-only","depends_on":["a_t","m_t"],"reason":"two normalized first eigenfunctions"} -->
<!-- math-proof-ledger: {"object":"S_t","kind":"local-only","depends_on":["lambda_t","u_t"],"reason":"two reduced resolvents"} -->
<!-- math-proof-ledger: {"object":"Gamma_t","kind":"local-only","depends_on":["u_t","L_epsilon"],"reason":"weak material conormal functionals"} -->
<!-- math-proof-ledger: {"object":"Lambda_t_red","kind":"local-only","depends_on":["S_t","L_epsilon"],"reason":"two pole-free reduced-DtN blocks"} -->
<!-- math-proof-ledger: {"object":"omega_i","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"common labelled interior angle"} -->
<!-- math-proof-ledger: {"object":"beta_i","kind":"local-only","depends_on":["omega_i"],"reason":"leading convex-sector exponent"} -->
<!-- math-proof-ledger: {"object":"rho_i_sigma_epsilon","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"incident-side material length ratio"} -->
<!-- math-proof-ledger: {"object":"c_i","kind":"local-only","depends_on":["u_t"],"reason":"physical leading sector amplitudes"} -->
<!-- math-proof-ledger: {"object":"e_i","kind":"local-only","depends_on":["c_i","beta_i"],"reason":"physical leading conormal coefficients"} -->
<!-- math-proof-ledger: {"object":"e_hat_i_sigma","kind":"local-only","depends_on":["e_i","rho_i_sigma_epsilon"],"reason":"scalar material endpoint coefficients"} -->
<!-- math-proof-ledger: {"object":"e_check_i_sigma","kind":"local-only","depends_on":["e_hat_i_sigma","rho_i_sigma_epsilon"],"reason":"weak flux-density endpoint coefficients"} -->
<!-- math-proof-ledger: {"object":"\\varepsilon","kind":"local-only","depends_on":["P_t_Y","P_t_B"],"reason":"displayed branch label Y or B"} -->
<!-- math-proof-ledger: {"object":"v_t","kind":"local-only","depends_on":["S_t","L_epsilon"],"reason":"two pole-free reduced material solutions"} -->
<!-- math-proof-ledger: {"object":"\\ell_{i,\\sigma}","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"physical incident-side lengths"} -->
<!-- math-proof-ledger: {"object":"r_t","kind":"local-only","depends_on":["rho_i_sigma_epsilon"],"reason":"physical arclength coordinate on the moving incident side"} -->
<!-- math-proof-ledger: {"object":"F_{i,t}","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"linear part of one material triangle map"} -->
<!-- math-proof-ledger: {"object":"\\eta","kind":"local-only","depends_on":["S_t"],"reason":"scalar multiplier in the augmented resolvent equation"} -->
<!-- math-proof-ledger: {"object":"\\delta","kind":"local-only","depends_on":["beta_i"],"reason":"fixed-ray positive convex-exponent margin"} -->
<!-- math-proof-ledger: {"object":"\\Psi_{i,t}","kind":"local-only","depends_on":["omega_i"],"reason":"moving physical sector parametrization"} -->
<!-- math-proof-ledger: {"object":"U_t","kind":"local-only","depends_on":["u_t","\\Psi_{i,t}"],"reason":"eigenfunction in fixed annular sector coordinates"} -->
<!-- math-proof-ledger: {"object":"y","kind":"local-only","depends_on":[],"reason":"integration variable in the endpoint Gagliardo calculation"} -->
<!-- math-proof-ledger: {"object":"j_*","kind":"local-only","depends_on":["Q8","Q11"],"reason":"positive material Jacobian margin after the ray and branch are fixed"} -->
<!-- math-proof-ledger: {"object":"R","kind":"local-only","depends_on":["Q8","Q11","Q12"],"reason":"sector radius chosen after fixing the ray, branch, and vertex"} -->
<!-- math-proof-ledger: {"object":"T_hat_t","kind":"local-only","depends_on":["Q8","Q11"],"reason":"second sector-compatible material map with fixed reference interfaces"} -->
<!-- math-proof-ledger: {"object":"alpha_t","kind":"local-only","depends_on":["Q8"],"reason":"parser alias for the completed fan path"} -->
<!-- math-proof-ledger: {"object":"r","kind":"local-only","depends_on":["Q12"],"reason":"physical radial variable in one fixed vertex sector"} -->
<!-- math-proof-ledger: {"object":"T_t","kind":"local-only","depends_on":["T_t_epsilon"],"reason":"parser alias for the original piecewise-affine material maps"} -->
<!-- math-proof-ledger: {"object":"b_{i,k}","kind":"local-only","depends_on":["u_t","Q12"],"reason":"Fourier--Bessel coefficients in one physical sector"} -->

For every \(K'<\infty\), there is \(N_{K'}\) such that the following holds
for \(N\ge N_{K'}\) and every \(q=(d,w)\) in the finite-bridge image with
\(\mathcal N_N(q)\le K'a^5\).

For \(0\le t\le1\), set
\[
P_t^Y=P_{\alpha_t}(Y_t),\qquad P_t^B=P_{\alpha_t}(B_t),
\]
and let \(\varepsilon\in\{Y,B\}\).  On a fixed labelled radial triangulation
of \(P_0^\varepsilon\), let
\(T_t^\varepsilon:P_0^\varepsilon\to P_t^\varepsilon\) be the
piecewise-affine material map and put
\(\mathcal H_\varepsilon=H_0^1(P_0^\varepsilon)\).

The compatible boundary space is
\[
\mathcal X_\varepsilon=\operatorname{Tr}H^1(P_0^\varepsilon)
\]
with its quotient norm; \(\mathcal X_\varepsilon^*\) denotes its Hilbert
dual.  Fix a bounded trace right inverse
\(L_\varepsilon:\mathcal X_\varepsilon\to H^1(P_0^\varepsilon)\).
Separately put
\[
\mathcal S_\varepsilon=\prod_{j=1}^N H^{1/2}(0,1)
\]
for scalar open-side conormal traces in the fixed side parameters.

Let \(a_t^\varepsilon,m_t^\varepsilon\) be the pulled-back stiffness and mass
forms on \(\mathcal H_\varepsilon\).  Denote by
\(\widetilde A_t^\varepsilon,\widetilde M_t^\varepsilon:
H^1(P_0^\varepsilon)\to\mathcal H_\varepsilon^*\) the same forms with the
trial slot extended to \(H^1\).  Let
\((\lambda_t^\varepsilon,u_t^\varepsilon)\) be the positive
\(m_t^\varepsilon\)-normalized first eigenpair.  With
\[
\Pi_t^\varepsilon F
=F-F(u_t^\varepsilon)m_t^\varepsilon(u_t^\varepsilon,\cdot),
\]
let \(S_t^\varepsilon\) be the inverse of
\(A_t^\varepsilon-\lambda_t^\varepsilon M_t^\varepsilon\) on the
\(m_t^\varepsilon\)-orthogonal complement, preceded by
\(\Pi_t^\varepsilon\).

Define the weak material conormal by
\[
\langle\Gamma_t^\varepsilon,f\rangle
=a_t^\varepsilon(u_t^\varepsilon,L_\varepsilon f)
-\lambda_t^\varepsilon
 m_t^\varepsilon(u_t^\varepsilon,L_\varepsilon f).
\]
Define \(v_t^\varepsilon(f)\) and the pole-free reduced-DtN block by
\[
v_t^\varepsilon(f)=L_\varepsilon f-
S_t^\varepsilon\Pi_t^\varepsilon
(\widetilde A_t^\varepsilon-
\lambda_t^\varepsilon\widetilde M_t^\varepsilon)L_\varepsilon f,
\]
\[
\langle\Lambda_t^{\varepsilon,\mathrm{red}}f,g\rangle
=a_t^\varepsilon(v_t^\varepsilon(f),L_\varepsilon g)
-\lambda_t^\varepsilon
 m_t^\varepsilon(v_t^\varepsilon(f),L_\varepsilon g).
\]

Now fix one vertex \(i\), one incident side
\(\sigma\in\{-,+\}\), and its reference arclength coordinate \(r_0\).
Let \(\ell_{i,\sigma}^\varepsilon(t)\) be the physical length of that
incident side and set
\[
\rho_{i,\sigma}^\varepsilon(t)
=\frac{\ell_{i,\sigma}^\varepsilon(t)}
       {\ell_{i,\sigma}^\varepsilon(0)}.
\]
The restrictions of \(T_t^\varepsilon\) give \(r_t=\rho r_0\).  Let
\(\omega_i(t)\in(0,\pi)\) be the common interior angle of the \(Y/B\)
families and \(\beta_i(t)=\pi/\omega_i(t)>1\).  In physical sector
coordinates,
\[
u_t^\varepsilon(r,\eta)
=c_i^\varepsilon(t)r^{\beta_i(t)}\sin(\pi\eta)
+o(r^{\beta_i(t)}),
\qquad
e_i^\varepsilon(t)=\beta_i(t)c_i^\varepsilon(t).
\]

There are two distinct material conormal conventions.  The scalar pullback
\[
\widehat g_{t,j}^\varepsilon
=(\partial_{\nu_t}u_t^\varepsilon)\circ
 T_t^\varepsilon\big|_{\text{side }j}
\]
is an element of \(\mathcal S_\varepsilon\).  Its leading unoriented
coefficient at the incidence \((i,\sigma)\) is
\[
\widehat e_{i,\sigma}^\varepsilon(t)
=e_i^\varepsilon(t)
 \bigl(\rho_{i,\sigma}^\varepsilon(t)\bigr)^{\beta_i(t)-1}.
\]
The weak flux-density pullback representing \(\Gamma_t^\varepsilon\) includes
the boundary Jacobian and has leading coefficient
\[
\check e_{i,\sigma}^\varepsilon(t)
=\rho_{i,\sigma}^\varepsilon(t)
 \widehat e_{i,\sigma}^\varepsilon(t)
=e_i^\varepsilon(t)
 \bigl(\rho_{i,\sigma}^\varepsilon(t)\bigr)^{\beta_i(t)}.
\]

Define
\[
A_i^{\mathrm c}=\frac{c_i^Y+c_i^B}{2},\qquad
A_i^{\mathrm j}=c_i^Y-c_i^B,
\]
and, for each \(\sigma\in\{-,+\}\),
\[
E_{i,\sigma}^{\mathrm c}
=\frac{\widehat e_{i,\sigma}^Y+
       \widehat e_{i,\sigma}^B}{2},\qquad
E_{i,\sigma}^{\mathrm j}
=\widehat e_{i,\sigma}^Y-\widehat e_{i,\sigma}^B.
\]
These formulas define the ordered coefficient space
\[
\mathcal C_N^{\mathrm{mat}}
=\mathbb R_\beta^N\times\mathbb R_A^{2N}\times\mathbb R_E^{4N}.
\]

Then:

1. the two pulled-back forms, their extended trial-slot operators, the first
   eigenpairs, projections, and reduced resolvents are \(C^3\) in the
   displayed scalar, vector, form, and bounded-operator topologies;
2. \(t\mapsto\Gamma_t^\varepsilon\) is \(C^3\) into
   \(\mathcal X_\varepsilon^*\), and
   \(t\mapsto\Lambda_t^{\varepsilon,\mathrm{red}}\) is \(C^3\) into
   \(\mathcal B(\mathcal X_\varepsilon,\mathcal X_\varepsilon^*)\);
3. \(t\mapsto\widehat g_t^\varepsilon\) is \(C^3\) into
   \(\mathcal S_\varepsilon\), and the displayed map into
   \(\mathcal C_N^{\mathrm{mat}}\) is \(C^3\); for a fixed material cutoff
   \(\chi\), subtracting the oriented profile
   \[
   \pm\widehat e_{i,\sigma}^\varepsilon(t)
       \chi(r_0)r_0^{\beta_i(t)-1}
   \]
   leaves a \(C^3\) map into edgewise \(H^{1/2}\); and
4. the weak flux density is exactly the scalar pullback multiplied by the
   side Jacobian \(\rho_{i,\sigma}^\varepsilon(t)\).  All derivatives through
   order three agree with the common material weak formulation; endpoint
   profile derivatives are the \(H^{1/2}\)-valued functions generated by
   \(r_0^{\beta_i(t)-1}(\log r_0)^j\), \(0\le j\le3\).

The assertion is pointwise on each fixed active completed ray.  It gives no
constant uniform in a collapsing side ratio and asserts neither the QRCI atom
identity nor its natural-energy estimate.  Any later Eulerian endpoint
distribution is defined and owned by JC_SP_LEDGER as the pushforward of the
material identities above.

## Dependencies

- Definitions supplies \(\alpha_t,Y_t,B_t\), the completed scalar, the
  finite-bridge image, and the closed active ray.
- Convexity and fixed-ray compactness give nondegenerate material triangles,
  positive side ratios, and \(\inf_{i,t}(\beta_i(t)-1)>0\).

## Proof Strategy
Status: done
- Plan: Kind: mechanism — for every fixed \(K'<\infty\), every
  \(N\ge N_{K'}\), every fixed finite-bridge ray (Q8), and each
  \(\varepsilon\in\{Y,B\}\), discharge: (O1) construct \(C^3\)
  piecewise-affine material maps with positive ray-dependent Jacobian margin;
  (O2) prove \(C^3\) stiffness/mass forms and their extended trial-slot
  operators; (O3) use the normalized eigenpair implicit function theorem and
  an augmented inverse to obtain the \(C^3\) eigenpair and reduced resolvent;
  (O4) obtain weak conormal and reduced-DtN regularity by typed composition;
  (O5) rerun the form IFT under a second sector-compatible fixed-interface
  material map and extract the leading coefficient by a fixed-radius
  Fourier--Bessel projection; (O6) factor every Bessel ratio and sum its first
  three parameter derivatives exponentially in edgewise \(H^{1/2}\); and (O7)
  change variables on each side to prove the exact
  \(\rho^{\beta-1}/\rho^\beta\) scalar/flux relation and the \(4N\)
  common/jump coefficient statement.  Every positive constant in O1--O7 may
  depend on the already fixed ray; no \(N\)-uniform estimate is produced.
- Key obstacle: promote \(C^3(H_0^1)\) eigenpair dependence to \(C^3\)
  leading sector amplitudes and edgewise \(H^{1/2}\) remainders without
  losing the material length factors.
- Needed dependencies: Definitions supplies the closed active material ray
  and its two polygon families; (H2) supplies convex genuine corners and
  (Q8) fixes the ray before compactness margins are taken.  No unproved
  child, citation, certificate, or later uniform estimate is used.
- Failure trigger: interface mismatch if the fixed-radius sector extraction
  cannot be expressed in the stated material spaces or if side change of
  variables gives a coefficient other than the displayed powers of \(\rho\).

## Experiments and Edge Cases
Status: done

### Check 1: compatible trace domain
- Model: independent constants \(1\) and \(0\) on two sides meeting at one vertex.
- Method: experiments/check_jc_sp_matreg_trace.py evaluates the exact truncated cross-edge \(H^{1/2}\) integral.
- Result: the cross-edge seminorm diverges logarithmically, while each separate edge seminorm is zero; the quotient trace space excludes the datum.
- Interpretation: supports the compatible global trace domain and refutes use of the full product as a lifting domain.

### Check 2: scalar versus flux coefficient
- Model: one incident side with \(r_t=\rho(t)r_0\) and physical trace \(e(t)r_t^{\beta(t)-1}\).
- Method: exact symbolic substitution and boundary-Jacobian multiplication in experiments/check_jc_sp_matreg_trace.py.
- Result: scalar pullback gives exactly
  \(e\rho^{\beta-1}r_0^{\beta-1}\), and multiplying by the side Jacobian
  gives exactly \(e\rho^\beta r_0^{\beta-1}\).
- Interpretation: supports the corrected distinction and its incidence-level endpoint coefficients.

### Check 3: spectral and endpoint thresholds
- Model: the exact rotating simple eigenpair and the profiles \(r^\gamma(\log r)^j\), \(\gamma>0\), \(0\le j\le3\).
- Method: experiments/check_jc_sp_reg_toy.py and experiments/check_jc_sp_matreg_trace.py.
- Result: the reduced block has only positive-gap denominators, and the dyadic \(H^{1/2}\) majorant has ratio \(2^{-2\gamma}<1\).
- Interpretation: supports pointwise spectral and endpoint regularity but not the actual sector coefficient extraction.

## Counterexample Search
Status: done

Agent: matflux_counterexample_scout.

The fresh independent search tested unequal adjacent side ratios,
scalar/flux confusion, incompatible edge traces, angle approach to \(\pi\),
vanishing triangle Jacobians, eigenvalue collision, zero leading corner
amplitude, and invertibility of the \(Y/B\) average-difference coordinates.
It returned PASS.  A fixed closed active ray has positive ray-dependent
margins for side ratios, triangle Jacobians, \(\beta_i-1\), and the first
spectral gap.  The corrected \(\rho^{\beta-1}\) and \(\rho^\beta\) factors and
the \(4N\) incidence block exclude the exact A9 failure.  No uniform margin as
a side ratio collapses was inferred.

## Proof
Status: done

Fix \(K'<\infty\) as in (Q9), \(N\ge N_{K'}\) as in (Q10), and one completed
coordinate \(q=(d,w)\) as in (Q8).  All constants below are allowed to depend
on this fixed \(N,q,K'\) and, after they are selected, on the finite branch,
vertex, and incidence labels.  They are never used in JC_SP_EST.  We prove the assertions
for one \(\varepsilon\in\{Y,B\}\) fixed as in (Q11); applying the same argument to both families
and taking their product gives the two-family statement.

Step 1: fixed material geometry and forms.

By the definition of the finite-bridge image, the whole segment
\(\{tq:0\le t\le1\}\) remains in one labelled positive-fan material chart.
We first make the parameter regularity of that chart explicit.  On a positive
fan,
\[
h_\alpha
=\left(\frac{\pi}{\sum_j\tan(\alpha_j/2)}\right)^{1/2}.
\tag{0a}
\]
For a regular-quotient vector \(w\), the retained canonical transport has the
finite-rank formula
\[
\begin{aligned}
L_\alpha w
&=\sum_i\left(\tan\frac{\alpha_{i-1}}2+
                    \tan\frac{\alpha_i}2\right)w_i,\\
s_\alpha(w)&=\frac{L_\alpha w}{L_\alpha\mathbf1},\\
J_\alpha w
&=w-s_\alpha(w)\mathbf1-\tau_\alpha(\vartheta_\alpha(w)).
\end{aligned}
\tag{0b}
\]
Here \(\tau_\alpha(b)_i=b\cdot e_r(\theta_i)\), and
\(\vartheta_\alpha(w)\in\mathbb R^2\) is the \(L^2\)-projection coefficient
of the sine interpolant of \(w-s_\alpha(w)\mathbf1\) onto
\(\{\cos\theta,\sin\theta\}\).  Every entry in (0b) is a finite integral of
sines and cosines divided only by positive \(\sin\alpha_i\) and by
\(L_\alpha\mathbf1>0\).  Hence \(\alpha\mapsto J_\alpha\) is real analytic
on the positive-fan chart; its inverse is analytic wherever it is the
retained quotient isomorphism.

The exact disk corrector is the solution of the finite-dimensional Riesz
system
\[
\mathcal R_\alpha z_\alpha^D=-\frac12p_\alpha,
\tag{0c}
\]
where \(\mathcal R_\alpha\) is the positive quotient Gram matrix of
\(\mathcal G_\alpha^{\mathrm{JP}}\) and \(p_\alpha\) is the disk forcing
covector.  Their entries are the same analytic endpoint integrals as in
(0b).  Matrix inversion in (0c) therefore makes
\(\alpha\mapsto z_\alpha^D\) analytic, and
\(c_\alpha=J_\alpha^{-1}z_\alpha^D\) is analytic as well.  Equations
(0a)--(0c), together with \(\alpha_t=\alpha_*+td\), prove that both support
vectors \(Y_t\) and \(B_t\) are \(C^3\).  This is an explicit derivation, not
an inference from activity.

The intersection formula for two consecutive support lines now shows that
every labelled vertex \(p_i^\varepsilon(t)\) is \(C^3\).  Its denominator is
the sine of the intervening positive exterior angle.  Positivity follows from
convex genuine polygonality (H2), and compactness of the already fixed
interval gives a ray-dependent positive lower bound.

On the reference triangle
\[
\Delta_i^\varepsilon(0)
=\operatorname{conv}\{o^\varepsilon,
  p_i^\varepsilon(0),p_{i+1}^\varepsilon(0)\},
\]
write \(F_{i,t}^\varepsilon\) for the linear part of
\(T_t^\varepsilon\).  Its columns are the two moving radial vertex vectors
expressed in the reference basis.  Hence \(F_{i,t}^\varepsilon\) is \(C^3\).
Activity and the fixed orientation give
\(\det F_{i,t}^\varepsilon>0\).  Since there are finitely many triangles and
\(0\le t\le1\), there is a number
\[
j_*=j_*(N,q,\varepsilon)>0
\quad\text{such that}\quad
\det F_{i,t}^\varepsilon\ge j_*
\tag{1}
\]
for every \(i,t\).  Thus the matrices, their inverses, and their derivatives
through order three are bounded on this fixed ray.  The same argument on each
labelled side shows that every
\(\rho_{i,\sigma}^\varepsilon(t)\) is \(C^3\) and is bounded above and below
by positive ray-dependent constants.  This proves O1.

For \(z,\phi\in H^1(P_0^\varepsilon)\), change variables triangle by triangle:
\[
\begin{aligned}
a_t^\varepsilon(z,\phi)
&=\sum_i\int_{\Delta_i^\varepsilon(0)}
 \det F_{i,t}^\varepsilon\,
 (F_{i,t}^\varepsilon)^{-1}
 (F_{i,t}^\varepsilon)^{-T}\nabla z\cdot\nabla\phi,\\
m_t^\varepsilon(z,\phi)
&=\sum_i\int_{\Delta_i^\varepsilon(0)}
 \det F_{i,t}^\varepsilon\,z\phi .
\end{aligned}
\tag{2}
\]
The coefficient matrices in (2) are piecewise constant in space and \(C^3\)
in \(t\) in \(L^\infty\).  Differentiating (2) therefore proves \(C^3\)
dependence in the form norm on \(H^1\times H^1\), and in particular in the
operator norms
\[
\mathcal B(\mathcal H_\varepsilon,\mathcal H_\varepsilon^*)
\quad\text{and}\quad
\mathcal B(H^1(P_0^\varepsilon),\mathcal H_\varepsilon^*).
\tag{3}
\]
The latter operators are exactly
\(\widetilde A_t^\varepsilon,\widetilde M_t^\varepsilon\).  Equation (1)
also gives uniform coercivity of \(a_t^\varepsilon\) on the fixed ray.  This
proves O2.

The trace map
\[
\operatorname{Tr}:H^1(P_0^\varepsilon)\longrightarrow
\mathcal X_\varepsilon
\]
has kernel \(\mathcal H_\varepsilon\).  This kernel is closed.  Its orthogonal
complement in the Hilbert space \(H^1(P_0^\varepsilon)\) maps bijectively onto
the quotient range \(\mathcal X_\varepsilon\); the inverse is bounded by the
definition of the quotient norm.  It supplies the fixed right inverse
\(L_\varepsilon\).  This also proves directly why no right inverse from the
larger independent-edge product is used.

Step 2: eigenpair and reduced resolvent.

Suppress \(\varepsilon\) temporarily.  Consider
\[
\mathcal F(t,u,\lambda)
=\left(A_tu-\lambda M_tu,\,
       \frac12(m_t(u,u)-1)\right)
\]
from
\([0,1]\times\mathcal H_\varepsilon\times\mathbb R\) to
\(\mathcal H_\varepsilon^*\times\mathbb R\).
By (2)--(3), \(\mathcal F\) is \(C^3\).  At the normalized first eigenpair its
derivative in \((u,\lambda)\) is
\[
(h,\mu)\longmapsto
\left((A_t-\lambda_tM_t)h-\mu M_tu_t,\,
      m_t(u_t,h)\right).
\tag{4}
\]
The first Dirichlet eigenvalue of the connected convex polygon is simple.
Indeed, the absolute value of a first eigenfunction has the same Rayleigh
quotient, and the strong maximum principle makes every nonnegative first
eigenfunction positive.  If \(u,v>0\) are two normalized first
eigenfunctions, test the equation for \(u\) with
\(v^2/(u+\epsilon)\), using the standard \(H_0^1\) truncation near
\(\{u=0\}\), and let \(\epsilon\downarrow0\).  Combining the resulting
identity with the equation tested by \(v\) gives Picone's exact identity
\[
\int_{P_t^\varepsilon}
\left|\nabla v-\frac vu\nabla u\right|^2=0.
\]
Thus \(\nabla(v/u)=0\) almost everywhere, so connectedness makes \(v/u\)
constant.  Hence the first eigenspace is one-dimensional.
Thus \(A_t-\lambda_tM_t\) is invertible on
\[
V_t=\{h\in\mathcal H_\varepsilon:m_t(u_t,h)=0\}.
\]
Decomposing \(h\) into its \(u_t\) and \(V_t\) components shows directly that
(4) is an isomorphism.  The Banach implicit-function theorem yields a local
\(C^3\) normalized eigenpair.  Positivity fixes its sign, so the local
branches agree on overlaps and give a \(C^3\) map on all of \([0,1]\).

For the resolvent, introduce the augmented operator
\[
\mathbb B_t(h,\eta)
=\left((A_t-\lambda_tM_t)h+\eta M_tu_t,\,
       m_t(u_t,h)\right).
\tag{5}
\]
The same decomposition proves that (5) is an isomorphism
\(\mathcal H_\varepsilon\times\mathbb R
\to\mathcal H_\varepsilon^*\times\mathbb R\).  Its coefficients are \(C^3\);
the identity
\[
\frac d{dt}\mathbb B_t^{-1}
=-\mathbb B_t^{-1}\mathbb B_t'\mathbb B_t^{-1}
\]
and two further differentiations show that
\(t\mapsto\mathbb B_t^{-1}\) is \(C^3\) in operator norm.  If
\(\mathbb B_t(h,\eta)=(F,0)\), evaluation of the first component on \(u_t\)
gives \(\eta=F(u_t)\), and hence
\[
(A_t-\lambda_tM_t)h
=F-F(u_t)m_t(u_t,\cdot)=\Pi_tF,\qquad h\in V_t.
\]
Consequently \(h=S_tF\).  The upper-left block of
\(\mathbb B_t^{-1}\) is therefore precisely \(S_t\), proving its asserted
\(C^3\) operator dependence.  This proves O3.

Step 3: weak conormal and reduced DtN.

If \(L_\varepsilon f\) is replaced by another lift of \(f\), their difference
lies in \(\mathcal H_\varepsilon\), and the eigenvalue equation makes the
difference in the definition of \(\Gamma_t^\varepsilon\) zero.  Thus
\(\Gamma_t^\varepsilon\) is well defined.  Equations (2)--(5), together with
the fixed bounded map \(L_\varepsilon\), show by composition that
\[
t\longmapsto\Gamma_t^\varepsilon
\in\mathcal X_\varepsilon^*
\]
is \(C^3\).  The same typed composition gives
\[
t\longmapsto v_t^\varepsilon
\in\mathcal B(\mathcal X_\varepsilon,H^1(P_0^\varepsilon))
\]
and then
\[
t\longmapsto\Lambda_t^{\varepsilon,\mathrm{red}}
\in\mathcal B(\mathcal X_\varepsilon,\mathcal X_\varepsilon^*)
\]
as \(C^3\) maps.  Notice that the extended operators in (3), rather than
their \(H_0^1\)-restrictions, act on \(L_\varepsilon f\).  This proves O4 and
removes the typing defect recorded in A8.

Step 4: extraction of the physical corner coefficient.

Fix a labelled vertex \(i\) as in (Q12).  Since (Q8) fixed a closed active ray, the two
incident sides have a positive minimum length over \(t\) and
\(\varepsilon\).  Choose \(R>0\), depending on this ray, such that the
physical sector
\[
0<r<2R,\qquad 0<\eta<1
\tag{6}
\]
about \(p_i^\varepsilon(t)\) meets no nonincident side.  The angle
\(\omega_i(t)=\pi-\alpha_i(t)\) and
\(\beta_i(t)=\pi/\omega_i(t)\) are \(C^3\).  Convexity in (H2) and compactness
give
\[
\beta_i(t)\ge1+\delta
\tag{7}
\]
for some \(\delta=\delta(N,q)>0\).

On (6), the physical eigenfunction solves
\[
-\Delta u_t^\varepsilon=\lambda_t^\varepsilon u_t^\varepsilon,
\qquad
u_t^\varepsilon=0\quad\text{at }\eta=0,1.
\tag{8}
\]
We do not compose the first material eigenfunction with a moving map.  Instead
construct a second materialization
\[
\widehat T_t^\varepsilon:P_0^\varepsilon\longrightarrow P_t^\varepsilon
\tag{8a}
\]
with fixed reference interfaces as follows.  Choose the vertex sectors
\(r<3R\) disjoint.  In the sector at vertex \(i\), set
\[
\widehat T_t^\varepsilon
\bigl(p_i^\varepsilon(0)+
 r\,e_r(\theta_i^-(0)+\omega_i(0)\eta)\bigr)
=p_i^\varepsilon(t)+
 r\,e_r(\theta_i^-(t)+\omega_i(t)\eta)
\quad (r<2R).
\tag{8b}
\]
Thus physical radius is unchanged near the vertex.  We now extend these exact
sector maps without any interpolation between derivative matrices and without
an \(N\)-uniform closeness assumption.

Because the ray is fixed and all its sides are genuine, choose
\(\ell>0\), depending on this ray, smaller than one quarter of every side
length of both polygon families.  On each of the two rays incident at vertex
\(i\), mark the point at physical distance \(\ell\) from the vertex and join
the two marked points by a chord.  The resulting closed corner triangles are
pairwise disjoint.  Removing their interiors leaves a convex core
\(C_t^\varepsilon\): it is the original convex polygon intersected with the
half-planes on the core side of the cutting chords.

In sector coordinates the cutting chord at vertex \(i\) has a positive radial
graph
\[
 r=L_{i,t}(\eta),\qquad 0\le\eta\le1.
\tag{8d}
\]
It is an explicit quotient of sines obtained by intersecting the ray
\(e_r(\theta_i^-(t)+\omega_i(t)\eta)\) with that chord.  Hence
\(L_{i,t}\) is spatially smooth and \(C^3\) in \(t\).  Fixed-ray compactness
gives a positive lower bound for the finitely many functions \(L_{i,t}\).
Shrink \(R\), if necessary, so that
\[
 4R<\min_{i,t,\varepsilon,\eta}L_{i,t}^\varepsilon(\eta).
\tag{8e}
\]

On the reference corner triangle define
\[
 \widehat T_t^\varepsilon
 \bigl(p_i^\varepsilon(0)+r e_r(\theta_i^-(0)+\omega_i(0)\eta)\bigr)
 =p_i^\varepsilon(t)+
arphi_{i,t}(r,\eta)
  e_r(\theta_i^-(t)+\omega_i(t)\eta),
\tag{8f}
\]
where
\[
 \varphi_{i,t}(r,\eta)=
 \begin{cases}
 r,&0\le r\le2R,\\[2mm]
 2R+\displaystyle
 \frac{L_{i,t}(\eta)-2R}{L_{i,0}(\eta)-2R}(r-2R),
 &2R\le r\le L_{i,0}(\eta).
 \end{cases}
\tag{8g}
\]
All denominators are positive by (8e), and
\(\partial_r\varphi_{i,t}>0\).  In the \((r,\eta)\) coordinates the
Jacobian determinant of (8f), relative to the reference sector Jacobian, is
\[
 \frac{\varphi_{i,t}\,\partial_r\varphi_{i,t}\,\omega_i(t)}
      {r\,\omega_i(0)}>0.
\tag{8h}
\]
The apparent quotient at \(r=0\) has limit one.  Thus (8f) is a bi-Lipschitz
homeomorphism from the reference corner triangle onto the moving one.  It is
exactly (8b) for \(r\le2R\), maps the outer chord to the outer chord with the
same \(\eta\), and is \(C^3\) in \(t\) into \(W^{1,\infty}\) on the two fixed
pieces \(r<2R\) and \(r>2R\).  No convex combination of orientation-
preserving matrices occurs.

It remains to map the convex cores.  On each cutting chord use the boundary
map already specified by (8f).  On each remaining middle segment of an
original side, use the orientation-preserving affine arclength map between
the two chord endpoints.  This defines an orientation-preserving piecewise
\(C^3\), bi-Lipschitz boundary homeomorphism
\[
 b_t^\varepsilon:\partial C_0^\varepsilon
      \longrightarrow\partial C_t^\varepsilon.
\tag{8i}
\]
Choose, for example, the arithmetic mean \(o_t^\varepsilon\) of the vertices
of the cut core; it lies in its interior and is \(C^3\).  Every noncentral
point of a convex core has the unique representation
\[
 x=o_0^\varepsilon+s\bigl(b_0^\varepsilon(\xi)-o_0^\varepsilon\bigr),
 \qquad 0<s\le1,quad \xi\in\partial C_0^\varepsilon.
\]
Define the conical extension
\[
 \widehat T_t^\varepsilon(x)
 =o_t^\varepsilon+s\bigl(b_t^\varepsilon(\xi)-o_t^\varepsilon\bigr),
 \qquad
 \widehat T_t^\varepsilon(o_0^\varepsilon)=o_t^\varepsilon.
\tag{8j}
\]
Convexity makes each ray from \(o_t^\varepsilon\) meet the target boundary
once, so (8j) is bijective.  On the finitely many conical pieces over the
chords and side segments, the boundary radius, its reciprocal, and the
angular derivative of (8i) have positive ray-dependent bounds.  The polar
derivative of (8j) and that of its inverse are therefore bounded.  Hence
(8j) is bi-Lipschitz and \(C^3\) in \(t\) into piecewise
\(W^{1,\infty}\).  It agrees with (8f) on every cutting chord.

Combining (8f) and (8j) gives the global map (8a).  Its reference partition
consists of the fixed inner/outer corner pieces and the fixed conical core
pieces.  The map and its inverse have positive, possibly ray-dependent,
Lipschitz and Jacobian margins.  This construction works after fixing any
eligible ray; it does not choose \(N_{K'}\) after \(q\) and uses no constant
uniform in a collapsing side ratio.

Pull the Dirichlet eigenproblem back by \(\widehat T_t^\varepsilon\).
On the second fixed partition the coefficients are
\(\det D\widehat T\,D\widehat T^{-1}D\widehat T^{-T}\) and
\(\det D\widehat T\).  The preceding \(C^3(W^{1,\infty})\) statement and
(8h) therefore give \(C^3\) form operators on
\(H_0^1(P_0^\varepsilon)\).
Repeating the normalized implicit-function argument (4) produces
\[
\widehat u_t^\varepsilon
:=u_t^\varepsilon\circ\widehat T_t^\varepsilon
\in C^3([0,1];H_0^1(P_0^\varepsilon)).
\tag{8c}
\]
This is a new application of the form argument; no differentiability of
composition on arbitrary \(H^1\) is asserted.  On \(r<2R\), (8b) identifies
\(\widehat u_t^\varepsilon\) with
\[
U_t(r,\eta)
=u_t^\varepsilon\!\left(
p_i^\varepsilon(t)+
r\,e_r(\theta_i^-(t)+\omega_i(t)\eta)\right).
\]
It satisfies on the fixed annulus a uniformly elliptic equation whose
coefficients are smooth in space and \(C^3\) in \(t\).  The first time
difference quotient solves the same principal equation with right side made
of \(U_t\), one coefficient difference quotient, and \(\lambda_t\);
successive time quotients have the same form with already controlled lower
time derivatives.  Interior elliptic estimates away from the vertex, and odd
reflection across either straight Dirichlet side, therefore give
\[
\|\partial_t^jU_t\|_{H^{m+2}(A')}
\le C_{m,j}\left(
\|\partial_t^jU_t\|_{H^1(A)}
+\sum_{\ell<j}\|\partial_t^\ell U_t\|_{H^{m+1}(A)}
\right)
\]
for \(0\le j\le3\), every smaller annulus \(A'\Subset A\), and every finite
\(m\).  Induction first in \(j\) and then in \(m\) shows that
\[
t\longmapsto
G_{i,t}^\varepsilon(\eta)
:=u_t^\varepsilon(R,\eta)
\]
is \(C^3\) into \(H^m(0,1)\) for every fixed finite \(m\).  The induction
starts from (8c); at each step the
differentiated equation has already controlled lower material derivatives.
All constants here may depend on \(R\) and the fixed ray.

Separation of variables in (8) gives, for \(0<r<R\),
\[
u_t^\varepsilon(r,\eta)
=\sum_{k\ge1}b_{i,k}^\varepsilon(t)
 J_{k\beta_i(t)}(\sqrt{\lambda_t^\varepsilon}\,r)
 \sin(k\pi\eta).
\tag{9}
\]
Choose \(R\) smaller if necessary.  Since
\(\beta_i(t)\) and \(\lambda_t^\varepsilon\) range over compact positive
sets, the power series for \(J_\nu(z)\) makes
\[
J_{\beta_i(t)}(\sqrt{\lambda_t^\varepsilon}R)\ne0
\tag{10}
\]
uniformly on the fixed ray.  Orthogonality in \(\eta\) gives the exact
coefficient
\[
b_{i,1}^\varepsilon(t)
=\frac{2\int_0^1G_{i,t}^\varepsilon(\eta)\sin(\pi\eta)\,d\eta}
       {J_{\beta_i(t)}
        (\sqrt{\lambda_t^\varepsilon}R)}.
\tag{11}
\]
The order and argument dependence of the Bessel power series is \(C^\infty\)
on these compact sets.  Equations (10)--(11) therefore show that
\(b_{i,1}^\varepsilon\) is \(C^3\).  Since
\[
J_\beta(\sqrt\lambda r)
=\frac{(\sqrt\lambda/2)^\beta}{\Gamma(\beta+1)}r^\beta
+O(r^{\beta+2}),
\]
the leading physical coefficient is
\[
c_i^\varepsilon(t)
=b_{i,1}^\varepsilon(t)
 \frac{(\sqrt{\lambda_t^\varepsilon}/2)^{\beta_i(t)}}
      {\Gamma(\beta_i(t)+1)}.
\tag{12}
\]
Thus \(c_i^\varepsilon\), and hence
\(e_i^\varepsilon=\beta_i c_i^\varepsilon\), are \(C^3\).
Formula (12) remains valid when \(c_i^\varepsilon=0\); no division by the
leading coefficient occurs.  This proves O5.

Step 5: strong conormal traces and the endpoint profile.

We first record the elementary endpoint lemma used below.  If
\(\gamma\) ranges in a compact subinterval of \((0,\infty)\), \(\chi\) is a
fixed smooth cutoff near \(0\), and \(0\le j\le3\), then
\[
\chi(r)r^\gamma(\log r)^j\in H^{1/2}(0,1)
\tag{13}
\]
and the map \(\gamma\mapsto\chi r^\gamma\) is \(C^3\) with these derivatives.
For the only singular part of the Gagliardo seminorm, put \(y=sr\) in the
region \(0<y<r<1\).  The measure and denominator reduce the integral to
\[
2\int_0^1\int_0^1
r^{2\gamma-1}
\frac{\left((\log r)^j
-s^\gamma(\log r+\log s)^j\right)^2}
     {(1-s)^2}\,ds\,dr.
\tag{14}
\]
Near \(s=1\), the numerator has a factor \(1-s\); near \(s=0\),
\(s^\gamma|\log s|^j\) is integrable.  The \(r\)-integral is finite because
\(\gamma>0\).  The same bounds, uniformly for \(\gamma\ge\delta\), permit
three differentiations under the integrals.  This proves (13).

Differentiate (9) normally on the two sides.  The \(k=1\) term and the first
Bessel asymptotic give the oriented leading trace
\[
\partial_{\nu_t}u_t^\varepsilon
=\pm e_i^\varepsilon(t)r_t^{\beta_i(t)-1}
+R_{i,\sigma}^\varepsilon(t,r_t).
\tag{15}
\]
After the leading term is removed, the next powers are at least
\[
\min\{\beta_i(t)+1,\,2\beta_i(t)-1\}>1.
\tag{16}
\]
We now give the all-mode estimate omitted from the first audit packet.  Put
\[
g_k(t)=2\int_0^1G_{i,t}^\varepsilon(\eta)\sin(k\pi\eta)\,d\eta,
\qquad \nu_k(t)=k\beta_i(t).
\]
Then \(b_{i,k}=g_k/J_{\nu_k}(\sqrt\lambda R)\), and the \(k\)-th physical
normal-trace mode, up to its fixed orientation sign, is
\[
Q_{k,t}(r)
=g_k(t)\frac{\nu_k(t)}r
 \frac{J_{\nu_k(t)}(\sqrt{\lambda(t)}\,r)}
      {J_{\nu_k(t)}(\sqrt{\lambda(t)}\,R)}.
\tag{16a}
\]
For \(\nu\ge1+\delta\), factor the Bessel series as
\[
J_\nu(z)
=\frac{(z/2)^\nu}{\Gamma(\nu+1)}H_\nu(z^2),
\qquad
H_\nu(s)
=\sum_{m\ge0}\frac{(-s/4)^m}{m!(\nu+1)_m}.
\tag{16b}
\]
Shrink \(R\) so that
\(\lambda(t)R^2\le s_0\) for all \(t\), with \(s_0\) small enough that
\[
\frac12\le H_\nu(s)\le\frac32
\quad(0\le s\le s_0,\ \nu\ge1+\delta).
\tag{16c}
\]
Termwise differentiation of the absolutely convergent series in (16b) shows
that its derivatives in \((\nu,s)\) through total order four are bounded on
this set.  (Order four is recorded because three time derivatives followed
by one radial derivative use one additional \(s\)-derivative.)  The quotient
in (16a) is therefore
\[
\left(\frac rR\right)^{\nu_k}
\frac{H_{\nu_k}(\lambda r^2)}
     {H_{\nu_k}(\lambda R^2)}.
\tag{16d}
\]
Since \(\partial_t\nu_k=k\beta_i'\), three differentiations of (16d) give,
for \(0<r\le R/2\) and \(0\le j\le3\),
\[
\left|
\partial_t^j\left[
\frac{\nu_k(t)}r
\frac{J_{\nu_k(t)}(\sqrt{\lambda(t)}r)}
     {J_{\nu_k(t)}(\sqrt{\lambda(t)}R)}
\right]\right|
\le C_j k^{2j+1}r^{-1}
\left(\frac rR\right)^{k(1+\delta)}
\left(1+\left|\log\frac rR\right|^j\right).
\tag{16e}
\]
The same estimate after one \(r\)-derivative has one additional factor
\(Ck/r\).  Direct integration, using \(k(1+\delta)>2\) for \(k\ge2\), yields
\[
\left\|
\partial_t^j\left[
\frac{\nu_k(t)}r
\frac{J_{\nu_k(t)}(\sqrt{\lambda(t)}\,r)}
     {J_{\nu_k(t)}(\sqrt{\lambda(t)}\,R)}
\right]\right\|_{H^1(0,R/2)}
\le C_j k^{M_j}2^{-k(1+\delta)}
\quad(k\ge2)
\tag{16f}
\]
for fixed integers \(M_j\).  The Fourier coefficient sequences
\(\{\partial_t^ag_k(t)\}_{k\ge1}\) are bounded in \(\ell^2\) for
\(0\le a\le3\), because
\(G_{i,t}^\varepsilon\in C^3(L^2(0,1))\).  Leibniz' rule, Cauchy--Schwarz,
and the exponentially summable right side of (16f) show that the
\(k\ge2\) series and its first three time derivatives converge absolutely in
\(H^1(0,R/2)\), hence in \(H^{1/2}\).

For \(k=1\), subtract the leading term in (15).  In (16b),
\(H_\beta(\lambda r^2)-H_\beta(0)=O(r^2)\), with the same bound after three
parameter derivatives.  More precisely, every such derivative of the
residual is a finite sum
\[
r^{\beta+1}(\log r)^j B_j(t,r^2),\qquad0\le j\le3,
\]
where the analytic factors \(B_j\), together with their first radial
derivatives, are uniformly bounded on the fixed ray.  These functions lie in
\(H^1(0,R/2)\) by (7).  Combining this fact with the \(k\ge2\)
sum proves that
\[
t\longmapsto R_{i,\sigma}^\varepsilon(t,\cdot)
\quad\text{is }C^3\text{ into }H^{1/2}
\tag{17}
\]
near every endpoint.  This conclusion is in physical radius.  We next prove
the material-radius version directly from the same series, rather than invoke
continuity of variable dilation on a generic Sobolev family.

Fix an incidence and abbreviate
\(\rho(t)=\rho_{i,\sigma}^\varepsilon(t)\).  On the fixed ray,
\(0<\rho_*\le\rho(t)\le\rho^*\), with all three parameter derivatives
bounded.  Choose \(R_0>0\) so that \(2\rho^*R_0\le R/2\).  After substituting
\(r=\rho(t)r_0\) in (16d), the power factor is
\[
 \left(\frac{\rho(t)r_0}{R}\right)^{\nu_k(t)}.
\tag{17a}
\]
Its first three time derivatives produce only polynomial factors in \(k\),
\(\rho^{(j)}/\rho\), and
\(\log(\rho r_0/R)\).  Repeating the proof of (16e)--(16f), using the
fourth-order bounds following (16c), gives
\[
 \left\|\partial_t^j
 \left[\frac{\nu_k(t)}{\rho(t)r_0}
 \frac{J_{\nu_k(t)}(\sqrt{\lambda(t)}\,\rho(t)r_0)}
      {J_{\nu_k(t)}(\sqrt{\lambda(t)}\,R)}\right]\right\|_{H^1(0,2R_0)}
 \le C_j k^{\widetilde M_j}2^{-k(1+\delta)},
 \quad k\ge2,\quad 0\le j\le3.
\tag{17b}
\]
The constants may depend on the fixed ray and incidence, which is permitted.
Cauchy--Schwarz against the \(C^3(\ell^2)\) sequence \(g_k(t)\) again sums
all \(k\ge2\) modes in \(C^3(H^1(0,2R_0))\).

For \(k=1\), direct substitution in the factored formula (16b) gives
\[
 Q_{1,t}(\rho r_0)
 \mp e_i^\varepsilon(t)\rho(t)^{\beta_i(t)-1}
       r_0^{\beta_i(t)-1}
 =r_0^{\beta_i(t)+1}\widetilde B(t,r_0^2),
\tag{17c}
\]
where \(\widetilde B\) is a bounded jointly \(C^3\) analytic factor after
the displayed power is removed.  Time differentiation produces finite sums
\(r_0^{\beta+1}(\log r_0)^j\widetilde B_j(t,r_0^2)\), \(j\le3\), with
bounded first radial derivatives.  By (7) they belong to \(H^1\).  Equations
(17b)--(17c) prove the specific material statement
\[
 t\longmapsto
 R_{i,\sigma}^\varepsilon(t,\rho(t)\,\cdot)
 \quad\hbox{is }C^3\hbox{ into }H^1(0,2R_0),
\tag{17d}
\]
and hence into \(H^{1/2}\).  This is a series-level proof and does not use a
translation/dilation action on an arbitrary \(H^1\)-valued map.

On the middle portion of each side, odd reflection of
(8) and the same parameter difference-quotient induction give \(C^3\) in
\(H^m\), hence in \(H^{1/2}\).  A fixed partition of unity combines the
endpoint and middle pieces.  The physical scalar conormal, pulled back to
each fixed side, is consequently a \(C^3\) map into
\(\mathcal S_\varepsilon\).

On the incidence \((i,\sigma)\), with \(\sigma\) fixed as in (Q13), the restriction of the material map is
affine and
\[
r_t=\rho_{i,\sigma}^\varepsilon(t)r_0.
\]
Substituting this identity into (15) gives
\[
(\partial_{\nu_t}u_t^\varepsilon)\circ T_t^\varepsilon
=\pm e_i^\varepsilon
 (\rho_{i,\sigma}^\varepsilon)^{\beta_i-1}
 r_0^{\beta_i-1}
+R_{i,\sigma}^\varepsilon(t,\rho r_0).
\tag{18}
\]
Thus the coefficient in (18) is exactly
\(\widehat e_{i,\sigma}^\varepsilon\).  Equations (7), (13), and the direct
material estimate (17d) prove the precise subtraction assertion in item 3 of
the statement.  This proves O6.

Step 6: weak flux density, common/jump coordinates, and derivative agreement.

For a smooth boundary datum \(f\), Green's identity and sidewise change of
variables give
\[
\begin{aligned}
\langle\Gamma_t^\varepsilon,f\rangle
&=\int_{\partial P_t^\varepsilon}
  \partial_{\nu_t}u_t^\varepsilon\,
  (f\circ(T_t^\varepsilon)^{-1})\,ds_t\\
&=\sum_j\int_{\text{side }j\subset\partial P_0^\varepsilon}
 \rho_j^\varepsilon(t)\,
 \widehat g_{t,j}^\varepsilon\,f\,ds_0.
\end{aligned}
\tag{19}
\]
Density extends (19) to all \(f\in\mathcal X_\varepsilon\).  Hence the weak
flux-density pullback is exactly \(\rho_j^\varepsilon\widehat g_{t,j}^\varepsilon\).
Multiplying (18) by this boundary Jacobian changes the leading coefficient
from
\[
e_i^\varepsilon\rho^{\beta_i-1}
\quad\text{to}\quad
e_i^\varepsilon\rho^{\beta_i},
\]
which proves the asserted formulas for
\(\widehat e_{i,\sigma}^\varepsilon\) and
\(\check e_{i,\sigma}^\varepsilon\).  This is the distinction whose absence
caused A9.

The maps
\[
(c_i^Y,c_i^B)\longmapsto(A_i^{\mathrm c},A_i^{\mathrm j})
\quad\text{and}\quad
(\widehat e_{i,\sigma}^Y,\widehat e_{i,\sigma}^B)
\longmapsto(E_{i,\sigma}^{\mathrm c},E_{i,\sigma}^{\mathrm j})
\]
have matrix
\[
\begin{pmatrix}1/2&1/2\\1&-1\end{pmatrix},
\qquad\det=-1.
\]
They are fixed invertible linear maps.  Since \(\beta_i,c_i^\varepsilon\),
and every incidence coefficient are \(C^3\), the displayed map into
\(\mathcal C_N^{\mathrm{mat}}\) is \(C^3\).

Finally, every object above was defined either by the common material weak
formulation, by an inverse whose derivative is uniquely determined by that
formulation, or by the exact sector projection (11).  Operator
differentiation and differentiation of (11), (18), and (19) therefore give
the same derivatives.  In particular,
\[
\partial_t^3 r_0^{\beta_i(t)-1}
=r_0^{\beta_i(t)-1}
\left(\beta_i'''\log r_0
+3\beta_i'\beta_i''(\log r_0)^2
+(\beta_i')^3(\log r_0)^3\right),
\]
and (13) justifies this identity in \(H^{1/2}\).  Thus no unrecorded endpoint
distribution is created in material coordinates; any Eulerian pushforward
belongs to JC_SP_LEDGER.  This proves O7 and all four conclusions.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: A10 | author:agent:matflux_proof_auditor_1 | interface mismatch -- the first proof inferred moving-sector \(C^3(H^1)\) by a false composition principle and supplied no all-mode differentiated \(H^{1/2}\) majorant.
Superseded attempts: A8 and A9 repaired the lifting and material-flux statement interfaces.

## Local Audit
Status: done

Subagent audit: used
Audit verdict: pass
Audit agent: agent:matflux_repair_auditor_3
Audit model: gpt-5.6-sol
Audit reasoning effort: xhigh
Audit packet SHA256: cb4b86b47f8e8df63a386c3fe5177d9980bcd29fd99ba8ec21a1d7ea9a87f07f
Dual audit: passed
Second audit agent: agent:matflux_repair_auditor_4
Second audit model: gpt-5.6-sol
Second audit reasoning effort: xhigh
Second audit packet SHA256: cb4b86b47f8e8df63a386c3fe5177d9980bcd29fd99ba8ec21a1d7ea9a87f07f

- Required depth: D3 audit-ready local regularity proof.
- Statement strength: pointwise \(C^3\) existence on each fixed closed active
  ray only; no side-ratio-uniform constant, atom identity, endpoint
  pushforward, or natural-energy estimate is asserted.
- Hypotheses and quantifiers: (H2) supplies convex genuine polygons, while
  (Q8) fixes one finite-bridge ray.  Compactness is used only after that ray is
  fixed, so every positive geometric or spectral margin may depend on it.
- Check 1: the exact cross-edge integral diverges logarithmically and confirms
  that \(\mathcal X_\varepsilon\), not the full edge product, is the lifting
  domain.
- Check 2: exact substitution gives the scalar coefficient
  \(e\rho^{\beta-1}\) and weak flux-density coefficient \(e\rho^\beta\).
- Check 3: the finite-dimensional reduced block has only positive-gap
  denominators; third exponent derivatives give only
  \(r^{\beta-1}(\log r)^j\), whose dyadic \(H^{1/2}\) majorant converges for
  the fixed-ray margin \(\beta-1>0\).
- Independent counterexample search: matflux_counterexample_scout returned
  PASS after testing both prior failures A8/A9, unequal incidences, zero
  leading amplitude, and all legal closed-ray degenerations.
- Dependency check: Definitions supplies only the active ray and completed
  polygon families.  No fact from JC_SP_LEDGER or JC_SP_EST is used.
- Type check: \(\mathcal X_\varepsilon\) and
  \(\mathcal X_\varepsilon^*\) own weak boundary data;
  \(\mathcal S_\varepsilon\) owns only scalar open-side traces; the two are
  related by the explicit side Jacobian rather than identified.
- Coefficient check: \(\mathcal C_N^{\mathrm{mat}}\) has \(N\) exponents,
  \(2N\) physical-sector average/difference amplitudes, and \(4N\)
  incidence-level scalar endpoint coefficients.  The weak coefficients are
  recovered by multiplying by \(\rho\).
- Failure checklist: PSF-02 is respected by pointwise rather than uniform
  constants; PSF-03 uses the closed active material ray; PSF-04 is deferred to
  the exact ledger; PSF-05 is the principal typed interface here; PSF-07 is
  respected because the promoted checks are exact symbolic or analytic
  identities.
- Citation need: none at claim-audit level.  Stage 5 will give the fixed-domain
  implicit-function and separated-sector derivations directly.
- Audit outcome: passed; the corner/core materialization and direct
  material-radius Bessel summation received two independent fresh passes.
- First proof audit: fail | agent:matflux_proof_auditor_1 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:89feb82ae3b6f7264540a23e7be048c76770a6945344596a5c9280f9ecc642e5.
- Second proof audit: uncertain | agent:matflux_proof_auditor_2 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:89feb82ae3b6f7264540a23e7be048c76770a6945344596a5c9280f9ecc642e5.
- First A10-repair audit: pass | agent:matflux_repair_auditor_3 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:a2522a96e389933c11dfcac76c72f5903f733ce527d33d9bd1068a181639e4cb.
- Second A10-repair audit: uncertain | agent:matflux_repair_auditor_4 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:a2522a96e389933c11dfcac76c72f5903f733ce527d33d9bd1068a181639e4cb.
- First A10-R2 audit: uncertain | agent:matflux_repair_auditor_3 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:1f5ee787b4e45fa97d2f83e1751dab333e41787925980add81cdd6d87311f50a.
- Second A10-R2 audit: uncertain | agent:matflux_repair_auditor_4 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:1f5ee787b4e45fa97d2f83e1751dab333e41787925980add81cdd6d87311f50a.
- First A10-R3 audit: pass | agent:matflux_repair_auditor_3 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:cb4b86b47f8e8df63a386c3fe5177d9980bcd29fd99ba8ec21a1d7ea9a87f07f.
- Second A10-R3 audit: pass | agent:matflux_repair_auditor_4 |
  model:gpt-5.6-sol | effort:xhigh |
  packet-sha256:cb4b86b47f8e8df63a386c3fe5177d9980bcd29fd99ba8ec21a1d7ea9a87f07f.
- Nonblocking audit note: in (8h), \(\varphi/r\) tends to one while the full
  relative Jacobian tends to \(\omega_i(t)/\omega_i(0)>0\).  The cut length
  \(\ell\) is chosen, by fixed-ray compactness, below the side-length,
  nonadjacent-vertex-separation, and core-interiority margins.  The helper
  objects \(\ell,C_t^\varepsilon,L_{i,t}^\varepsilon,
  \varphi_{i,t}^\varepsilon,b_t^\varepsilon,o_t^\varepsilon\) are
  proof-local choices made after \(q,\varepsilon\); the semantic ledger lint
  found no missing statement-level object.
- Audit repair criterion: establish the support path's analytic dependency,
  rerun the eigenpair IFT under a sector-compatible fixed-interface material
  map constructed without an unproved uniform chart estimate, and sum
  explicit differentiated Bessel-ratio bounds in material \(H^{1/2}\).
