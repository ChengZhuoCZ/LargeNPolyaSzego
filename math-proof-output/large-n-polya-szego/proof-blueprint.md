# Proof Blueprint

Current Stage: Stage 5: Local Proof
Active Target: JC_CL_RL
Next Stage: Stage 5: Local Proof
Last Completed: Stage 5: local audit JC_SP_COORD passed
Global Status: in-progress
Proof Chain: Prove JC_SP_MATFLUX and the finite-dimensional coordinate bridge JC_SP_COORD, derive the completed five-source normal form JC_SP_SRC, and estimate it in JC_SP_EST; prove the real-line profile inequality JC_CL_RL, transfer it to the circle in JC_CL_CIRC_RES and to all finite gap simplices in JC_CL_PROF, then complete JC_CL_RES; combine both branches in JC_PL and obtain the theorem and rigidity.

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
| H2 | $P\subset\mathbb R^2$ is a bounded open convex polygon with $\lvert P\rvert=A$ and exactly $N$ genuine sides | Formal statement | T, JC_PL, JC_SP_MATFLUX, JC_SP_SRC, JC_SP_EST, JC_CL | pending |

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
| Q14 | $c_{\mathbb R}$ | exists | absolute coercivity surplus in JC_CL_RL | none | pending |
| Q15 | $W$ | arbitrary | compactly supported zero-mass $BV(\mathbb R)$ displacement with $\operatorname{id}+W$ nondecreasing | Q14 | pending |
| Q16 | $\tau$ | arbitrary | Burgers interpolation time in $[0,1]$ | Q15 | pending |
| Q17 | $T$ | constructed | monotone interpolation $T_\tau=\operatorname{id}+\tau W$ | Q15, Q16 | pending |
| Q18 | $U$ | constructed | compactly supported displacement of the generalized inverse of $\operatorname{id}+W$ | Q15 | pending |
| Q19 | $E$ | defined | homogeneous negative half-order energy used along the Burgers interpolation | Q15 | pending |
| Q20 | $\mu$ | arbitrary | atomic staircase probability measure used in the dense finite-profile reduction | Q15 | pending |
| Q21 | $P_i,y_0,y_{n+1}$ | constructed | cumulative masses and endpoint conventions for the atomic staircase | Q20 | pending |
| Q22 | $V$ | arbitrary | mean-zero displacement of a degree-one monotone circle lift used in the periodic-train test | Q15 | pending |
| Q23 | $a$ | constructed | interval-collapse parameter $a=1-t$ in the failed Hardy-strip test | Q16 | pending |

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
| R-JC | completed-scalar energy-scale decomposition in the active fixed-normal support chart | JC_PL | split: JC_SP_EST, JC_CL_RES | split | pending | 4 substantial | 4 analytic | selected |
| R-QFK | quantitative Faber--Krahn localization followed by a near-disk polygonal comparison | T | global class reduces to Fraenkel asymmetry at most \(C_{\mathrm{FK}}/N\) | split | independent-pass | 3 substantial | 3 global | backup |

## Proof DAG

T
JC_PL
JC_SP_EST
JC_SP_SRC
JC_SP_COORD
JC_SP_MATFLUX
JC_CL_RES
JC_CL_PROF
JC_CL_CIRC_RES
JC_CL_RL

| ID | Parents | Statement | Depends on | File | Risk | Status | Audit | Citation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | root | Large-N convex polygonal Polya-Szego theorem with rigidity | JC_PL | parts/00-main-theorem.md | critical | todo | not-started | none |
| JC_PL | T | Uniform nonnegativity of the completed pathwise action on every active no-ratio support chart | JC_SP_EST, JC_CL_RES | parts/10-jc-pl.md | critical | todo | not-started | none |
| JC_SP | JC_PL | superseded by JC_SP_EST and JC_SP_QRCI | Definitions | parts/11-jc-sp.md | critical | stale | superseded | none |
| JC_SP_EST | JC_PL | Uniform natural-energy bound for the exact completed QRCI third-jet identity | JC_SP_SRC | parts/13-jc-sp-est.md | critical | todo | not-started | none |
| JC_SP_QRCI | JC_SP_EST | superseded by JC_SP_REG and JC_SP_LEDGER | Definitions | parts/14-jc-sp-qrci.md | critical | stale | superseded | none |
| JC_SP_LEDGER | JC_SP_EST | superseded by JC_SP_SRC and JC_SP_EST | JC_SP_MATFLUX | parts/16-jc-sp-ledger.md | critical | stale | superseded | none |
| JC_SP_SRC | JC_SP_EST | Exact five-source normal form for the third derivative of the completed scalar | JC_SP_MATFLUX, JC_SP_COORD | parts/25-jc-sp-src.md | critical | todo | not-started | none |
| JC_SP_COORD | JC_SP_SRC | C3 regularity of the completed metric, corrector, quotient, and fan-defect curves on each fixed material ray | Definitions | parts/26-jc-sp-coord.md | critical | proved | local-passed | none |
| JC_SP_REG | JC_SP_SRC | superseded by JC_SP_MATREG | Definitions | parts/15-jc-sp-reg.md | critical | stale | failed | none |
| JC_SP_MATREG | JC_SP_SRC | superseded by JC_SP_MATFLUX | Definitions | parts/17-jc-sp-matreg.md | critical | stale | failed | none |
| JC_SP_MATFLUX | JC_SP_SRC | C3 two-family material spectral, compatible-trace, scalar-conormal, weak-flux, reduced-DtN, and incidence-level corner regularity | Definitions | parts/18-jc-sp-matflux.md | critical | proved | local-passed | none |
| JC_CL | JC_PL | superseded by JC_CL_RES | Definitions | parts/12-jc-cl.md | critical | stale | superseded | none |
| JC_CL_RES | JC_PL | Uniform completed-action lower bound after the all-period gap certificate | JC_CL_PROF | parts/20-jc-cl-res.md | critical | todo | not-started | none |
| JC_CL_GAP | JC_CL_RES | superseded by JC_CL_PROF and JC_CL_CIRC | Definitions | parts/19-jc-cl-gap.md | critical | stale | superseded | none |
| JC_CL_PROF | JC_CL_RES | Uniform closed gap-simplex coercivity after the circle profile inequality | JC_CL_CIRC_RES | parts/22-jc-cl-prof.md | critical | todo | not-started | none |
| JC_CL_CIRC | JC_CL_PROF | superseded by JC_CL_CIRC_RES and JC_CL_RL | Definitions | parts/21-jc-cl-circ.md | critical | stale | superseded | none |
| JC_CL_CIRC_RES | JC_CL_PROF | Uniform circle inverse-displacement coercivity after the real-line profile bound | JC_CL_RL | parts/24-jc-cl-circ-res.md | critical | todo | not-started | none |
| JC_CL_RL | JC_CL_CIRC_RES | Uniform real-line coercivity for zero-mass monotone displacement profiles | Definitions | parts/23-jc-cl-rl.md | critical | proof-draft | pre-proof-passed | none |
