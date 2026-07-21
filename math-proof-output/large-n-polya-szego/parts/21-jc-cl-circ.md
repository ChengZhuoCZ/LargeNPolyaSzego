# JC_CL_CIRC: Circle Inverse-Displacement Coercivity

## Local Summary
- Statement: superseded by JC_CL_CIRC_RES and JC_CL_RL
- Dependencies: Definitions
- Current obstruction: prove a strict universal norm comparison through flat intervals, jumps, and arbitrarily concentrated transition layers.
- Proof status: todo
- Next action: use the replacement singular-limit decomposition in JC_CL_CIRC_RES
- Local Context Packet: this statement + the Fourier convention below + monotone degree-one lifts + generalized inverses + PSF-01--PSF-04 and PSF-07; finite-period lattice corrections and polygonal transfers are excluded.

## Statement

There exists an absolute constant $c_{\mathbb T}>0$ such that the following
holds. Let $X:\mathbb R\to\mathbb R$ be a nondecreasing right-continuous lift
satisfying
\[
X(s+1)=X(s)+1,
\qquad
V(s):=X(s)-s\in L^\infty(\mathbb T),
\qquad
\int_0^1V(s)\,ds=0.
\]
Let $\mu_X=X_\#(ds)$ be the pushforward of normalized Lebesgue measure on
$\mathbb T$, and set
\[
\widehat{\mu_X}(n)=\int_0^1e^{-2\pi i nX(s)}\,ds,
\qquad
\widehat V(n)=\int_0^1V(s)e^{-2\pi i ns}\,ds .
\]
Then
\[
\boxed{
\frac1{2\pi^2}\sum_{n=1}^{\infty}
\frac{|\widehat{\mu_X}(n)|^2}{n^3}
\ge
\left(\frac12+c_{\mathbb T}\right)
2\sum_{n=1}^{\infty}\frac{|\widehat V(n)|^2}{n}.
}
\tag{CIRC}
\]
Both series are finite. The conclusion includes maps with flat intervals and
jumps, using the stated right-continuous representative.

## Dependencies

- Definitions supplies only the normalized Fourier convention.
- Monotonicity and the degree-one condition imply that $V$ has bounded
  variation on the circle, so the displayed series converge.
- No finite-period gap theorem, finite-$N$ polygonal estimate, or external
  citation is imported.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — (O1) rewrite the left side as the homogeneous $H^{-1/2}$ norm of the displacement of the generalized inverse of $X$; (O2) prove a strict two-sided inverse-displacement norm comparison for strictly increasing smooth lifts; (O3) keep the constant uniform under approximation by lifts with flat intervals and jumps; (O4) rule out loss of the surplus by concentration and dichotomy.
- Key obstacle: ordinary compactness fails because monotone lifts may concentrate all nontrivial displacement into intervals of vanishing length.
- Needed dependencies: only monotonicity, the degree-one normalization, Fourier integration by parts for generalized inverses, and lower semicontinuity under monotone graph convergence.
- Failure trigger: statement likely false if a certified monotone sequence has ratio tending to $1/2$; constant-estimate insufficient if the comparison constant degenerates under concentration; proof too large if the real-line blow-up cannot share the same audit packet.

## Experiments and Edge Cases
Status: done

### Check 1: exact singular profiles
- Model: the identity, infinitesimal Fourier modes, complete collapse to one atom, and a two-atom pushforward with masses $1/4$ and $3/4$ at antipodal points.
- Method: PSF-01, PSF-02, and PSF-07; evaluate the Fourier series exactly before any floating-point search.
- Result: for an infinitesimal nonzero Fourier mode the quotient of the two sides without the proposed factor tends to $1$. Complete collapse has
  \[
  \mathfrak D_{\mathbb T}
  =\mathfrak Q_{\mathbb T}
  =\frac{\zeta(3)}{2\pi^2}.
  \]
  For the two-atom profile,
  \[
  \mathfrak D_{\mathbb T}=\frac{11\zeta(3)}{64\pi^2},
  \qquad
  \mathfrak Q_{\mathbb T}=\frac{29\zeta(3)}{128\pi^2},
  \qquad
  \frac{\mathfrak D_{\mathbb T}}{\mathfrak Q_{\mathbb T}}=\frac{22}{29}.
  \]
- Interpretation: supports; singular atomic profiles do not force the ratio to $1/2$, but these examples do not give a uniform bound for the full monotone class.

### Check 2: concentration and dichotomy
- Model: compactly supported zero-mean blow-ups embedded at scale $\varepsilon\downarrow0$, together with two profiles separated by a distance tending to infinity in blow-up coordinates.
- Method: PSF-03, PSF-04, and PSF-07; derive the real-line Fourier limit and test additivity of separated profiles.
- Result: with
  \[
  A_W(\xi)=\int_{\mathbb R}
  \{e^{-2\pi i\xi(y+W(y))}-e^{-2\pi i\xi y}\}\,dy,
  \]
  the exact Riemann-sum limits are
  \[
  \varepsilon^{-4}\mathfrak D_{\mathbb T}(X_\varepsilon)
  \longrightarrow
  \frac1{2\pi^2}\int_0^\infty\frac{|A_W(\xi)|^2}{\xi^3}\,d\xi,
  \qquad
  \varepsilon^{-4}\mathfrak Q_{\mathbb T}(V_\varepsilon)
  \longrightarrow
  2\int_0^\infty\frac{|\widehat W(\xi)|^2}{\xi}\,d\xi.
  \]
  When $\int W=0$, separated profiles have vanishing Fourier cross terms by
  the Riemann--Lebesgue lemma, so the limiting quotient is a weighted average.
  When $\int W\ne0$, the numerator and denominator have the same leading
  logarithmic coefficient and their quotient tends to $1$.
- Interpretation: supports; concentration and dichotomy preserve the plausibility of a strict surplus, while the zero-mean real-line profile inequality remains the decisive unproved limit.

## Counterexample Search
Status: done

The identity linearization, complete collapse, the asymmetric two-atom
profile, nonzero-mass blow-ups, and separated zero-mass profiles produce no
counterexample. The surviving adversarial class consists of connected
zero-mean real-line blow-ups; no exact or certified sequence in that class is
known to drive the quotient to $1/2$.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: superseded by JC_CL_RL plus JC_CL_CIRC_RES
Recent failed attempt: proof too large — the Stage 4 claim audit isolated the zero-mean real-line blow-up as an objective singular-limit interface.
Superseded attempts: none

## Route Correction

Trigger: the independent Stage 4 claim audit returned split after verifying the circle statement and its cyclic indexing.
Failure: the zero-mass concentration alternative requires a uniform real-line Fourier inequality that cannot be audited as routine circle compactness.
Failure type: proof too large
Replacement: JC_CL_RL isolates the real-line coercivity claim, while JC_CL_CIRC_RES retains the unchanged circle conclusion and the graph-compactness residual.
Stale Scope: JC_CL_CIRC only; JC_CL_PROF is rewired to JC_CL_CIRC_RES.

## Local Audit
Status: todo
