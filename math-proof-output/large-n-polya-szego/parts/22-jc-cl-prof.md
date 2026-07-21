# JC_CL_PROF: Discrete Profile Compactness Transfer

## Local Summary
- Statement: Uniform closed gap-simplex coercivity after the circle profile inequality
- Dependencies: JC_CL_CIRC_RES
- Current obstruction: transfer the strict circle surplus through the lattice baseline and every vanishing-scale collision profile.
- Proof status: todo
- Next action: after JC_CL_CIRC_RES closes, audit the finite-period concentration/compactness transfer
- Local Context Packet: this statement + JC_CL_CIRC_RES + the exact Bregman and power-sum identities inherited from JC_CL_GAP + closed-simplex collision continuity + PSF-01--PSF-04 and PSF-07; finite-$N$ polygonal transfers are excluded.

## Statement

There exists an absolute constant $c_0>0$ with the following property. For
every integer $p\ge2$ and every
$g=(g_i)_{i\in\mathbb Z/p\mathbb Z}$ satisfying
\[
g_i\ge0,\qquad \sum_{i=0}^{p-1}g_i=p,
\]
let $v,u\in\mathbb R^p$ be the unique mean-zero periodic vectors satisfying
\[
v_i-v_{i-1}=g_i-1,\qquad u_{i+1}-u_i=v_i.
\]
With
\[
\widehat u_k=\frac1p\sum_{j=0}^{p-1}u_j e^{-2\pi i k j/p},
\qquad
\mathcal Q_p[u]=2\pi\sum_{k=1}^{p-1}|\widehat u_k|^2Q(k/p),
\]
\[
Q(x)=\frac{2\sin^4(\pi x)}{\pi^3}
\{\zeta(3,x)+\zeta(3,1-x)\},
\]
define
\[
\mathcal D_p(g)
=\frac2p\sum_{i,j=0}^{p-1}(v_i-v_j)^2
\int_0^1(1-t)
\log\left|2\sin\frac{\pi\{(i-j)+t(v_i-v_j)\}}p\right|\,dt
\]
by improper limits at endpoint collisions and by $0$ for every
zero-coefficient term. Then
\[
\boxed{
\mathcal D_p(g)\ge
\left(\frac12+c_0\right)\mathcal Q_p[u].
}
\tag{PROF}
\]

## Dependencies

- JC_CL_CIRC_RES supplies a period-independent strict surplus for every monotone
  degree-one circle profile, including atomic and concentrated limits.
- The exact identities retained in JC_CL_GAP supply the cyclic Bregman form,
  the power-sum form of $\mathcal D_p$, the power-sum form of $\mathcal Q_p$,
  and continuity on the closed gap simplex. Those identities are rederived in
  this part before use; the stale row is not treated as a proved dependency.

## Proof Strategy
Status: todo
- Plan: Kind: residual — (O1) encode each cyclic gap vector by its monotone empirical step lift and identify the common circle energy plus the regular lattice baseline; (O2) use JC_CL_CIRC_RES when the profile energy stays macroscopic relative to that baseline; (O3) rescale every vanishing-energy sequence and show that its zero-mass blow-up is governed by the same profile constant, while nonzero-mass clusters have ratio tending to $1$; (O4) use additivity under dichotomy and closed-simplex continuity to exclude loss of the surplus.
- Key obstacle: subtracting the regular lattice baseline destroys a direct application of JC_CL_CIRC exactly in the small-profile regime.
- Needed dependencies: the constant $c_{\mathbb T}$ from JC_CL_CIRC_RES, exact cyclic Fourier identities with all normalization factors, monotone profile compactness, and a uniform root-neighborhood estimate.
- Failure trigger: constant-estimate insufficient if the lattice baseline consumes the circle surplus; interface mismatch if a genuinely independent lattice inequality is needed; proof too large if one concentration profile requires a separate audit packet.

## Experiments and Edge Cases
Status: todo

### Check 1: lattice-baseline normalization
- Model: regular gaps, infinitesimal modes, the exact $p=2$ collision, and the exact $p=3$ collapse.
- Method: PSF-01, PSF-02, and PSF-07; compare the empirical-step circle energies with the finite power sums term by term.
- Result: pending Stage 4 verification.
- Interpretation: inconclusive; the exact baseline comparison has not yet been executed.

### Check 2: all concentration regimes
- Model: macroscopic profiles, fixed-support clusters, growing $o(p)$ zero-mass clusters, nonzero-mass clusters, and separated clusters.
- Method: PSF-03, PSF-04, and PSF-07; derive each limiting functional and verify that the alternatives are exhaustive.
- Result: pending Stage 4 verification.
- Interpretation: inconclusive; the proposed concentration alternatives are not yet known to be exhaustive.

## Counterexample Search
Status: todo

Search the full closed simplex, with special attention to growing zero-mass
collision clusters and sequences whose circle energy is comparable to the
regular lattice baseline.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo
