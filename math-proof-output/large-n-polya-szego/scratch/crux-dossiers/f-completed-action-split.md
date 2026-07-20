# Crux Dossier

Family ID: F-COMPLETED-ACTION

## Core Obligation

Core bottleneck: prove JC_PL on the full active no-ratio chart

This reduction keeps the exact completed scalar intact and partitions its
domain at the natural energy scale \(a^5\), where \(a=2\pi/N\).

## D2 Derivation

Define the branch energy
\[
E_\alpha(z)
=\mathcal J_4(\alpha)
+\mathcal G^{\mathrm{JP}}_\alpha(z-z_\alpha^D).
\]
Fix a cutoff \(K>\max\{M_0,C_F/c_F\}\). On the branch
\(E_\alpha(z)\le Ka^5\), the retained finite bridge supplies completed-path
activity and a bridge-dependent constant \(K'=K'(K)\) such that the completed
coordinates \(q=(d,w)\) satisfy
\[
\mathcal N_N(d,w)
=a^2\sum_i d_i^2+\mathcal G^{\mathrm{JP}}_{\alpha_*}(w),
\qquad
r_N(d,w)
=\frac{\|d\|_\infty}{a}
+a^{-2}\mathcal G^{\mathrm{JP}}_{\alpha_*}(w)^{1/2}.
\]
Specifically \(\mathcal N_N(q)\le K'a^5\), and hence
\(r_N(q)\le C_{K'}a^{1/2}\). The direct-child estimate
\[
|D^3\mathbf A_N(tq)[q,q,q]|
\le C_{K'}r_N(q)\mathcal N_N(q),\qquad 0\le t\le1,
\tag{JC-SP}
\]
together with the positive base Hessian would imply
\[
\mathbf A_N(q)
=\int_0^1(1-t)D^2\mathbf A_N(tq)[q,q]\,dt
\ge
\left(\mu_0-\frac{C_{K'}}{2}r_N(q)\right)\mathcal N_N(q)
\ge0
\]
for large \(N\). Every moving-fan, corrector, quotient-transport, metric,
ground-state, and base-subtraction term remains inside this scalar.

On the disjoint complementary branch \(E_\alpha(z)>Ka^5\), the minimal
direct coarse child is the restricted implication
\[
E_\alpha(z)>M_0a^5
\Longrightarrow
\mathscr A_\alpha(z)\ge c_FE_\alpha(z)-C_Fa^5.
\tag{JC-CL}
\]
The retained source sometimes states a stronger whole-chart lower bound; the
canonical child JC-CL is only the coarse-restricted antecedent displayed
above. Since \(K>C_F/c_F\), its right side is positive on
\(E_\alpha(z)>Ka^5\). Therefore
\[
\mathrm{JC\_SP}+\mathrm{JC\_CL}
+\text{retained closed bridges}
\Longrightarrow\mathrm{JC\_PL}.
\]

Two exact checks expose the subcruxes. Terminal and annular complement powers
must be combined before differentiation:
\[
A^2\vartheta^{2\beta}K_\beta
+A^2(1-\vartheta^{2\beta})K_\beta=A^2K_\beta,
\]
which cancels artificial \(\beta\log\vartheta\) terms. On the regular
period-three collapsing gap
\[
u=(1/3,-1/6,-1/6),\qquad g=(0,3/2,3/2),
\]
the exact leading coarse ratio is
\[
\frac{2\pi\{S_3(1)-S_3(0)\}}{\mathcal Q_3[u]}
=\frac{10}{13}>\frac12,
\]
with surplus \(7\mathcal Q_3[u]/26\). Nevertheless the support-time Hessian
tends to \(-\infty\) logarithmically at the colliding pair, so pointwise
convexity is not a valid shortcut.

## Reduction Witness

Reduction witness: prove JC_PL on the full active no-ratio chart => prove JC_SP on the super-near branch and JC_CL on the coarse/far branch; axis=locality

The children occupy disjoint exhaustive energy regimes and use distinct
mechanisms. The split is structural only; neither child is claimed proved.

## Falsification

Alternating vertex data have derivative jumps with divergent scalar radial
\(H^{1/2}\) seminorm, killing that analytic shortcut but not the completed
third-jet claim. The exact period-three collision kills pointwise coarse
Hessian positivity but not the support-time-integrated Bregman inequality.

The remaining JC-SP obligation is the uniform full-cell QRCI jet estimate.
The remaining JC-CL obligations are the all-period gap-simplex inequality,
finite-\(N\) ratio-free transfer, and nonregular original-path transfer with a
single completed covector/Hessian budget.

## Verdict

Verdict: split. Promote JC-SP and JC-CL only as unproved direct children,
subject to independent review.
