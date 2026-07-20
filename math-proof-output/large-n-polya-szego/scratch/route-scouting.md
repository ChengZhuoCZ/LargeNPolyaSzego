# Route Scouting

## Scout Header
Scout Mode: conjecture-portfolio
Query Cap: 12
Opened Result Cap: 8
Route Cap: 3
Probe Cap: 4
Decision: split
Selected Route: R-JC
Portfolio Round: 2
Selection rationale: exact analytic certificates kill the Steiner and conformal-order bypasses; verified quantitative disk localization remains a nonselected reserve, while the completed-action probe gives the only selected strict reduction, namely an exhaustive super-near/coarse branch split with boundary regularity, exact-ledger, and estimate interfaces inside the super-near branch.

## Search Lanes
| Lane | Queries | Best hits | Kill signals | Decision effect |
| --- | --- | --- | --- | --- |
| exact-stronger | no public exact-conjecture query; blind exact-\(N\) symmetrization probe | generic parabola-polygon side count | every Steiner symmetral has at least \(2N-4>N\) sides | archive the killed subfamily in route history |
| technique | standard quantitative Faber--Krahn theorem; conformal-operator probe; completed-scalar branch probe | exact disk localization; exact Green-form pullback; exact QRCI and Bregman targets | Loewner order forces congruence; radial \(H^{1/2}\) and pointwise Hessian shortcuts fail | retain R-QFK; kill R-E1; split R-JC |
| obstruction | collapsing side, alternating quotient mode, equal-area order saturation | exact period-three surplus and two exact shortcut obstructions | no counterexample to JC_PL; two child mechanisms remain unproved | keep incompatible backup and select structural split |

## Source Cards
| Source ID | Locator | Claim found | Reliability | Route effect | Linked route | Citation ID | Text verified | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Route Capsules
| Route ID | Family ID | Name | Decision | Core bottleneck | Citation shortcut | Remaining crux | Seed evidence | Proof cost | Citation risk | Hidden hypothesis risk | Certificate risk | Fanout | Kill signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-QFK | F-QFK-LOCALIZATION | quantitative disk localization followed by a near-disk polygonal comparison | backup | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality | none | prove the theorem for competitors with Fraenkel asymmetry at most \(C_{\mathrm{FK}}/N\) | inradius plus quantitative Faber--Krahn => supports | 3 | 2 | 3 | 1 | 2 | none |
| R-E1 | F-CONFORMAL-LOEWNER | conformal weighted-Green Loewner domination | kill | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality | none | operator order is possible only at congruence | equal-area localized form test => refutes | 3 | 2 | 5 | 1 | 1 | equal integrals plus pointwise order force equality |
| R-JC | F-COMPLETED-ACTION | completed-scalar energy-scale decomposition | selected | prove JC_PL on the full active no-ratio chart | none | prove QRCI boundary regularity, the atom-indexed identity, its uniform estimate, and the integrated coarse/nonregular estimate | fixed-domain form calibration, exact resummation, and exact period-three collapse => supports | 4 | 2 | 4 | 2 | 2 | none |

## Probe Ledger
| Probe ID | Route ID | Scout visibility | Aim | Method | Result | Obstruction | Verdict | Probe author | Reviewer | Review model | Review effort | Old obligation | New obligation | Crux reduced | Reduction witness | Outcome map |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P-QFK-1 | R-QFK | blind | test whether disk stability reduces the global comparison | compare the regular polygon with its inball and reserve the standard stability theorem for verification | every strict competitor lies in an \(O(N^{-2})\) spectral window above the disk | no smallest-angle or side-ratio control follows from the exact inradius estimate alone | keep-live | agent:portfolio_blind_a | none | none | none | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality | unchanged | no | none | success=keep-live; failure=defer |
| P-E1 | R-E1 | blind | test weighted-Green operator domination | localize the quadratic-form order and use equality of conformal-weight integrals | domination forces congruence | full Loewner order removes the needed sign cancellation | kill | agent:portfolio_operator_e | none | none | none | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality | unchanged | no | none | success=commit; failure=kill |
| P-QFK-2 | R-QFK | synthesized | verify and strengthen the localization reserve | optimize the exact inradius deficit and apply the primary quantitative Faber--Krahn theorem | every potential counterexample or equality competitor satisfies \(\mathcal A(P)\le C_{\mathrm{FK}}/N\) | Fraenkel closeness still permits microscopic fan modes | keep-live | agent:portfolio_blind_b | none | none | none | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality | prove T for competitors with Fraenkel asymmetry at most C_FK/N | yes | prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality => prove T for competitors with Fraenkel asymmetry at most C_FK/N; axis=locality | success=keep-live; failure=defer |
| P-JC | R-JC | synthesized | test whether the completed action has an exact smaller two-branch core | split at \(E_\alpha(z)=Ka^5\), use a bridge-dependent \(K'\) for the JC_SP_MATFLUX to JC_SP_LEDGER to JC_SP_EST chain, and integrate the coarse corner current before comparison | JC_SP_EST and the coarse-restricted JC_CL form disjoint exhaustive branches and imply JC_PL, while JC_SP_MATFLUX and JC_SP_LEDGER are the typed material-flux and exact-identity prerequisites of JC_SP_EST | scalar/weak flux and incidence-level corner regularity, the atom ledger, its uniform estimate, all-period OB-BC, finite-\(N\) transfer, and nonregular original-path estimate remain unproved | split | agent:portfolio_discrete_f | agent:continuation_reviewer_k | gpt-5.6-sol | xhigh | prove JC_PL on the full active no-ratio chart | prove JC_SP_MATFLUX then JC_SP_LEDGER then JC_SP_EST on the super-near branch and JC_CL on the coarse/far branch | yes | prove JC_PL on the full active no-ratio chart => prove JC_SP_MATFLUX then JC_SP_LEDGER then JC_SP_EST on the super-near branch and JC_CL on the coarse/far branch; axis=regularity | success=split:JC_SP_MATFLUX_JC_SP_LEDGER_JC_SP_EST_JC_CL; failure=switch-route:R-QFK |

## Portfolio Ledger
| Round | Entry ID | Probe ID | Family ID | Role | Concrete artifact | Novelty witness | Merge witness | Dossier | State effect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PE-QFK-1 | P-QFK-1 | F-QFK-LOCALIZATION | blind-initial | equation: exact regular-polygon inradius gives an \(O(N^{-2})\) spectral window | none | none | scratch/crux-dossiers/f-qfk-localization.md#sha256=A459AA68391548CE2A4EFFA0D5C584B0C317A187AE927BD844ED3D501A1EF699 | live |
| 1 | PE-E1 | P-E1 | F-CONFORMAL-LOEWNER | blind-initial | obstruction: equal-area Green-form order forces equality of conformal weights | none | none | scratch/crux-dossiers/f-conformal-loewner.md#sha256=98A83B92BCB5B861EE74EA782338673E59FB416D7343AB99D98D6094520434C0 | kill |
| 2 | PE-QFK-2 | P-QFK-2 | F-QFK-LOCALIZATION | reserve-heartbeat | derivation: quantitative Faber--Krahn and the exact inradius bound give \(\mathcal A(P)\le C_{\mathrm{FK}}/N\) | none | none | scratch/crux-dossiers/f-qfk-localization.md#sha256=A459AA68391548CE2A4EFFA0D5C584B0C317A187AE927BD844ED3D501A1EF699 | live |
| 2 | PE-JC | P-JC | F-COMPLETED-ACTION | targeted | derivation: the \(E_\alpha(z)=Ka^5\) cut gives the exhaustive JC_SP and coarse-restricted JC_CL implication | none | none | scratch/crux-dossiers/f-completed-action-split.md#sha256=B269BB7A5DB8828CF7B8C2948A2DFE20CC3373C740F9FADE9528A46CD05A09F8 | selected |

## Decision
Route decision: split. The selected completed-action family has a strict locality reduction into the JC_SP_MATFLUX to JC_SP_LEDGER to JC_SP_EST super-near chain and the independent JC_CL coarse branch; this is not a proof of any child.
Expansion reason: all pre-commit global bypass candidates with purported one-step certificates were rejected; the exact completed-action case split is the new mechanism family.
Next blueprint action: audit JC_SP_MATFLUX first after the independent A9 continuation review, and preserve R-QFK as a nonselected reserve.
