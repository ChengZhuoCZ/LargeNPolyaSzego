# JC_SP_LEDGER: Atom-Indexed Full-Cell Identity (Stale)

## Local Summary
- Statement: superseded by JC_SP_SRC and JC_SP_EST
- Dependencies: JC_SP_MATFLUX
- Current obstruction: the ownership categories were never defined as mathematical predicates.
- Proof status: todo
- Next action: use the replacement five-source normal form JC_SP_SRC
- Local Context Packet: this statement + proved JC_SP_MATFLUX material scalar/flux data + completed scalar + exact terminal/complement cancellation + PSF-04, PSF-05, and PSF-07; no uniform bound is part of this row.

## Statement
Under JC_SP_MATFLUX, for every finite-bridge ray \(q\) there is a finite atom set
\(\mathscr I_N\), an explicitly listed family of scalar atoms
\(\{\mathfrak q_\xi(t;q)\}_{\xi\in\mathscr I_N}\), and an ownership map
\[
\operatorname{own}:\mathscr I_N\longrightarrow
\{\mathrm{full\mbox{-}cell},\mathrm{endpoint},\mathrm{pair},
\mathrm{ground\mbox{-}state},\mathrm{metric},\mathrm{gauge},
\mathrm{area},\mathrm{base},\mathrm{lower},\mathrm{fan}\}
\]
such that, for \(0\le t\le1\),
\[
D^3\mathbf A_N(tq)[q,q,q]
=\sum_{\xi\in\mathscr I_N}\mathfrak q_\xi(t;q)
=:\mathfrak Q_N(t;q).
\]
The atom list and formulas must be written term by term and satisfy:

1. terminal two-ray and annular-complement atoms combine to the full-cell
   amplitude before any estimate;
2. endpoint/nonendpoint and same-cell/adjacent/first-separation pair indices
   are disjoint and exhaust their exact source sums;
3. the differentiated moving ground state, reduced-DtN, area, fixed-rank,
   quotient, corrector, metric, base-subtraction, lower, and fan rows are each
   the image of exactly one source term under the ownership map; and
4. summing the atoms reproduces the third chain-rule derivative of the exact
   completed scalar, with no omitted or duplicated distribution.

This row asserts only the finite identity. JC_SP_EST owns every quantitative
bound for \(\mathfrak Q_N\).

## Dependencies

- JC_SP_MATFLUX supplies the two-family third material scalar-conormal,
  weak-flux, leading-corner, compatible-trace, and reduced-DtN derivatives.
  This row owns the explicit
  Eulerian pushforward and every endpoint distribution used by its atom list.
- Definitions supplies \(\mathbf A_N\) and the completed material ray.

## Proof Strategy
Status: todo
- Plan: Kind: mechanism — differentiate the exact completed scalar in the common material chart, assign each resulting source descendant to a unique atom, recombine terminal/complement atoms, and prove coverage by an inverse ownership map back to the undifferentiated source.
- Key obstacle: separate corner and full-vector ledgers have historically omitted moving source/trace derivatives or duplicated endpoint contributions.
- Needed dependencies: the complete JC_SP_MATFLUX derivative package and the exact scalar normal form.
- Failure trigger: interface mismatch if an atom has no unique source owner or a source descendant has no atom; statement likely false if the summed ledger differs from a direct third material derivative.

## Experiments and Edge Cases
Status: todo

### Check 1: one-channel ownership calibration
- Model: one terminal corner power and its exact annular complement.
- Method: PSF-04, PSF-05, and PSF-07; differentiate their sum symbolically and compare it with the derivative after full-cell recombination.
- Result: the residual is identically zero through third order, so this two-atom ownership block is exact.
- Interpretation: supports one ownership block but is inconclusive for the complete ledger; next action audit all source descendants after JC_SP_REG closes.

## Counterexample Search
Status: todo

Search for a source descendant with two owners, no owner, or an endpoint
distribution whose pairing is absent from the finite atom set.

## Proof
Status: todo

No proof is claimed.

## Proof Attempt Log
Active attempt: none
Recent failed attempt: none
Superseded attempts: none

## Local Audit
Status: todo

## Route Correction

Trigger: an independent Stage 4 claim audit returned split.

Failure: Definitions and JC_SP_MATFLUX define the completed scalar and its
typed material derivatives, but do not define the proposed terminal,
complement, endpoint, pair, ground-state, metric, gauge, area, base, lower,
and fan ownership predicates. The existential atom statement was therefore
not falsifiable: one could always call the entire derivative one atom.

Failure type: interface mismatch.

Replacement: JC_SP_SRC gives a finite, formula-defined five-source normal
form directly from the exact completed scalar. JC_SP_EST owns every later
full-cell/endpoint resummation needed for the uniform estimate.

Stale Scope: JC_SP_LEDGER only; JC_SP_EST is rewired to JC_SP_SRC.
