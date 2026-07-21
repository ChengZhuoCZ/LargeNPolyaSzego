# T: Large-N Convex Polygonal Polya-Szego Theorem

## Local Summary
- Statement: Large-N convex polygonal Polya-Szego theorem with rigidity
- Dependencies: JC_PL
- Current obstruction: JC_PL has not been proved or independently route-reviewed in the math-proof workflow.
- Proof status: todo
- Next action: keep peripheral assembly rows outside the current DAG until the JC_PL Crux Gate is resolved
- Local Context Packet: frozen theorem + JC_PL interface + PSF-01, PSF-02, PSF-06, PSF-08; retained conditional TeX is migration evidence, not a current audit receipt.

## Statement
There exists an integer $N_0\ge 3$ such that, for every real number $A>0$, every integer $N\ge N_0$, and every bounded open convex polygon $P\subset\mathbb R^2$ with area $|P|=A$ and exactly $N$ genuine sides,
\[
\lambda_1(P)\ge \lambda_1(R_N(A)),
\]
where $\lambda_1$ is the first Dirichlet eigenvalue and $R_N(A)$ is the regular $N$-gon of area $A$. Equality holds if and only if $P$ is congruent to $R_N(A)$.

## Dependencies

- `JC_PL`: supplies uniform nonnegativity of the completed pathwise action on the full active no-ratio support chart. The repository-level legacy assembly in `legacy/revision-24/conditional-assembly/` records the intended implication from this interface to the theorem, but it has not been promoted through current math-proof audits.

## Proof Strategy
Status: todo
- Plan: Kind: residual — compare R1 (the retained completed-action/LCA route) with R2 (a global variational or symmetrization bypass). R1 is recorded only as `tentative-select`; its core probe is `not-probed`, and no route commitment or PASS is migrated. After the core gate, re-admit and audit the conditional assembly modules in dependency order, then restore area scaling and rigidity.
- Key obstacle: the local completed-action inequality is open uniformly in side count and all adjacent side ratios.
- Needed dependencies: JC_PL with constants independent of $N$, the smallest angle, and adjacent side ratios.
- Failure trigger: route-level defect if JC_PL is false or if its required chart does not cover every near-disk competitor; interface mismatch if the retained assembly consumes a stronger estimate.

## Experiments and Edge Cases
Status: todo

### Check 1: theorem boundary cases
- Model: scaling, congruent copies, and polygons with one arbitrarily short positive side.
- Method: verify that the frozen quantifiers include all three and that no migration field excludes them.
- Result: the statement and PSF checklist include these cases; no mathematical inequality is thereby proved.
- Interpretation: supports (heuristic); next action run Stage 4 claim audit after route selection.

## Counterexample Search
Status: todo

## Proof
Status: todo

The existing conditional proof remains in `legacy/revision-24/conditional-assembly/conditional-proof.tex`. It is not canonical Stage 5 proof text and is not a proof of the frozen theorem until JC_PL and all migrated interfaces pass the required audits.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo
