# Definitions and Notation

## Conventions

- All polygonal domains are bounded, open, convex subsets of $\mathbb R^2$.
- A polygon has exactly $N$ genuine sides when every side has positive length and no two consecutive sides are collinear.
- Congruence is equality after a Euclidean isometry.
- Dirichlet eigenvalues are taken for the Friedrichs realization of $-\Delta$ on $H_0^1(P)$.
- The area normalization $A=\pi$ may be used inside local arguments, but every final statement must restore arbitrary $A>0$ by scaling.
- Legacy revision-24 TeX labels are source identifiers only; the Markdown blueprint and parts own current workflow status.

## Definitions

- $R_N(A)$ is the regular convex $N$-gon of area $A$.
- $\lambda_1(\Omega)$ is the least Dirichlet eigenvalue of $-\Delta$ on $\Omega$.
- A positive normal fan $\alpha$ records the exterior-angle data of a convex polygon in the fixed-normal support parametrization.
- $\mathsf X_\alpha$ is the affine scale/translation quotient section used by the retained joint-comparison source.
- $\Phi_\alpha(h)=|P_\alpha(h)|\lambda_1(P_\alpha(h))/\pi$ is the scale-invariant polygonal spectral scalar.
- $\mathcal J_4(\alpha)$ is the fourth-order fan defect appearing in the retained endpoint estimate.
- $\mathcal G^{\mathrm{JP}}_\alpha$ is the retained positive normal-sine support metric.
- $z_\alpha^D$ is the exact disk corrector defined by the Riesz completion of the disk forcing.
- $\mathscr A_\alpha(z)$ is the completed pathwise action in the retained JC algebra.
- $a=2\pi/N$ is the regular exterior-angle scale.
- $E_\alpha(z)=\mathcal J_4(\alpha)+\mathcal G^{\mathrm{JP}}_\alpha(z-z_\alpha^D)$ is the branch energy used to split the completed action.
- For completed coordinates $q=(d,w)$ at the regular fan,
  \[
  \mathcal N_N(q)=a^2\sum_i d_i^2+\mathcal G^{\mathrm{JP}}_{\alpha_*}(w),
  \qquad
  r_N(q)=\frac{\|d\|_\infty}{a}
  +a^{-2}\mathcal G^{\mathrm{JP}}_{\alpha_*}(w)^{1/2}.
  \]
- The regular fan is \(\alpha_*=a\mathbf1\). On a completed ray set
  \[
  \alpha_t=\alpha_*+td,\qquad
  Y_t=h_{\alpha_t}\mathbf1+
      J_{\alpha_t}(c_{\alpha_t}+tw),\qquad
  B_t=h_{\alpha_t}\mathbf1,
  \]
  where \(J_\alpha\) is the retained scale/translation quotient transport and
  \(c_\alpha\) is the pulled-back exact disk corrector
  \(z_\alpha^D=J_\alpha c_\alpha\).
- The exact completed scalar is
  \[
  \begin{aligned}
  \mathbf A_N(d,w)={}&
  \Phi_\alpha\!\left(h_\alpha\mathbf1+
        J_\alpha(c_\alpha+w)\right)
  -\Phi_\alpha(h_\alpha\mathbf1)\\
  &+\mathcal G^{\mathrm{JP}}_\alpha(J_\alpha c_\alpha)
  -\frac12\mathcal G^{\mathrm{JP}}_\alpha(J_\alpha w)
  +\frac\kappa2\mathcal J_4(\alpha),
  \qquad \alpha=\alpha_*+d.
  \end{aligned}
  \]
  This is the scalar to be differentiated; its summands may not be replaced by
  a polygon-minus-disk ledger or estimated before exact completion.
- The finite-bridge image at level \(K'\) is the set of completed coordinates
  \(q=(d,w)\) assigned to active normalized support data on the super-near
  branch for which the whole ray \(tq\), \(0\le t\le1\), stays in the retained
  material chart and \(\mathcal N_N(q)\le K'a^5\). The retained bridge gives
  \(r_N(q)\le C_{K'}a^{1/2}\) on this image.
- `JC_PL` denotes the quantified assertion $\mathscr A_\alpha(z)\ge0$ on every active normalized no-ratio support chart covered by the frozen local interface.

- JC_SP_MATFLUX denotes the typed two-family \(C^3\) material spectral,
  compatible-trace, scalar-conormal, weak-flux, reduced-DtN, and
  incidence-level leading-corner regularity package on the finite-bridge
  image.
- JC_SP_LEDGER denotes the exact atom-indexed full-cell completed
  third-derivative identity constructed from that regularity package.
- JC_SP_EST denotes the uniform estimate of that exact QRCI identity on the
  branch reached from \(E_\alpha(z)\le Ka^5\).
- JC_SP_MATREG, JC_SP_REG, JC_SP_QRCI, and JC_SP are superseded names
  retained only as audit provenance.
- JC_CL denotes the coarse-restricted lower bound for \(E_\alpha(z)>M_0a^5\); it is not the stronger whole-chart version appearing as a convenient target in some retained notes.

## Symbol Table

| Symbol | Meaning | Scope | Notes |
| --- | --- | --- | --- |
| $A$ | prescribed polygonal area | global | strictly positive |
| $N$ | number of genuine sides | global | integer, eventually $N\ge N_0$ |
| $P$ | arbitrary comparison polygon | global | bounded, open, convex, exactly $N$ genuine sides |
| $R_N(A)$ | regular area-$A$ comparator | global | unique up to congruence |
| $\lambda_1$ | first Dirichlet eigenvalue | global | scales as length$^{-2}$ |
| $\alpha$ | positive normal fan | local | may have arbitrarily small positive angles |
| $z$ | normalized support perturbation | local | the full segment must remain active |
| $\Phi_\alpha$ | scale-invariant spectral scalar | local | defined on the fixed-normal support chart |
| $\mathscr A_\alpha$ | completed pathwise action | local core | contains forcing, integrated Hessian, metric, and fan defect in one budget |
| $E_\alpha$ | completed branch energy | local core | defines the exhaustive super-near/coarse cutoff |
| $\mathcal N_N$ | completed-coordinate natural energy | super-near child | controlled by \(E_\alpha\) through the retained finite bridge |
| $r_N$ | dimensionless completed-coordinate radius | super-near child | must be \(O(a^{1/2})\) on bounded \(a^5\)-energy balls |
| $\mathbf A_N$ | exact completed scalar in fixed completed coordinates | super-near subtree | includes the moving fan, corrector, quotient transport, metric, base subtraction, and fan defect |
| $J_\alpha$ | retained scale/translation quotient transport | super-near subtree | \(J_{\alpha_*}=I\) |
| $c_\alpha$ | pulled-back disk corrector | super-near subtree | \(z_\alpha^D=J_\alpha c_\alpha\) |
| $\mathcal X_\varepsilon$ | compatible global trace space \(\operatorname{Tr}H^1(P_0^\varepsilon)\), \(\varepsilon\in\{Y,B\}\) | super-near regularity child | carries the quotient norm and has a bounded global lifting |
| $\mathcal X_\varepsilon^*$ | Hilbert dual of the compatible trace space | super-near regularity child | codomain of weak conormal and reduced-DtN maps |
| $\mathcal S_\varepsilon$ | strong open-side conormal space \(\prod_iH^{1/2}(0,1)\) | super-near regularity child | no global Dirichlet lifting is asserted from this product space |
| $\mathcal C_N^{\mathrm{mat}}$ | \(\mathbb R_\beta^N\times\mathbb R_A^{2N}\times\mathbb R_E^{4N}\) | super-near regularity child | \(A^{\mathrm c},A^{\mathrm j}\) are the average/difference of the \(Y/B\) physical sector amplitudes; \(E_{i,\sigma}^{\mathrm c},E_{i,\sigma}^{\mathrm j}\) are the corresponding scalar material conormal coefficients for both vertex incidences \(\sigma\in\{-,+\}\) |
| $\mathscr I_N$ | finite QRCI atom index set | super-near ledger child | carries a disjoint ownership map back to exact scalar source terms |
| $\mathfrak Q_N$ | exact sum of the atom-indexed completed third-jet ledger | super-near ledger and estimate children | no quantitative bound is included in its definition |
| $\mathcal J_4$ | fan defect | local | nonnegative and vanishes at the regular fan |
| $\mathcal G^{\mathrm{JP}}_\alpha$ | support energy | local | quotient metric modulo scale and translations |
| $z_\alpha^D$ | disk corrector | local | must not be separated from the completed action |

## Problem-Specific Failure Checklist

| ID | Failure mode | Triggering feature | Required adversarial check |
| --- | --- | --- | --- |
| PSF-01 | constants deteriorate with $N$ | high-frequency and microscopic fan modes | track every constant uniformly as $N\to\infty$ and test the smallest resolved scales |
| PSF-02 | a proof silently assumes a lower side-length or angle ratio | the class permits arbitrarily short positive sides | test collapsing-side and adjacent-ratio limits before taking any supremum |
| PSF-03 | a labelled affine-side interpolation leaves the admissible class | only the fixed-normal support segment is known active | verify activity of the exact path used by every derivative or integral identity |
| PSF-04 | covector and Hessian estimates double-count or lose cancellation | the completed action couples disk forcing and polygonal curvature | expand the exact scalar first and audit a disjoint complete pair ledger |
| PSF-05 | shape derivatives omit corner or material chain-rule terms | polygonal corners and moving normal fans | state the chart, regularity, and all material derivatives before differentiating |
| PSF-06 | local positivity is promoted to a global theorem without quantitative entry | compactness only gives qualitative near-disk convergence | exhibit an $N$-uniform localization threshold and a separate far-region gap |
| PSF-07 | numerical scans are treated as coercivity proofs | gap-simplex and mode searches are floating-point | require exact symbolic, rational, interval, or analytic certification for every promoted sign |
| PSF-08 | equality or scaling is lost in assembly | normalization to area $\pi$ and quotient gauges | restore arbitrary area and prove every zero mode is exactly a Euclidean congruence |

## Notation Changes

The migration preserves the revision-24 mathematical symbols where they are stable. Workflow IDs use underscores (`JC_PL`) while displayed mathematics may retain typographic labels (`JC--PL`); this is a naming convention, not a change of claim.
