# JC_CL_CIRC_RES: Circle Profile Compactness Residual

## Local Summary
- Statement: Uniform circle inverse-displacement coercivity after the real-line profile bound
- Dependencies: JC_CL_RL
- Current obstruction: convert the real-line surplus into a uniform circle surplus through compactness, concentration, and dichotomy.
- Proof status: todo
- Next action: after JC_CL_RL closes, audit the circle graph-compactness residual
- Local Context Packet: this statement + JC_CL_RL + monotone degree-one circle lifts + generalized inverses + graph convergence + PSF-01--PSF-04 and PSF-07; cyclic lattice and finite-$N$ transfers are excluded.

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
Let $\mu_X=X_\#(ds)$ and define
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
\tag{CIRC-RES}
\]

## Dependencies

- JC_CL_RL supplies a strict surplus uniform over every compactly supported
  zero-mass real-line blow-up.
- Monotonicity and degree one supply graph compactness away from concentration,
  while Fourier integration by parts identifies the left side with the
  negative half-order norm of the generalized-inverse displacement.

## Proof Strategy
Status: todo
- Plan: Kind: residual — (O1) normalize a hypothetical sequence whose quotient tends to $1/2$; (O2) use monotone graph compactness to exclude a nontrivial circle limit; (O3) rescale every concentrating component and contradict JC_CL_RL; (O4) use Fourier decoupling to show that dichotomy yields only weighted averages, then pass through flat intervals and jumps by lower semicontinuity.
- Key obstacle: the homogeneous norm permits both vanishing scale and multiple separated concentration cores.
- Needed dependencies: the constant $c_{\mathbb R}$ from JC_CL_RL, generalized-inverse Fourier identities, an exhaustive profile decomposition, and lower semicontinuity with no loss in the denominator.
- Failure trigger: constant-estimate insufficient if profile extraction loses a fixed part of the norm; interface mismatch if a noncompact profile is not covered by JC_CL_RL; proof too large if the profile decomposition cannot share one audit packet.

## Experiments and Edge Cases
Status: done

### Check 1: exact compact singular profiles
- Model: identity linearization, complete collapse, and the asymmetric antipodal two-atom map with masses $1/4$ and $3/4$.
- Method: PSF-01, PSF-02, and PSF-07; evaluate the Fourier series exactly.
- Result: the linearized and complete-collapse quotients are $1$, while the two-atom quotient is $22/29$.
- Interpretation: supports; flat intervals, jumps, and atomic pushforwards do not by themselves force the quotient to $1/2$.

### Check 2: concentration and dichotomy
- Model: zero-mass blow-ups, nonzero-mass localized profiles, and separated concentration cores.
- Method: PSF-03, PSF-04, and PSF-07; derive the real-line Riemann-sum limit and the cross-term limit.
- Result: zero-mass concentration produces exactly JC_CL_RL; nonzero mass gives matching logarithmic leading terms and quotient $1$; separated zero-mass cores combine by weighted averages.
- Interpretation: supports; JC_CL_RL is the only new coercive input visible in the singular alternatives.

## Counterexample Search
Status: done

The exact compact models and all concentration alternatives isolated in the
parent claim audit produced no counterexample. Exhaustiveness of the proposed
profile decomposition remains a proof obligation, not experimental evidence.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo

