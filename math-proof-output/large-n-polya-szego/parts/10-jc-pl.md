# JC_PL: Pathwise LCA Payment

## Local Summary
- Statement: Uniform nonnegativity of the completed pathwise action on every active no-ratio support chart
- Dependencies: JC_SP_EST, JC_CL
- Current obstruction: both direct branches remain open; JC_SP_EST depends on JC_SP_REG boundary regularity and the exact JC_SP_LEDGER identity before uniform QRCI bounds, while JC_CL requires an all-period integrated coarse certificate plus ratio-free transfer.
- Proof status: todo
- Next action: Stage 4 claim audit of JC_SP and JC_CL, then attack the highest-risk dependency-ready child
- Local Context Packet: exact JC_PL statement + JC_SP_MATFLUX, JC_SP_LEDGER, JC_SP_EST, and JC_CL interfaces + completed-action definitions + PSF-01--PSF-08 + attack ledger A1--A10; retained conditional text is source evidence, not a proof receipt.

## Statement
There are no-ratio fan and radial endpoint-chart thresholds, and constants
independent of \(N\), of the smallest positive fan angle, and of adjacent
angle ratios, such that the following holds after the endpoint modulus is
reduced so that \(\varepsilon_V(S)\le\kappa/2\). For every positive fan
\(\alpha\) in that neighborhood and every normalized support vector
\(z\in\mathsf X_\alpha\) whose full fixed-normal segment is active and
satisfies the retained JP--NS chart bounds,
\[
h_\alpha\mathbf 1+[0,1]z\ \text{is active},\qquad
\sup_{0\le t\le1}\|\rho_t\|_{W^{1,\infty}}
+\bigl(\mathcal G^{\mathrm{JP}}_\alpha(z)\bigr)^{1/2}
\le C(S+\rho_0),
\]
one has
\[
\mathscr A_\alpha(z)\ge0.
\]
Here \(\mathscr A_\alpha\) is the exact completed action defined in the
retained joint-comparison source; its disk forcing, true ground-state
multiplier, reduced energy, mixed flux, area, fixed-rank, and integrated
polygonal Hessian terms are evaluated with one common completed covector. Any
proof must remain valid when a genuine side tends to zero, integrate in
support time before taking a side-ratio supremum, and count terminal,
nonterminal, same-cell, adjacent, and first-separation pairs in one disjoint
complete ledger.

## Dependencies

- JC_SP_EST, after JC_SP_REG and JC_SP_LEDGER, imports nonnegativity on the branch
  \(E_\alpha(z)\le Ka^5\) after the retained finite bridge sends it to a
  completed-coordinate ball \(\mathcal N_N(q)\le K'(K)a^5\).
- JC_CL imports the coarse-restricted estimate
  \[
  E_\alpha(z)>M_0a^5
  \Longrightarrow
  \mathscr A_\alpha(z)\ge c_FE_\alpha(z)-C_Fa^5.
  \]
- The retained finite bridge, completed action equivalence, path activity, and
  positive base Hessian are closed interfaces of the migrated conditional
  source. They must be promoted to current rows if Stage 4 finds any mismatch.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — the conjecture portfolio compared quantitative disk localization, exact-\(N\) Steiner descent, conformal operator order, cellwise semidefinite pullback, and the completed-action route. Exact certificates killed the three one-step bypasses; quantitative disk localization remains a backup. The selected Route Screen row R-JC has verdict split because the energy cutoff gives the strict locality reduction JC_SP plus JC_CL implies JC_PL.
- Key obstacle: the exact completed scalar must survive both the super-near moving completed Hessian and the coarse regime with collapsing sides; estimating its covector and Hessian separately destroys the cancellation.
- Needed dependencies: JC_SP_REG, JC_SP_LEDGER, and JC_SP_EST with its bridge-dependent constant \(K'(K)\), plus the minimal coarse-restricted JC_CL with constants \(c_F,C_F,M_0\) uniform in all no-ratio limits.
- Failure trigger: interface mismatch if the finite bridge does not map the \(E_\alpha\) cutoff into the stated completed-coordinate ball; constant-estimate insufficient if either child loses powers of \(a\); route-level defect only if the exact action or active path is not common to both branches.

Route probe: author:agent:portfolio_discrete_f | phase:pre-commit | outcome:split | evidence:the cutoff \(E_\alpha(z)=Ka^5\) gives disjoint exhaustive super-near and coarse branches, with Taylor absorption on the first and quantitative positivity on the second | artifact:check-2

Interface patches: 1 (blocks JC_PL-JC-SP)
Interface patches: 1 (blocks JC_SP_EST-JC_SP_QRCI)
Attack attempts: 10
Attack evidence: A1,A2,A3,A4,A5,A6,A7,A8,A9,A10
Committed route resets: 0


## Experiments and Edge Cases
Status: in-progress

### Check 1: retained obstruction families
- Model: regular period-three side collapse, arbitrary active microscopic gap simplices, and genuinely nonregular fans with one short side.
- Method: retain exact counterexamples only as falsification inputs and keep floating-point scans non-probative.
- Result: the old fixed-reserve RF--IM statement is refuted, while no exact counterexample to JC_PL is recorded.
- Interpretation: supports the need for an integrated coarse branch; next action audit JC_CL.

### Check 2: exact energy-scale decomposition
- Model: the full active no-ratio JC_PL chart with \(E_\alpha(z)=\mathcal J_4(\alpha)+\mathcal G_\alpha^{\mathrm{JP}}(z-z_\alpha^D)\).
- Method: choose \(K>\max\{M_0,C_F/c_F\}\); on \(E_\alpha(z)\le Ka^5\) use the retained bridge to obtain \(\mathcal N_N(q)\le K'(K)a^5\) and completed-path activity, and on \(E_\alpha(z)>Ka^5\) apply the coarse-restricted lower bound without changing paths or covectors.
- Result: JC_SP and JC_CL are disjoint, exhaustive, strictly more local obligations and, with the retained bridges, imply JC_PL. Neither child is proved by this check.
- Interpretation: supports the independently reviewed branch split; next action create and audit both child rows.

## Counterexample Search
Status: in-progress

The search includes active paths approaching a zero side, high-frequency
quotient directions, support-time corner collisions, and configurations where
the \(E_\alpha\)-to-\(\mathcal N_N\) bridge might lose a ratio-free constant.
No exact counterexample to JC_PL is currently recorded.

## Proof
Status: todo

Assume JC_SP_REG, JC_SP_LEDGER, JC_SP_EST, and JC_CL. Fix
\(K>\max\{M_0,C_F/c_F\}\). If
\(E_\alpha(z)\le Ka^5\), the retained finite bridge, JC_SP_REG, JC_SP_LEDGER, and JC_SP_EST give
\(\mathscr A_\alpha(z)\ge0\). If \(E_\alpha(z)>Ka^5\), then JC_CL gives
\[
\mathscr A_\alpha(z)
\ge c_FE_\alpha(z)-C_Fa^5
>(c_FK-C_F)a^5>0.
\]
The two cases exhaust the active chart. This proves JC_PL conditionally on the
two direct children and the retained closed bridges; the unconditional proof
remains open until those children are closed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: A10 | author:agent:matflux_proof_auditor_1 | interface mismatch — the first local proof used a false moving-\(H^1\) composition inference and no differentiated all-mode Bessel \(H^{1/2}\) summation
Superseded attempts: A1@agent:portfolio_geometry_d,A2@agent:portfolio_operator_e,A3@agent:portfolio_discrete_f,A4@agent:portfolio_blind_b,A5@agent:portfolio_discrete_f,A6@agent:jc_sp_stage4_probe,A7@agent:qrci_stage4_probe,A8@agent:codex_stage5_strategy,A9@agent:matreg_counterexample_scout | three bypasses were killed, QFK remained a reserve, the action was branched, and the super-near regularity interfaces were progressively typed

## Local Audit
Status: todo
