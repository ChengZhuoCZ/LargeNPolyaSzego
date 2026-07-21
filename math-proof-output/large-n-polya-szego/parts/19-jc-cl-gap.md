# JC_CL_GAP: Uniform Closed Gap-Simplex Coercivity

## Local Summary
- Statement: superseded by JC_CL_PROF and JC_CL_CIRC
- Dependencies: Definitions
- Current obstruction: prove a strictly positive surplus uniformly as the period grows and through arbitrary endpoint collision clusters.
- Proof status: todo
- Next action: use the replacement profile decomposition in JC_CL_PROF
- Local Context Packet: this statement + the exact pair integral + the $v$-Fourier form of the normal-sine metric + closed-simplex activity + the cyclic block-distance constraint + PSF-01--PSF-04 and PSF-07; finite-$N$, shape-derivative, and nonregular polygonal transfers are excluded.

## Statement

There exists an absolute constant $c_0>0$ with the following property. For
every integer $p\ge2$ and every $g=(g_i)_{i\in\mathbb Z/p\mathbb Z}$ in
the closed gap simplex
\[
g_i\ge0,\qquad \sum_{i=0}^{p-1}g_i=p,
\]
let $v,u\in\mathbb R^p$ be the unique mean-zero periodic vectors satisfying
\[
v_i-v_{i-1}=g_i-1,\qquad u_{i+1}-u_i=v_i.
\]
Put
\[
\widehat u_k=\frac1p\sum_{j=0}^{p-1}u_j e^{-2\pi i k j/p},
\qquad
\mathcal Q_p[u]=2\pi\sum_{k=1}^{p-1}|\widehat u_k|^2Q(k/p),
\]
where
\[
Q(x)=\frac{2\sin^4(\pi x)}{\pi^3}
\bigl\{\zeta(3,x)+\zeta(3,1-x)\bigr\}.
\]
Define the completed-source increment directly by the improper pair integral
\[
\mathcal D_p(g)
=\frac2p\sum_{i,j=0}^{p-1}(v_i-v_j)^2
\int_0^1(1-t)
\log\left|2\sin\frac{\pi\{(i-j)+t(v_i-v_j)\}}p\right|\,dt,
\]
with every zero-coefficient term interpreted as $0$, and endpoint collision
terms interpreted by their improper limits. Then the integral is finite and
\[
\boxed{
\mathcal D_p(g)\ge\left(\frac12+c_0\right)\mathcal Q_p[u].
}
\]

## Dependencies

- Definitions supplies the regular exterior-angle scale and the
  normal-sine symbol $Q$.
- The identities defining $u,v,g$ imply
  $g_i(t)=(1-t)+tg_i\ge0$, so the exact support-time path stays in the
  closed gap simplex. No finite-$N$ polygonal transfer is imported.

## Proof Strategy
Status: in-progress
- Plan: Kind: mechanism — (O1) prove improper-integral continuity and the exact trilogarithmic Bregman identity for every closed gap vector; (O2) rewrite $\mathcal Q_p$ in the displacement variable $v$; (O3) retain the simultaneous nesting $r_{i,m}=g_{i+1}+\cdots+g_{i+m}$ and prove one joint cyclic-partition coercivity inequality, rather than bounding pairs independently; (O4) make the constant uniform through low-frequency, localized-cluster, and collision compactness alternatives as $p\to\infty$.
- Key obstacle: fixed-period compactness does not prevent the optimal surplus from tending to zero as $p\to\infty$, while pointwise support-time Hessians diverge negatively at collisions.
- Needed dependencies: only the exact pair ledger, cyclic ordering, endpoint logarithm integrability, and the explicit positive symbol $Q$.
- Failure trigger: statement likely false if a certified growing-period family has nonpositive surplus; constant-estimate insufficient if the proof yields $c_0(p)\downarrow0$; interface mismatch if it uses any finite-$N$ polygonal remainder.

## Experiments and Edge Cases
Status: done

### Check 1: exact collision normalizations
- Model: $p=2$, $g=(0,2)$, and $p=3$, $g=(0,3/2,3/2)$.
- Method: exact Fourier/Hurwitz-zeta evaluation, with the pair-integral normalization rerun by `experiments/check_jc_cl_gap_simplex.py` using seed `20260721`.
- Result: the ratios $\mathcal D_2/\mathcal Q_2=1$ and $\mathcal D_3/\mathcal Q_3=10/13$ are exact; the latter leaves completed surplus $7\mathcal Q_3/26>0$.
- Interpretation: supports; next action prove that no longer period or collision cluster drives the surplus to zero.

### Check 2: growing-period candidate search
- Model: periods through $64$, including low Fourier modes, single spikes, alternating collisions, half-block collisions, boundary faces, and fixed-seed simplex samples.
- Method: PSF-01, PSF-02, and PSF-07; execute `experiments/check_jc_cl_gap_simplex.py`, treating Gauss-Legendre output only as floating-point candidate hunting.
- Result: no executed family has ratio at most $1/2$; the retained independent $p=384$ optimization reaches approximately $0.582293$, so the data cannot justify any $c_0>0.082293$.
- Interpretation: supports (heuristic); next action obtain an analytic period-uniform lower bound rather than extrapolate the scan.

### Check 3: independent committed-route repair probe
- Model: the entire closed gap simplex, collision faces, growing-period low-frequency and localized profiles, and the exact period-three RF--IM counterexample.
- Method: agent `matflux_repair_auditor_3`; PSF-01--PSF-04 and PSF-07; distinguish the completed-source claim from the stronger fixed-reserve Hessian claim.
- Result: verdict `split`; the displayed child is coherent and invariant under cyclic relabelling, reversal, addition of constants to $u$, and repetition of a primitive period. Its first load-bearing obstruction is a positive constant uniform in $p$, not a small-period sign. The RF--IM counterexample does not refute this statement.
- Interpretation: supports; next action retain this singular-limit interface as one child and leave all finite-(N) and nonregular work in `JC_CL_RES`.

## Counterexample Search
Status: done

The exact $p=2,3$ collision faces, executed $p\le64$ structured and random
families, and the independent growing-period probe produced no counterexample.
This is a pre-proof falsification result only. Simultaneous collision clusters,
continuum limits as $p\to\infty$, and profiles near the observed
$0.582293$ ratio remain mandatory analytic edge cases.

## Proof
Status: in-progress

Step 1 (exact reduction established by the first whole-target attempt).

Choose periodic lifts
\[
x_i=i+v_i,\qquad x_{i+p}=x_i+p.
\]
The gap equations give $x_i-x_{i-1}=g_i\ge0$. Along the prescribed path
$x_i(t)=i+tv_i$,
\[
x_i(t)-x_{i-1}(t)=(1-t)+tg_i.
\]
Thus distinct labels cannot collide for $t<1$. At $t=1$, every collision
factor has the form $\log(1-t)+O(1)$, which is integrable against $1-t$.
Splitting at $1-\varepsilon$ gives ordinary dominated convergence on the
first interval, while
$\int_{1-\varepsilon}^1(1-t)|\log(1-t)|\,dt=o(1)$ uniformly controls every
endpoint collision cluster. Hence all improper terms are finite and their
sum is continuous on the closed simplex.

Let $\Psi_p$ be a $p$-periodic even primitive satisfying
\[
\Psi_p''(r)=\log\left|2\sin\frac{\pi r}{p}\right|
\]
away from $p\mathbb Z$, with its continuous endpoint value supplied by twice
integrating the logarithm. Taylor's integral formula, first in the open
simplex and then by the preceding limit, gives
\[
\mathcal D_p(g)=\frac2p\sum_{i=0}^{p-1}\sum_{m=1}^{p-1}
\left\{
\Psi_p(x_{i+m}-x_i)-\Psi_p(m)
-\Psi_p'(m)(v_{i+m}-v_i)
\right\}.
\]
For each fixed $m$, $\sum_i(v_{i+m}-v_i)=0$. Hence all linear terms cancel:
\[
\boxed{
\mathcal D_p(g)=\frac2p\sum_{i=0}^{p-1}\sum_{m=1}^{p-1}
\left\{\Psi_p(r_{i,m})-\Psi_p(m)\right\},
\qquad
r_{i,m}=\sum_{s=1}^{m}g_{i+s}.
}
\tag{1}
\]
This records the indispensable nesting
$0=r_{i,0}\le r_{i,1}\le\cdots\le r_{i,p}=p$ and the mean identities
$\sum_i r_{i,m}=pm$.

The same identity has an absolutely convergent power-sum form. Indeed one may
choose
\[
\Psi_p(r)=\frac{p^2}{4\pi^2}
\sum_{n=1}^{\infty}\frac{\cos(2\pi nr/p)}{n^3}.
\]
If
\[
P_n(x)=\sum_{j=0}^{p-1}e^{2\pi i n x_j/p},
\]
then inclusion of the zero self-pairs, which cancel between the two
configurations, yields
\[
\boxed{
\mathcal D_p(g)=\frac{p}{2\pi^2}
\sum_{n=1}^{\infty}
\frac{|P_n(x)|^2-p^2\mathbf 1_{p\mid n}}{n^3}.
}
\tag{2}
\]
Absolute convergence follows from $|P_n|\le p$.

With the normalized Fourier convention in the statement,
$\widehat v_k=(e^{2\pi ik/p}-1)\widehat u_k$. Therefore
\[
\boxed{
\mathcal Q_p[u]
=\frac1{\pi^2}\sum_{k=1}^{p-1}
\sin^2\frac{\pi k}{p}
\left\{\zeta(3,k/p)+\zeta(3,1-k/p)\right\}
|\widehat v_k|^2.
}
\tag{3}
\]
There is also a power-sum form on the same frequency scale as (2). Set
\[
G_n(g)=\sum_{j=0}^{p-1}g_j e^{-2\pi i n j/p}.
\]
For $p\nmid n$, the constant part of $g$ vanishes and
\[
G_n(g)=p(1-e^{-2\pi i n/p})\widehat v_{\,n\bmod p}.
\]
Grouping the positive integers by their nonzero residue classes, then using
the reality symmetries
$|G_{p-k}|=|G_k|$ and $|\widehat v_{p-k}|=|\widehat v_k|$, turns (3) into
\[
\boxed{
\mathcal Q_p[u]
=\frac{p}{2\pi^2}
\sum_{\substack{n\ge1\\p\nmid n}}\frac{|G_n(g)|^2}{n^3}.
}
\tag{4}
\]
Consequently the target is exactly the following joint stability inequality:
\[
\sum_{n\ge1}\frac{
|P_n(x)|^2-p^2\mathbf 1_{p\mid n}
-\frac12\mathbf 1_{p\nmid n}|G_n(g)|^2}{n^3}
\ge
c_0\sum_{\substack{n\ge1\\p\nmid n}}\frac{|G_n(g)|^2}{n^3}.
\tag{5}
\]
The remaining obligation is to prove (5) uniformly in $p$. A termwise
comparison cannot do this: nonmultiple frequencies contribute the positive
$|P_n|^2$, whereas the multiples of $p$ contribute the coupled negative
defects
\[
-\frac{p^2-|P_{\ell p}|^2}{(\ell p)^3}.
\]
Thus the cyclic ordering has to control the full frequency sum jointly.

Failed mechanism (independent pair convexification).

The first attempt replaced each Bregman quotient separately by
\[
a_p(m):=\inf_{0\le r\le p}
\int_0^1(1-t)
\log\left|2\sin\frac{\pi\{(1-t)m+tr\}}p\right|\,dt.
\]
Because $\log\sin$ is concave between consecutive singular endpoints, this
infimum is attained at $r=0$ or $r=p$. The resulting circulant lower form has
character symbol
\[
8\sum_{m=1}^{p-1}a_p(m)\sin^2\frac{\pi km}{p}.
\]
For even $p\ge4$, its alternating character is negative: pair $m$ with
$p-m$, insert the endpoint formula, and integrate the finite geometric cosine
sum. Thus independent pair minima discard exactly the nested block-distance
constraint in (1) and cannot prove even nonnegativity. This does not refute
the target, because the failed inference independently chooses mutually
incompatible collision endpoints for different $(i,m)$.

The proof remains open at O3: establish the joint cyclic-partition inequality
using all nested block sums simultaneously. The coherent multiscale retry
identified a stronger singular-limit statement that cannot share this finite
period audit packet: the $H^{-1/2}$ inverse-displacement inequality for
monotone degree-one circle maps. The finite-period compactness transfer is a
separate residual argument.

## Proof Attempt Log
Active attempt: superseded by the profile decomposition JC_CL_CIRC plus JC_CL_PROF
Recent failed attempt: proof too large — the whole-target retry reduced the macroscopic regime to a stronger circle-map coercivity inequality, while localized zero-mass clusters require a separate concentration/compactness transfer.
Superseded attempts: independent pair convexification and frequencywise/scale-by-scale Hardy estimates fail because they destroy the cancellations between nested block lengths and period-multiple frequencies.

## Route Correction

Trigger: the bounded whole-target retry exposed a stronger singular-limit claim and a distinct finite-period compactness interface.
Failure: the exact reductions (1)--(5) do not yield a joint uniform reserve without first controlling inverse displacements of arbitrary monotone degree-one circle maps; transferring that control back to the discrete cyclic simplex is logically separate.
Failure type: proof too large
Replacement: JC_CL_CIRC proves the circle profile inequality, and JC_CL_PROF retains the finite-period compactness residual used by JC_CL_RES.
Stale Scope: JC_CL_GAP only; JC_CL_RES is rewired to JC_CL_PROF.

## Local Audit
Status: todo
