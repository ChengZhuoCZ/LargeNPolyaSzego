# Proof Blueprint

Current Stage: Stage 4: Claim Audit
Active Target: JC_CL
Next Stage: Stage 4: Claim Audit
Last Completed: Stage 5: local audit JC_SP_MATFLUX passed
Global Status: in-progress
Proof Chain: Prove typed scalar/flux material regularity JC_SP_MATFLUX, assemble the exact atom ledger JC_SP_LEDGER, estimate it in JC_SP_EST, combine that super-near branch with JC_CL to prove JC_PL, then use the retained conditional interfaces to obtain the large-N polygonal Polya-Szego theorem and its equality case.

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
| H2 | $P\subset\mathbb R^2$ is a bounded open convex polygon with $\lvert P\rvert=A$ and exactly $N$ genuine sides | Formal statement | T, JC_PL, JC_SP_MATFLUX, JC_SP_LEDGER, JC_SP_EST, JC_CL | pending |

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
| Q8 | $q=(d,w)$ | constructed | completed coordinate assigned by the retained finite bridge on the super-near subtree | Q3, Q6, Q7 | pending |
| Q9 | $K'$ | arbitrary | finite nonnegative finite-bridge energy level for JC_SP_MATFLUX | Q8 | pending |
| Q10 | $N_{K'}$ | exists | integer threshold for the fixed level \(K'\) in JC_SP_MATFLUX | Q9 | pending |
| Q11 | $\varepsilon$ | arbitrary | branch label in \(\{Y,B\}\) | Q8 | pending |
| Q12 | $i$ | arbitrary | labelled vertex index in \(\{1,\ldots,N\}\) | Q3 | pending |
| Q13 | $\sigma$ | arbitrary | one of the two incidences \(\{-,+\}\) at vertex \(i\) | Q12 | pending |

## Citation Cache

| Citation ID | Source | Exact locator | Exact statement | Verified hypotheses | Status |
| --- | --- | --- | --- | --- | --- |
| CIT-FKQ | L. Brasco, G. De Philippis, B. Velichkov, “Faber-Krahn inequalities in sharp quantitative form,” Duke Math. J. 164 (2015), 1777–1831; arXiv:1306.0392 | Main Theorem, equation (1.9), specialized to ambient dimension \(2\) and \(q=2\) | There is a dimensional constant \(\sigma_{\mathrm{FK}}>0\) such that every open \(\Omega\subset\mathbb R^2\) of finite measure satisfies \(\lvert\Omega\rvert\lambda_1(\Omega)-\lvert B\rvert\lambda_1(B)\ge\sigma_{\mathrm{FK}}\mathcal A(\Omega)^2\), where \(B\) is an equal-area disk. | The current polygons are bounded open subsets of \(\mathbb R^2\), hence have finite measure; \(q=2<\infty=2^*\) in dimension two; the normalization is scale invariant. | verified |

## Certificate Plan

| Claim ID | Certificate type | Evidence plan | Verifier/ledger | Status |
| --- | --- | --- | --- | --- |
| none | none | no finite computation certificate is currently promoted as proof evidence | none | not-needed |

## Route Screen

| Route ID | Mechanism | Core ID | Probe | Verdict | Review | Cost | Risk | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-JC | completed-scalar energy-scale decomposition in the active fixed-normal support chart | JC_PL | split: JC_SP_EST, JC_CL | split | independent-pass | 4 substantial | 4 analytic | selected |
| R-QFK | quantitative Faber--Krahn localization followed by a near-disk polygonal comparison | T | global class reduces to Fraenkel asymmetry at most \(C_{\mathrm{FK}}/N\) | split | independent-pass | 3 substantial | 3 global | backup |

## Proof DAG

T
JC_PL
JC_SP_EST
JC_SP_LEDGER
JC_SP_MATFLUX
JC_CL

| ID | Parents | Statement | Depends on | File | Risk | Status | Audit | Citation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | root | Large-N convex polygonal Polya-Szego theorem with rigidity | JC_PL | parts/00-main-theorem.md | critical | todo | not-started | none |
| JC_PL | T | Uniform nonnegativity of the completed pathwise action on every active no-ratio support chart | JC_SP_EST, JC_CL | parts/10-jc-pl.md | critical | todo | not-started | none |
| JC_SP | JC_PL | superseded by JC_SP_EST and JC_SP_QRCI | Definitions | parts/11-jc-sp.md | critical | stale | superseded | none |
| JC_SP_EST | JC_PL | Uniform natural-energy bound for the exact completed QRCI third-jet identity | JC_SP_LEDGER | parts/13-jc-sp-est.md | critical | todo | not-started | none |
| JC_SP_QRCI | JC_SP_EST | superseded by JC_SP_REG and JC_SP_LEDGER | Definitions | parts/14-jc-sp-qrci.md | critical | stale | superseded | none |
| JC_SP_LEDGER | JC_SP_EST | Exact atom-indexed QRCI full-cell identity with a disjoint complete ownership map | JC_SP_MATFLUX | parts/16-jc-sp-ledger.md | critical | todo | not-started | none |
| JC_SP_REG | JC_SP_LEDGER | superseded by JC_SP_MATREG | Definitions | parts/15-jc-sp-reg.md | critical | stale | failed | none |
| JC_SP_MATREG | JC_SP_LEDGER | superseded by JC_SP_MATFLUX | Definitions | parts/17-jc-sp-matreg.md | critical | stale | failed | none |
| JC_SP_MATFLUX | JC_SP_LEDGER | C3 two-family material spectral, compatible-trace, scalar-conormal, weak-flux, reduced-DtN, and incidence-level corner regularity | Definitions | parts/18-jc-sp-matflux.md | critical | proved | local-passed | none |
| JC_CL | JC_PL | Uniform completed-action lower bound on the coarse and collapsing-side branch | Definitions | parts/12-jc-cl.md | critical | todo | not-started | none |
