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
- `JC_PL` denotes the quantified assertion $\mathscr A_\alpha(z)\ge0$ on every active normalized no-ratio support chart covered by the frozen local interface.

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
