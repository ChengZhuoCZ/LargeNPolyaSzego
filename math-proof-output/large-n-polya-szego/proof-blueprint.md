# Proof Blueprint

Current Stage: Stage 3: Blueprint
Active Target: none
Next Stage: Stage 3: Blueprint
Last Completed: Stage 2: preliminary literature review
Global Status: in-progress
Proof Chain: Prove the pathwise payment JC_PL, then combine it with the retained conditional assembly to obtain the large-N polygonal Polya-Szego theorem and its equality case.

## Formal Statement

There exists an integer $N_0\ge 3$ such that, for every real number $A>0$, every integer $N\ge N_0$, and every bounded open convex polygon $P\subset\mathbb R^2$ with area $|P|=A$ and exactly $N$ genuine sides,
\[
\lambda_1(P)\ge \lambda_1(R_N(A)),
\]
where $\lambda_1$ is the first Dirichlet eigenvalue and $R_N(A)$ is the regular $N$-gon of area $A$. Equality holds if and only if $P$ is congruent to $R_N(A)$.

## Statement Freeze
Status: frozen
Frozen From User Problem: The project is to prove that, for all sufficiently large side counts, the regular fixed-area convex polygon uniquely minimizes the first Dirichlet eigenvalue.
Formalization Notes: A genuine side has positive length and adjacent sides are not collinear; congruence means equality after a Euclidean isometry. The existential threshold is taken independent of the area, consistently with Dirichlet scaling.
User Permission Required For: any change to hypotheses, objects, quantifiers, parameter ranges, or conclusion

## Statement Change Log
None.

## Persistent Files

- Definitions and notation: definitions-and-notation.md
- Literature review: literature-review.md

## Hypothesis Ledger

| ID | Hypothesis | Source | Used in | Status |
| --- | --- | --- | --- | --- |
| H1 | $A>0$ | Formal statement | T | pending |
| H2 | $P\subset\mathbb R^2$ is a bounded open convex polygon with $\lvert P\rvert=A$ and exactly $N$ genuine sides | Formal statement | T, JC_PL | pending |

## Quantifier Ledger

| ID | Object | Quantifier | Scope | Depends on | Status |
| --- | --- | --- | --- | --- | --- |
| Q1 | $N_0$ | exists | integer threshold with $N_0\ge3$ | none | pending |
| Q2 | $A$ | arbitrary | positive real area | Q1 | pending |
| Q3 | $N$ | arbitrary | integer side count with $N\ge N_0$ | Q1 | pending |
| Q4 | $P$ | arbitrary | bounded open convex polygon in the theorem comparison class | H1, H2, Q2, Q3 | pending |
| Q5 | $R$ | constructed | regular comparator $R=R_N(A)$ | Q2, Q3 | pending |
| Q6 | $\alpha$ | arbitrary | positive normal fan in the active local chart | H2, Q3 | pending |
| Q7 | $z$ | arbitrary | normalized support vector in $\mathsf X_\alpha$ with an active full segment | Q6 | pending |

## Citation Cache

| Citation ID | Source | Exact locator | Exact statement | Verified hypotheses | Status |
| --- | --- | --- | --- | --- | --- |

## Certificate Plan

| Claim ID | Certificate type | Evidence plan | Verifier/ledger | Status |
| --- | --- | --- | --- | --- |
| none | none | no finite computation certificate is currently promoted as proof evidence | none | not-needed |

## Route Screen

| Route ID | Mechanism | Core ID | Probe | Verdict | Review | Cost | Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | completed-action and lowest-common-ancestor pathwise comparison in the active fixed-normal support chart | JC_PL | prove the uniform pathwise action inequality with a disjoint complete pair ledger | not-probed | pending | 3 substantial | 3 analytic | tentative-select |
| R2 | global variational localization or symmetrization bypass of the pathwise comparison | T | derive the theorem without assuming JC_PL while preserving side count and equality | not-probed | pending | 3 substantial | 3 global | backup |

## Proof DAG

T
JC_PL

| ID | Parents | Statement | Depends on | File | Risk | Status | Audit | Citation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | root | Large-N convex polygonal Polya-Szego theorem with rigidity | JC_PL | parts/00-main-theorem.md | critical | todo | not-started | none |
| JC_PL | T | Uniform nonnegativity of the completed pathwise action on every active no-ratio support chart | Definitions | parts/10-jc-pl.md | critical | todo | not-started | none |
