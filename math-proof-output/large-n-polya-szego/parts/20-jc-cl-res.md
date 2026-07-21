# JC_CL_RES: Finite-(N) and Nonregular Coarse Payment

## Local Summary
- Statement: Uniform completed-action lower bound after the all-period gap certificate
- Dependencies: JC_CL_PROF
- Current obstruction: transfer the gap certificate to every finite-(N) regular active path and prove the same completed budget on genuinely nonregular original paths without side-ratio losses.
- Proof status: todo
- Next action: after JC_CL_PROF closes, run Stage 4 on the exact finite-(N) and nonregular interfaces
- Local Context Packet: this statement + JC_CL_PROF + exact completed action + original active path + no-ratio chart + PSF-01--PSF-07; no auxiliary disk-corrector path is admissible.

## Statement

There exist absolute constants $c_F>0$, $C_F<\infty$, $M_0<\infty$,
and $N_1$, together with the no-ratio chart thresholds of `JC_PL`, all
independent of the smallest positive fan angle and adjacent angle and side
ratios, such that for every $N\ge N_1$, every positive fan $\alpha$, and
every normalized support vector $z$ whose original full fixed-normal segment
is active and satisfies the `JC_PL` chart assumptions,
\[
E_\alpha(z)
=\mathcal J_4(\alpha)
+\mathcal G^{\mathrm{JP}}_\alpha(z-z_\alpha^D)>M_0a^5
\]
implies
\[
\boxed{
\mathscr A_\alpha(z)
\ge c_FE_\alpha(z)-C_Fa^5.
}
\]

## Dependencies

- JC_CL_PROF supplies one period-independent positive surplus for every
  closed microscopic regular-fan gap simplex, including collision endpoints.
- Definitions supplies $E_\alpha$, the exact completed action, the
  fixed-normal active path, and the no-ratio convention.
- The exact completed-action algebra supplies
  \[
  \mathscr A_\alpha(d+w)
  =\Phi_\alpha(h_\alpha\mathbf1+d+w)-\Phi_\alpha(h_\alpha\mathbf1)
  -\frac12\mathcal G^{\mathrm{JP}}_\alpha(w)
  +\mathcal G^{\mathrm{JP}}_\alpha(d)
  +\frac\kappa2\mathcal J_4(\alpha).
  \]

## Proof Strategy
Status: todo
- Plan: Kind: residual — first convert JC_CL_PROF into a uniform finite-$N$ regular-fan Bregman bound by exact secant, disk-multiplier, cubic, and tail estimates; then compare the complete one-budget original-path action for arbitrary positive fans without separating its covector from its integrated Hessian.
- Key obstacle: the transfer must cover microscopic periods growing with $N$, and the nonregular row must tolerate an arbitrarily short genuine side with no inverse side-length estimate.
- Needed dependencies: JC_CL_PROF, a finite-$N$ $O(a^5)$ transfer uniform over every active regular support amplitude, and a ratio-free nonregular original-path payment.
- Failure trigger: constant-estimate insufficient if transfer errors exceed $O(a^5)$; interface mismatch if an auxiliary path replaces the original active segment; proof too large if the finite-$N$ and nonregular mechanisms cannot be line-audited in one residual packet.

## Experiments and Edge Cases
Status: todo

### Check 1: one-short-side quantifier audit
- Model: positive fans with one side tending to zero, support amplitudes approaching the chart boundary, and $E_\alpha(z)\asymp a^3$.
- Method: PSF-01--PSF-04 and PSF-06; keep $N_1,c_F,C_F,M_0$ outside all fan and side-ratio quantifiers and use only the original active support segment.
- Result: the exact completed action remains well-defined, but no retained estimate supplies the required uniform lower bound; an $O(a^5)$ additive error cannot absorb a negative order-$a^3$ mode.
- Interpretation: inconclusive; next action run the full Stage 4 finite-$N$/nonregular falsification pass after JC_CL_PROF is proved.

## Counterexample Search
Status: todo

Test microscopic periods growing with (N), endpoint collision clusters,
arbitrarily short genuine sides, adjacent-angle ratios tending to zero, and
amplitudes at the no-ratio chart threshold. The disproved RF--IM estimate is a
warning against separated Hessian control, not a counterexample to this
completed-action statement.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo
