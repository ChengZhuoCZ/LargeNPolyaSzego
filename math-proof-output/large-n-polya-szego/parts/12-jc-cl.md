# JC_CL: Coarse and Collapsing-Side Payment

## Local Summary
- Statement: Uniform completed-action lower bound on the coarse and collapsing-side branch
- Dependencies: Definitions
- Current obstruction: the all-period gap-simplex inequality, its finite-\(N\) ratio-free transfer, and the genuinely nonregular original-path payment remain unproved.
- Proof status: todo
- Next action: Stage 4 claim audit, then isolate the first exact all-period or nonregular transfer obligation
- Local Context Packet: this statement + exact completed action + gap-simplex current identity + period-three collapse + PSF-01--PSF-08; numerical scans are calibration only.

## Statement
There exist constants \(c_F>0\), \(C_F<\infty\), \(M_0<\infty\), and
\(N_1\), together with the no-ratio chart thresholds of JC_PL, all independent
of the smallest positive fan angle and adjacent angle and side ratios, such
that for every \(N\ge N_1\), every positive fan \(\alpha\), and every
normalized support vector \(z\) whose original full fixed-normal segment is
active and satisfies the JC_PL chart assumptions,
\[
E_\alpha(z)
=\mathcal J_4(\alpha)
+\mathcal G^{\mathrm{JP}}_\alpha(z-z_\alpha^D)>M_0a^5
\]
implies
\[
\mathscr A_\alpha(z)
\ge c_FE_\alpha(z)-C_Fa^5.
\]
This is the minimal coarse-restricted child. It does not assert the stronger
whole-chart lower bound sometimes used as a convenient target in the retained
source.

## Dependencies

- Definitions supplies \(E_\alpha\), the exact completed action, the
  fixed-normal active path, and the no-ratio convention.
- The retained completed-action algebra supplies the exact scalar identity
  \[
  \mathscr A_\alpha(d+w)
  =\Phi_\alpha(h_\alpha\mathbf1+d+w)-\Phi_\alpha(h_\alpha\mathbf1)
  -\frac12\mathcal G^{\mathrm{JP}}_\alpha(w)
  +\mathcal G^{\mathrm{JP}}_\alpha(d)
  +\frac\kappa2\mathcal J_4(\alpha),
  \]
  with one common covector and integrated Hessian budget.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — first prove the support-time-integrated Bregman inequality on every periodic gap simplex, then transfer it uniformly to finite \(N\) and genuinely nonregular fans without leaving the original active path.
- Key obstacle: endpoint collisions make the pointwise support-time Hessian diverge negatively, so only the integrated pair ledger can be positive; a separate nonregular transfer must tolerate arbitrarily short genuine sides.
- Needed dependencies: the exact all-period OB--BC inequality, uniform secant/disk-multiplier/cubic/tail estimates with total \(O(a^5)\), and a one-budget nonregular transfer.
- Failure trigger: statement likely false if an exact closed gap-simplex point has nonpositive integrated surplus; constant-estimate insufficient if transfer errors exceed \(O(a^5)\); interface mismatch if any intermediate path is not the original active support path.

## Experiments and Edge Cases
Status: todo

### Check 1: exact period-three collapse
- Model: \(p=3\), \(u=(1/3,-1/6,-1/6)\), and gap vector \(g=(0,3/2,3/2)\).
- Method: evaluate the exact Fourier/polylogarithmic support-time identity.
- Result: \(\mathcal Q_3[u]=13\zeta(3)/(4\pi^2)\) and \(2\pi\{S_3(1)-S_3(0)\}=(10/13)\mathcal Q_3[u]\), leaving the positive completed surplus \(7\mathcal Q_3[u]/26\).
- Interpretation: supports integrated coarse positivity at a genuine collapsing-side boundary point; next action audit the all-period statement.

## Counterexample Search
Status: todo

Search the entire closed gap simplex for small exact periods, growing-period
low-frequency limits, colliding atoms, and nonregular fans with one short
side. The fact that \(S_3''(t)\to-\infty\) at a collision refutes pointwise
Hessian convexity but not the integrated claim.

## Proof
Status: todo

No proof is claimed. The leading regular obligation is the exact
finite-dimensional inequality
\[
2\pi\{S_p(1)-S_p(0)\}
\ge\left(\frac12+c_0\right)\mathcal Q_p[u]
\]
for every period and every point of the closed gap simplex. Even after this is
proved, the finite-\(N\) and nonregular transfers remain required.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo
