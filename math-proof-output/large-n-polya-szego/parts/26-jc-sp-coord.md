# JC_SP_COORD: Finite-Dimensional Coordinate Regularity

## Local Summary
- Statement: C3 regularity of the completed metric, corrector, quotient, and fan-defect curves on each fixed material ray
- Dependencies: Definitions
- Current obstruction: none
- Proof status: done
- Next action: none
- Local Context Packet: this statement + Definitions' normal-sine metric, canonical quotient transport, exact disk corrector, fourth fan defect, and one fixed finite-bridge ray; polygonal spectral derivatives and all uniform estimates are excluded.

## Statement

Fix $N$ and one finite-bridge completed ray $q=(d,w)$ from (Q8). Let
\[
\alpha_t=\alpha_*+td,
\qquad C_t=J_{\alpha_t}c_{\alpha_t}=z_{\alpha_t}^D,
\qquad W_t=tJ_{\alpha_t}w,
\qquad 0\le t\le1.
\]
Then the three scalar functions
\[
t\longmapsto
\mathcal G^{\mathrm{JP}}_{\alpha_t}(C_t),
\qquad
t\longmapsto
\mathcal G^{\mathrm{JP}}_{\alpha_t}(W_t),
\qquad
t\longmapsto\mathcal J_4(\alpha_t)
\tag{COORD}
\]
are C3 on $[0,1]$. At an endpoint, C3 means the restriction of a C3
extension to a slightly larger interval. This extension is supplied by the
open canonical quotient chart in (Q8), together with the fixed-ray margins
\[
\min_{i,t}\{\alpha_i(t),\pi-\alpha_i(t)\}>0,
\qquad
\min_t\lambda_{\min}(\bar{\mathcal R}_{\alpha_t})>0,
\tag{COORD-0}
\]
and may depend on the already fixed ray. The angle margin and open chart
permit the extension; the Riesz margin follows from the continuity and
positivity proved below. Here
$\bar{\mathcal R}_\alpha$ is the Riesz matrix of the pulled-back metric on
the fixed regular quotient. In particular, all three ordinary third
derivatives used in JC_SP_SRC exist.

No bound uniform in $N$, the ray, or the smallest fan angle is asserted.
The statement concerns the scalar quadratic forms in (COORD), not C3
differentiability of the raw moving-knot interpolants as H1/2-valued curves.

## Dependencies

- Definitions supplies the positive fan path, the canonical quotient map
  $J_\alpha$, the corrector $z_\alpha^D=J_\alpha c_\alpha$, the normal-sine
  metric, and $\mathcal J_4$.
- The open chart in (Q8), compactness of the fixed ray, and
  $0<\alpha_i(t)<\pi$ supply the angle part of (COORD-0), an open fan
  neighborhood, and a positive separation margin between every normal knot
  and every adjacent midpoint knot. Positivity of the quotient metric and
  its continuity, proved below, then supply the Riesz part of (COORD-0).

## Proof Strategy
Status: done
- Plan: Kind: mechanism -- write the canonical quotient map as a finite matrix of analytic trigonometric cell integrals; pull every normal-sine function to the fixed regular cells; split the disk multiplier into its half-order Gagliardo principal part and lower-order remainder; differentiate the scalar double integrals under the fixed-ray bi-Lipschitz margin; obtain the corrector from a finite positive matrix inverse; and differentiate the explicit polynomial $\mathcal J_4$.
- Key obstacle: the Eulerian derivative of a moving-knot interpolant may jump at a knot, so vector-valued H1/2 differentiation is not an admissible shortcut.
- Needed dependencies: only the explicit finite-dimensional definitions and the fixed-ray positive separation margin.
- Failure trigger: interface mismatch if the pulled scalar kernel has a nonintegrable third parameter derivative; statement likely false if an exact positive-fan path makes one scalar in (COORD) fail to have a third one-sided derivative.

## Experiments and Edge Cases
Status: done

### Check 1: fan polynomial
- Model: $\alpha_t=a\mathbf1+td$ with $\sum_i d_i=0$.
- Method: expand the definition $\mathcal J_4(\alpha)=\sum_i\alpha_i^4-Na^4$.
- Result: the restriction is a polynomial of degree four in $t$.
- Interpretation: supports; the fan curve is C3 with no endpoint issue.

### Check 2: moving-knot warning
- Model: a continuous piecewise-sine interpolant with one moving knot and unequal one-sided spatial derivatives.
- Method: differentiate at fixed Eulerian angle and compare the two traces.
- Result: the Eulerian parameter derivative can jump and need not be H1/2, although the scalar Gagliardo energy remains differentiable after a material change of variables.
- Interpretation: supports the scalar-only formulation and rules out the stronger vector-valued shortcut.

## Counterexample Search
Status: done

The claim excludes collision of normal-angle knots by fixing one positive fan
ray before taking derivatives. The identity, small-angle, unequal-angle, and
moving-knot cases reveal no scalar obstruction. No claim is made uniformly as
the fixed ray approaches a collision.

## Proof
Status: done

<!-- math-proof-ledger: {"object":"\\theta_i","kind":"local-only","depends_on":["Q8"],"reason":"normal-angle coordinates chosen only inside the fixed-ray proof"} -->
<!-- math-proof-ledger: {"object":"\\theta_0","kind":"local-only","depends_on":["Q8"],"reason":"origin convention for the proof-local normal-angle coordinates"} -->
<!-- math-proof-ledger: {"object":"j","kind":"local-only","depends_on":[],"reason":"fixed first positive zero of the disk ground-state Bessel function"} -->
<!-- math-proof-ledger: {"object":"m_i","kind":"local-only","depends_on":["Q8"],"reason":"midpoint knots used only in the scalar-kernel calculation"} -->
<!-- math-proof-ledger: {"object":"\\beta_\\alpha","kind":"local-only","depends_on":["Q8"],"reason":"finite-dimensional translation-projection coefficient in the displayed canonical quotient formula"} -->
<!-- math-proof-ledger: {"object":"\\beta","kind":"local-only","depends_on":["Q8"],"reason":"abbreviated translation-projection coefficient used only in the quotient calculation"} -->

Write the consecutive normal angles as
$\theta_0=0$ and $\theta_i=\sum_{r<i}\alpha_r$. We first record a scalar
kernel form of the disk metric. The retained normal-sine interpolant is
\[
(\mathcal I_\alpha z)(\theta)
=\frac{\sin(\theta_{i+1}-\theta)z_i
+\sin(\theta-\theta_i)z_{i+1}}{\sin\alpha_i},
\qquad \theta_i\le\theta\le\theta_{i+1}.
\tag{16}
\]
If $u=\mathcal I_\alpha z$, then on each open normal cell $u''+u=0$,
while continuity at the knots gives, distributionally,
\[
(\partial_\theta^2+1)u
=\sum_i\rho_i(\alpha,z)\delta_{\theta_i},
\qquad
\rho_i=u'(\theta_i+)-u'(\theta_i-).
\tag{17}
\]
Formula (16) shows directly that every $\rho_i$ is linear in $z$ and real
analytic in $\alpha$ as long as
$0<\alpha_i<\pi$.

Let $j=j_{0,1}$, $d_\circ=\partial_ru_0(1)$, and, for $n\ge2$, put
\[
\omega_n=n+1-k_n,
\qquad
k_n=j\frac{J_{n+1}(j)}{J_n(j)}.
\]
These are exactly the nongeometric eigenvalues of
$\mathcal D_\circ+1$. The Bessel recurrence gives
\[
k_n=\frac{j^2}{2(n+1)-k_{n+1}}.
\tag{18}
\]
Since $j$ is fixed and $0<k_n=O(n^{-1})$, finite differencing (18) gives,
for $0\le r\le3$,
\[
|\Delta^rk_n|\le C_r(1+n)^{-1-r}.
\tag{19}
\]
Define the periodic kernel
\[
\mathscr K(x)=\frac{d_\circ^2}{2\pi}
\sum_{|n|\ge2}
\frac{\omega_{|n|}}{(n^2-1)^2}e^{inx}.
\tag{20}
\]
Its series is absolutely convergent, so $\mathscr K$ is continuous on the
circle. Moreover (19), followed by discrete summation by parts for the
Fourier series of its first three distributional derivatives, shows that
\[
\mathscr K\in C^3_{\mathrm{loc}}(\mathbb T\setminus\{0\}).
\tag{21}
\]
Indeed the third differentiated coefficients are a constant multiple of
$\operatorname{sgn}(n)$ plus a sequence whose first difference is
$O(n^{-2})$. The first term has the standard principal-value cotangent
kernel, which is smooth off the diagonal, and the remainder converges
locally uniformly after one summation by parts. This proves (21) without
claiming that $\mathscr K$ is C3 at the origin.

Taking Fourier coefficients in (17) and using Parseval now gives the exact
finite formula
\[
\mathcal G^{\mathrm{JP}}_\alpha(z,z')
=\sum_{i,j}\rho_i(\alpha,z)\rho_j(\alpha,z')
\mathscr K(\theta_i-\theta_j).
\tag{22}
\]
For $i=j$, the kernel factor is the fixed number $\mathscr K(0)$. For
$i\ne j$, the fixed-ray separation margin and (21) apply. Hence (22) is
C3 in $t$ whenever the nodal vectors are C3 after pullback to a fixed
finite-dimensional space.

We next treat the disk forcing used by the corrector. Before deletion of
the three geometric modes its source is, on the cell
$[\theta_i,\theta_{i+1}]$,
\[
b_\alpha(\theta)
=h_\alpha\sec\!\left(
\min\{\theta-\theta_i,\theta_{i+1}-\theta\}\right)-1,
\qquad
h_\alpha^2=\frac{\pi}{\sum_i\tan(\alpha_i/2)}.
\tag{23}
\]
Thus $h_\alpha$ is analytic. The function $b_\alpha$ is smooth through
each normal knot and has its only derivative jumps at the midpoint knots
$m_i=(\theta_i+\theta_{i+1})/2$. Consequently
\[
(\partial_\theta^2+1)b_\alpha
=g_\alpha(\theta)\,d\theta
+\sum_i\sigma_i(\alpha)\delta_{m_i},
\tag{24}
\]
where on every half-cell $g_\alpha$, its first three material derivatives,
and the coefficients $\sigma_i$ are smooth functions of the fixed material
coordinate and analytic functions of $\alpha$. Deleting geometric modes
changes only the smooth density in (24).

Pair (24) with (17) through the same kernel (20). This expresses
$p_\alpha[z]=2\langle B_\alpha,\mathcal I_\alpha z\rangle_D$ as a finite
sum of
\[
\rho_j(\alpha,z)\mathscr K(m_i-\theta_j)
\quad\text{and}\quad
\rho_j(\alpha,z)
\int_{\mathbb T}\mathscr K(\theta_j-y)g_\alpha(y)\,dy,
\tag{25}
\]
with analytic scalar coefficients suppressed. A midpoint never meets a
normal knot on the enlarged fixed ray, so (21) handles the first type. For
the integral, choose a fixed material neighborhood of $\theta_j$ which
contains no midpoint. After translating its center to zero, parameter
derivatives fall only on the smooth density and the material Jacobian,
while $\mathscr K\in L^1$ is fixed. On the complement the kernel argument
stays away from zero and (21) permits three ordinary derivatives. Dominated
differentiation proves that every coordinate of the pulled-back forcing is
C3.

It remains to make the quotient and corrector levels explicit. Fix a basis
$e_1,\ldots,e_{N-3}$ of the regular quotient and set
\[
\bar g_\alpha(u,v)
=\mathcal G^{\mathrm{JP}}_\alpha(J_\alpha u,J_\alpha v),
\qquad
\bar p_\alpha(u)=p_\alpha[J_\alpha u].
\tag{26}
\]
For completeness, put
\[
L_\alpha v
=\sum_i\left\{\tan\frac{\alpha_{i-1}}2
+\tan\frac{\alpha_i}2\right\}v_i,
\qquad
s_\alpha(v)=\frac{L_\alpha v}{L_\alpha\mathbf1},
\]
let $\beta_\alpha(v)$ be the $L^2$ projection coefficient of
$\mathcal I_\alpha(v-s_\alpha(v)\mathbf1)$ onto
$\{\cos\theta,\sin\theta\}$, and set
\[
J_\alpha v=v-s_\alpha(v)\mathbf1
-\tau_\alpha(\beta_\alpha(v)),
\qquad
\tau_\alpha(b)_i=b\cdot e_r(\theta_i).
\tag{26a}
\]
Every entry in (26a) is a finite analytic trigonometric cell integral.
Thus the matrix of $J_\alpha$ is C3 (in fact analytic) on the enlarged
ray. Equations (22) and (25) imply that
\[
M_{rs}(t)=\bar g_{\alpha_t}(e_r,e_s),
\qquad b_r(t)=\bar p_{\alpha_t}(e_r)
\tag{27}
\]
are C3. The metric is positive definite on the quotient. By compactness
and (COORD-0), $M(t)^{-1}$ is C3 on a slightly larger interval. Hence
\[
c_{\alpha_t}=-\frac12M(t)^{-1}b(t),
\qquad z_{\alpha_t}^D=J_{\alpha_t}c_{\alpha_t}
\tag{28}
\]
are C3 in fixed coordinates, and
\[
\mathcal G^{\mathrm{JP}}_{\alpha_t}(C_t)
=c_{\alpha_t}^{\mathsf T}M(t)c_{\alpha_t},
\qquad
\mathcal G^{\mathrm{JP}}_{\alpha_t}(W_t)
=t^2w^{\mathsf T}M(t)w
\tag{29}
\]
are C3 scalar functions.

Finally,
\[
\mathcal J_4(\alpha_t)
=6a^2t^2\sum_i d_i^2
+4at^3\sum_i d_i^3+t^4\sum_i d_i^4,
\tag{30}
\]
so the third scalar is a polynomial. Equations (29)--(30) prove (COORD),
including the endpoint convention supplied by the enlarged ray.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: differentiating the raw moving-knot interpolant as an H1/2-valued curve

## Local Audit
Status: done

- Independent claim-audit verdict: commit.
- Endpoint correction applied: the extension uses the open Q8 quotient
  chart, both fan-angle margins, and the positive pulled-back Riesz matrix,
  rather than positivity of the lower angle alone.
- Scope check: the proof is fixed-N and fixed-ray; it asserts no uniform
  constants and no vector-valued H1/2 differentiability.
- Both auditors reconstructed (17)--(30), including the off-diagonal
  cotangent-kernel term, moving-cutoff differentiation, and the typed chain
  $J_\alpha\to(M,b)\to c_\alpha\to z_\alpha^D$.
- Nonblocking note: (19) abbreviates the routine repeated finite-difference
  induction from (18); the endpoint sentence is read in the logical order
  stated before the proof, namely continuity and positivity first supply the
  compact Riesz margin and then preserve it on the enlarged interval.

Subagent audit: used
Audit verdict: pass
Audit agent: /root/rl_layer_phase_attack
Audit model: gpt-5.6-sol
Audit reasoning effort: xhigh
Audit packet SHA256: f490360e682bf31c6b6ed76561ce7c1455e5ae77d8fc65dae8ba70114f3a9c2c
Dual audit: passed
Second audit agent: /root/rl_convex_dual_attack
Second audit model: gpt-5.6-sol
Second audit reasoning effort: xhigh
Second audit packet SHA256: f490360e682bf31c6b6ed76561ce7c1455e5ae77d8fc65dae8ba70114f3a9c2c
