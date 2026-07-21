# JC_CL_RL: Real-Line Zero-Mass Coercivity

## Local Summary
- Statement: Uniform real-line coercivity for zero-mass monotone displacement profiles
- Dependencies: Definitions
- Current obstruction: prove the quantitative Cayley cross-term estimate in
  Step 8, uniformly through concentration and coherent long-period trains.
- Proof status: todo
- Next action: prove a strict angle bound for the two Cayley components, or
  produce a certified extremizing sequence; fixed-period compactness alone is
  not sufficient.
- Local Context Packet: this statement + the Fourier convention below + compactly supported BV displacements + monotone real-line lifts + PSF-01--PSF-04 and PSF-07; circle compactness, cyclic lattices, and finite-$N$ polygonal transfers are excluded.

## Statement

There exists an absolute constant $c_{\mathbb R}>0$ such that the following
holds. Let $W\in BV(\mathbb R)$ have compact support and satisfy
\[
\int_{\mathbb R}W(y)\,dy=0,
\qquad
T(y):=y+W(y)\ \text{is nondecreasing}.
\]
Choose the right-continuous representative of $T$ and set
\[
\widehat W(\xi)=\int_{\mathbb R}W(y)e^{-2\pi i\xi y}\,dy,
\]
\[
A_W(\xi)=\int_{\mathbb R}
\left\{e^{-2\pi i\xi T(y)}-e^{-2\pi i\xi y}\right\}\,dy .
\]
Then both integrals below are finite and
\[
\boxed{
\frac1{2\pi^2}\int_0^\infty
\frac{|A_W(\xi)|^2}{\xi^3}\,d\xi
\ge
\left(\frac12+c_{\mathbb R}\right)
2\int_0^\infty
\frac{|\widehat W(\xi)|^2}{\xi}\,d\xi .
}
\tag{RL}
\]

## Dependencies

- Definitions supplies only the Fourier normalization.
- Compact support, bounded variation, and zero mass give
  $\widehat W(\xi)=O(\xi)$ and $A_W(\xi)=O(\xi^2)$ at the origin, while the
  BV bounds control both tails. Hence the displayed quantities are finite.
- No circle, lattice, finite-period, or polygonal estimate is imported.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — (O1) identify $A_W/(2\pi i\xi)$ with the Fourier transform of the displacement of the generalized inverse of $T$; (O2) express both sides as logarithmic energies of the two coordinate marginals of the signed region between the graphs of $T$ and the identity; (O3) prove a strict norm comparison for a single connected zero-mass profile; (O4) extend by BV approximation and show that separated profiles combine by weighted averages.
- Key obstacle: the inverse displacement can acquire oscillatory Fourier phases across different height layers, so equimeasurability alone does not compare the negative half-order norms.
- Needed dependencies: monotone generalized-inverse calculus, Fourier integration by parts, exact scaling invariance, and a lower-semicontinuity argument that preserves the strict constant.
- Failure trigger: statement likely false if a certified compactly supported profile has ratio at most $1/2$; constant-estimate insufficient if the surplus vanishes along connected profiles of growing support; proof too large if a further irreducible profile interface appears.

## Experiments and Edge Cases
Status: done

### Check 1: origin, tail, and scaling audit
- Model: arbitrary compactly supported $BV$ profiles with zero mass and their dilations $W_\varepsilon(y)=\varepsilon W(y/\varepsilon)$.
- Method: PSF-01, PSF-03, and PSF-07; expand the two Fourier transforms at $\xi=0$ and change variables exactly under dilation.
- Result: zero mass gives $\widehat W(\xi)=O(\xi)$ and $A_W(\xi)=O(\xi^2)$. Both energies scale by the fourth power of the spatial dilation, so their quotient is scale invariant.
- Interpretation: supports; the statement is finite and correctly normalized, but scale invariance removes ordinary compactness.

### Check 2: elementary singular and separated profiles
- Model: infinitesimal smooth profiles, the interval-collapse profile $W(y)=-y$ on $[-1,1]$, finite symmetric staircases, and separated localized profiles.
- Method: PSF-02--PSF-04 and PSF-07; use exact Fourier expansion at zero amplitude and the Riemann--Lebesgue lemma for cross terms.
- Result: the infinitesimal quotient tends to $1$. For interval collapse,
  \[
  A_W(\xi)=2-\frac{\sin(2\pi\xi)}{\pi\xi},
  \qquad
  \widehat W(\xi)=\frac{2i(\sin a-a\cos a)}{a^2},
  \quad a=2\pi\xi,
  \]
  and exact integration gives
  \[
  \frac{\mathfrak D_{\mathbb R}(W)}
       {\mathfrak Q_{\mathbb R}(W)}
  =\frac{4\log2-1}{3}
  =0.5908629066\ldots .
  \]
  There is also a strictly better exact calibration. Let $T$ be odd, let
  $T=0$ on $[-3/5,3/5]$, give $T$ jumps of size $1/2$ at the two endpoints,
  and join $(3/5,1/2)$ to $(1,1)$ affinely (with the odd reflected tail).
  In the probability-measure notation of (12), direct integration of
  $r^2\log|r|$ gives
  \[
  I(\mu)=\frac7{120}+\frac{\log5}{24}-\frac{9\log3}{200},
  \qquad
  I(\nu)=-\frac3{100}+\frac{27\log3}{400},
  \]
  and hence
  \[
  \frac{E(U)}{E(W)}
  =\frac{81\log3-36}{70+50\log5-54\log3}
  =0.5813432480\ldots .
  \]
  The decimal is not used for the inequality: the positive-term
  expansion
  $\log x=2\sum_{j\ge0}z^{2j+1}/(2j+1)$,
  $z=(x-1)/(x+1)$, gives rigorous rational upper and lower bounds.
  Alignment-correct symmetric staircase searches reached approximately
  $0.58316$ and never $1/2$; that search remains heuristic only. Separated zero-mass
  components yield weighted averages. Opposite nonzero-mass components have
  matching logarithmic leading energies, so their quotient tends to $1$.
- Interpretation: supports; neither linearization, interval collapse, nor dichotomy creates a counterexample, leaving connected profiles with increasingly fine internal structure as the decisive class. Any valid constant must satisfy
  \[
  c_{\mathbb R}\le
  \frac{81\log3-36}{70+50\log5-54\log3}-\frac12
  <0.081344.
  \]

### Check 3: independent full-class claim audit
- Model: the entire compactly supported zero-mass $BV$ class, including jumps, plateaus, dilations, connected staircases, and separated components.
- Method: agent jc_cl_rl_claim_auditor; PSF-01--PSF-04 and PSF-07; verify the generalized-inverse convention and try to force the quotient to $1/2$.
- Result: verdict commit; the statement, normalization, finiteness, and invariances are coherent, and no exact or certified counterexample was found.
- Interpretation: supports; proceed to a whole-target proof of the strict inverse-displacement norm comparison.

## Counterexample Search
Status: done

Exact linearization, scale changes, interval collapse, finite step profiles,
separated zero-mass profiles, and opposite nonzero-mass pairs produced no
counterexample. The remaining falsification target is a connected compactly
supported monotone profile, or a sequence of such profiles with increasing
internal complexity, whose quotient tends to $1/2$.

## Proof
Status: in-progress

Step 1 (exact generalized-inverse reduction).

Let
\[
S(x)=\inf\{y\in\mathbb R:T(y)>x\},
\qquad
U(x)=S(x)-x,
\]
using the left-continuous generalized inverse; changing representatives on
countably many jump values does not affect any Fourier integral. Since
$T(y)=y$ outside a compact interval, the same is true of $S$, and
$U\in BV_c(\mathbb R)$.

For every $\varphi\in C_c^1(\mathbb R)$, monotone change of variables gives
\[
\int_{\mathbb R}\varphi(T(y))\,dy
=\int_{\mathbb R}\varphi(x)\,dS(x).
\]
Subtracting the identity measure and integrating by parts therefore yields,
for $\xi\ne0$,
\[
A_W(\xi)
=\int_{\mathbb R}e^{-2\pi i\xi x}\,dU(x)
=2\pi i\xi\,\widehat U(\xi).
\tag{1}
\]
Consequently the desired estimate is exactly
\[
\boxed{
\|U\|_{\dot H^{-1/2}}^2
\ge\left(\frac12+c_{\mathbb R}\right)
\|W\|_{\dot H^{-1/2}}^2,
\qquad
\|f\|_{\dot H^{-1/2}}^2
:=2\int_0^\infty\frac{|\widehat f(\xi)|^2}{\xi}\,d\xi .
}
\tag{2}
\]

Step 2 (the inverse preserves the full amplitude distribution).

For every $t>0$, the generalized-inverse relation gives, up to null endpoint
sets,
\[
\{x:U(x)<-t\}=\{y+t:W(y)>t\},
\qquad
\{x:U(x)>t\}=\{y-t:W(y)<-t\}.
\tag{3}
\]
Thus $U$ and $-W$ are equimeasurable. In particular,
\[
\int_{\mathbb R}|U|^q=\int_{\mathbb R}|W|^q
\quad(1\le q\le\infty),
\qquad
\int_{\mathbb R}U=-\int_{\mathbb R}W=0.
\tag{4}
\]
This also proves directly that both sides of (2) are invariant under the
common dilation $W_\varepsilon(y)=\varepsilon W(y/\varepsilon)$.

Step 3 (convex-dual formulation).

Define compactly supported primitives
\[
F(y)=\int_{-\infty}^yW(s)\,ds,
\qquad
G(x)=\int_{-\infty}^xU(s)\,ds.
\]
Then
\[
\Phi(y)=\frac{y^2}{2}+F(y)
\]
is convex and $\Phi^*(x)=x^2/2+G(x)$ after fixing the additive constant at
infinity. At every graph point $x=T(y)$ where the single-valued formulas
apply, Fenchel equality gives
\[
G(T(y))=-F(y)-\frac12W(y)^2.
\tag{5}
\]
Moreover (2) is equivalently the comparison of the homogeneous
$H^{1/2}$ seminorms of the two compact perturbations $G$ and $F$.

Step 4 (first whole-target mechanism and its exact failure).

Writing
\[
A_t=\{W>t\},\qquad B_t=\{W<-t\},
\]
the layer-cake formula and (3) give
\[
\widehat W(\xi)
=\int_0^\infty
\{\widehat{\mathbf1_{A_t}}(\xi)
-\widehat{\mathbf1_{B_t}}(\xi)\}\,dt,
\tag{6}
\]
\[
\widehat U(\xi)
=\int_0^\infty
\{e^{2\pi i\xi t}\widehat{\mathbf1_{B_t}}(\xi)
-e^{-2\pi i\xi t}\widehat{\mathbf1_{A_t}}(\xi)\}\,dt.
\tag{7}
\]
Equimeasurability controls the amplitudes in these formulas, but not the
frequency-dependent phases in (7). Applying the triangle inequality or
estimating the two sign families separately loses all fixed surplus: the
phase factors may cancel at a prescribed frequency, and the monotone nesting
of the level sets only becomes visible after the full $\xi^{-1}$ integration.
Hence an amplitude-only rearrangement estimate cannot prove (2).

Step 5 (two exact dynamic/geometric reformulations).

For $0\le\tau\le1$, let $T_\tau=\operatorname{id}+\tau W$ and let
$S_\tau$ be its generalized inverse. Define
\[
h_\tau(q)=\frac{q-S_\tau(q)}{\tau}\quad(\tau>0),
\qquad h_0=W.
\]
The level-set identity (3), with $\tau W$ in place of $W$, shows that
$h_\tau$ is equimeasurable with $W$. At smooth graph points it satisfies
\[
h_\tau(q)=W(S_\tau(q)),
\qquad
\partial_\tau h_\tau+h_\tau\partial_qh_\tau=0.
\]
Across upward jumps of $W$, the generalized inverse fills the centered
rarefaction fan, so the same formula is precisely the entropy solution of
inviscid Burgers. Since $U=S_1-\operatorname{id}=-h_1$, (2) is equivalent to
\[
\|h_1\|_{\dot H^{-1/2}}^2
\ge\left(\frac12+c_{\mathbb R}\right)
\|h_0\|_{\dot H^{-1/2}}^2
\tag{8}
\]
for every compactly supported zero-mean datum with distributional derivative
$W'\ge-1$. Thus the issue is a critical-time lower bound for the Burgers
entropy semigroup at the first time a slope $-1$ can focus.

There is also a symmetric Minty parametrization. Rotate the graph of $T$ by
$\pi/4$ and write
\[
r=\frac{y+T(y)}{\sqrt2},
\qquad
k(r)=\frac{T(y)-y}{\sqrt2}.
\]
Then $k$ is compactly supported and $1$-Lipschitz, and
\[
\int_{\mathbb R}k(r)\,dr=\int_{\mathbb R}W(y)\,dy=0.
\]
Conversely every compactly supported mean-zero $1$-Lipschitz $k$ arises this
way. The two complementary coordinates are
\[
y=\frac{r-k(r)}{\sqrt2},
\qquad
x=T(y)=\frac{r+k(r)}{\sqrt2},
\]
and
\[
W(y)=\sqrt2\,k(r),
\qquad
U(x)=-\sqrt2\,k(r).
\tag{9}
\]
The common spatial/amplitude scaling cancels in the homogeneous norm.
Therefore (2) is also exactly a two-map inequality comparing the same
$1$-Lipschitz, mean-zero function pulled back by
$\operatorname{id}-k$ and $\operatorname{id}+k$.

Step 6 (exact dissipation and measure formulations).

Use the Hilbert-transform convention
\[
\widehat{\mathcal Hf}(\xi)=-i\,\operatorname {sgn}(\xi)\widehat f(\xi)
\]
and put $E(h)=\|h\|_{\dot H^{-1/2}}^2$. Smooth solutions of the Burgers
formulation in Step 5 satisfy
\[
\frac{d}{d\tau}E(h_\tau)
=-2\pi\int_{\mathbb R}h_\tau^2\mathcal Hh_\tau
=-\frac{2\pi}{3}\int_{\mathbb R}(\mathcal Hh_\tau)^3.
\tag{10}
\]
The first equality follows by differentiating the Fourier energy and using
$\partial_\tau h=-\partial_x(h^2/2)$; the second is the cubic boundary-value
identity for $h+i\mathcal Hh$. Strict approximation in the Minty
parametrization extends the integrated identity through rarefaction fans.
Consequently (RL) is equivalent to the existence of $\eta>0$ such that
\[
2\pi\int_0^1\!\int_{\mathbb R}h_\tau^2\mathcal Hh_\tau\,dx\,d\tau
\le \left(\frac12-\eta\right)E(W).
\tag{11}
\]
The cubic integrand has no useful pointwise sign: the constraint $W'\ge-1$
alone does not control the same-sign contributions across an upward jump.
Thus a one-time Gronwall estimate does not prove (11).

There is also an exact probability-measure form. After a common translation
and dilation, assume that $W$ is supported in $[-1,1]$. Let
\[
d\lambda=\frac12\mathbf1_{[-1,1]},dx,
\qquad \mu=\frac12\,dT,
\qquad \nu=\frac12\,dS=T_\#\lambda.
\]
Both $\mu$ and $\nu$ are probability measures of barycenter zero. If
\[
I(\rho)=\iint (x-y)^2\log|x-y|\,
d(\rho-\lambda)(x)d(\rho-\lambda)(y),
\]
then Fourier transformation of $(x^2\log|x|)''=2\log|x|+3$ gives
\[
E(W)=4I(\mu),\qquad E(U)=4I(\nu).
\tag{12}
\]
For an atomic staircase $\mu=\sum_{i=1}^n p_i\delta_{y_i}$, with
$P_i=\sum_{j\le i}p_j$, $y_0=-1$, and $y_{n+1}=1$, the conjugate measure is
\[
\nu=\sum_{i=0}^n\frac{y_{i+1}-y_i}{2}
\,\delta_{-1+2P_i}.
\tag{13}
\]
The endpoint terms $i=0,n$ are essential. Formula (13) makes the involution
and all plateau/jump indices explicit, but its Euler--Lagrange equation still
contains the same nonlocal comparison as (11).

Step 7 (a periodic obstruction to the first compactness plan).

Let $V$ be a mean-zero displacement of a degree-one monotone circle lift,
cut at a point for which the two boundary jumps needed below are upward, and
define
\[
W_N(y)=V(y-j)\quad (j\le y<j+1,\ 0\le j<N),
\qquad W_N=0\quad\text{off }[0,N].
\]
Then $\operatorname{id}+W_N$ is nondecreasing and $\int W_N=0$. With
\[
D_N(\xi)=\sum_{j=0}^{N-1}e^{-2\pi i\xi j}
\]
one has exactly
\[
\widehat W_N(\xi)=D_N(\xi)\widehat W_1(\xi),
\qquad
A_{W_N}(\xi)=D_N(\xi)A_{W_1}(\xi).
\tag{14}
\]
The Fejer-comb limit therefore turns both real-line energies, divided by
$N$, into the corresponding circle Fourier series. In particular, adjacent
cells do not decouple into a weighted average: their phases add coherently at
integer frequencies. Hence a profile decomposition containing only one
compact core and separated zero-mass dichotomy is not exhaustive. Any
compactness proof of (RL) must include a periodic/stationary alternative and
must prove its endpoint inequality independently; importing the downstream
circle conclusion would be circular.

The remaining obligation is thus the common periodic/real-line phase
estimate: equivalently, the Burgers dissipation budget (11), the conjugate
measure comparison from (12), or the complementary-map estimate (9). The
convex-dual pointwise route is insufficient as well: for interval collapse,
$F(y)=(1-y^2)/2$ while $-G(x)=(1-|x|)^2/2$ on $[-1,1]$, so the pointwise ratio
$(-G)/F$ tends to zero at the boundary even though the global energy ratio is
strictly larger than $1/2$.

Step 8 (Hardy budget and the exact Cayley cross term).

The Burgers formulation has a useful exact Hardy-space packaging, but it
also rules out a natural pointwise-in-time shortcut. Write

\[
z_t=h_t+i\mathcal Hh_t
\]

for the positive-frequency analytic signal in the upper half-plane. With the
normalization in (2), direct Plancherel integration gives

\[
\int_{\mathbb H}|z_t|^2\,dx\,dy=\frac{E(h_t)}{2\pi}.
\]

Since $(\Im z_t)_y=(\Re z_t)_x$, integration first on horizontal lines and
then in $y$ yields

\[
\int h_t^2\mathcal Hh_t
=\frac13\int(\mathcal Hh_t)^3
=-\int_{\mathbb H}|z_t|^2\Re z_t'\,dx\,dy.
\tag{15}
\]

The two monotonicity inequalities along the entropy interpolation are

\[
-\frac1{1-t}\le \partial_xh_t\le\frac1t.
\]

Consequently

\[
p_t:=t+t(1-t)z_t'
\qquad\text{satisfies}\qquad
0\le\Re p_t\le1
\quad\text{in }\mathbb H.
\]

If

\[
m(t)=\frac{\int_{\mathbb H}|z_t|^2\Re p_t}
{\int_{\mathbb H}|z_t|^2},
\]

then (10) and (15) give the exact identity

\[
\boxed{
\frac d{dt}\log E(h_t)=\frac{m(t)-t}{t(1-t)}.
}
\tag{16}
\]

The tempting estimate $m(t)\ge t/(2-t)$, which would integrate to the
non-strict factor $1/2$, is false. For the interval-collapse datum
$W(x)=-x$ on $[-1,1]$, put $a=1-t$. An exact Fourier calculation gives

\[
E(t)=\frac{8J(a)}{t^2a^2},
\]

\[
24J(a)=8a^2\log2+8a^4\log(2a)
+a(1-a)^4\log(1-a)-a(1+a)^4\log(1+a).
\]

Substitution into (16) gives
$m(0.9)=0.7948739137\ldots<9/11$. Thus the proof must use a genuinely
integrated endpoint mechanism rather than a pointwise strip bound.

That endpoint mechanism can be isolated as one scalar angle estimate. In
the Minty parametrization (9), suppress the harmless common $\sqrt2$ scale
and use the angular Fourier variable $\omega>0$. Define

\[
C(\omega)=\frac1\omega\int_{\mathbb R}
e^{-i\omega r}\sin(\omega k(r))\,dr,
\]

\[
D(\omega)=-\frac i\omega\int_{\mathbb R}
e^{-i\omega r}\{1-\cos(\omega k(r))\}\,dr.
\tag{17}
\]

The second expression also equals

\[
D(\omega)=-\frac1\omega\int_{\mathbb R}
e^{-i\omega r}k'(r)\sin(\omega k(r))\,dr,
\]

first for smooth compactly supported $k$ and then by $BV$ approximation.
Fourier integration by parts in the two coordinates
$r\mapsto r\pm k(r)$ shows that the endpoint transforms are $C+D$ and
$C-D$, up to a common unimodular factor and interchange of the signs.
Therefore, in

\[
\mathcal H=L^2((0,\infty),d\omega/\omega),
\]

if

\[
S=\|C\|_{\mathcal H}^2+\|D\|_{\mathcal H}^2,
\qquad
R=\Re\langle C,D\rangle_{\mathcal H},
\]

then exactly

\[
E_+=S+2R,\qquad E_-=S-2R.
\tag{18}
\]

It follows that the two-sided baseline
$\min(E_+,E_-)\ge\frac12\max(E_+,E_-)$ is equivalent to

\[
|R|\le\frac16S,
\]

and a period-independent strict surplus is equivalent to the quantitative
Cayley estimate

\[
\boxed{
|R|\le\left(\frac16-\delta\right)S
}
\tag{19}
\]

for some absolute $\delta>0$. Formula (19) is now the sole unresolved
analytic estimate in this row. Equality exclusion in each fixed compact
class would not suffice: dilation, dichotomy, and coherent periodic trains
must all be included in the stability argument.

## Proof Attempt Log
Active attempt: quantitative Cayley cross-term estimate (19)
Recent failed attempt: constant-estimate insufficient -- the pointwise Hardy-strip estimate $m(t)\ge t/(2-t)$ is false for the exact interval-collapse flow; fixed-period equality exclusion also omits coherent long-period trains.
Superseded attempts: amplitude-only layer estimates in (6)--(7)

## Local Audit
Status: todo
