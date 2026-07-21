# JC_SP_SRC: Completed Third-Source Normal Form

## Local Summary
- Statement: Exact five-source normal form for the third derivative of the completed scalar
- Dependencies: JC_SP_MATFLUX, JC_SP_COORD
- Current obstruction: JC_SP_COORD must justify the three finite-dimensional C3 source curves.
- Proof status: todo
- Next action: prove JC_SP_COORD, then rerun both independent proof audits
- Local Context Packet: this statement + Definitions' exact completed scalar + the proved JC_SP_MATFLUX C3 material regularity; no endpoint atom partition or uniform estimate is imported.

## Statement

Fix the quantifiers and one completed ray from JC_SP_MATFLUX. Put
\[
\alpha_t=\alpha_*+td,
\qquad
Y_t=h_{\alpha_t}\mathbf1+J_{\alpha_t}(c_{\alpha_t}+tw),
\qquad
B_t=h_{\alpha_t}\mathbf1,
\]
\[
C_t=J_{\alpha_t}c_{\alpha_t},
\qquad
W_t=tJ_{\alpha_t}w.
\]
For the completed scalar, use only the third directional derivative along
this fixed ray,
\[
\partial_q^3\mathbf A_N(tq)
:=\left.\frac{d^3}{ds^3}\right|_{s=0}
\mathbf A_N((t+s)d,(t+s)w).
\tag{SRC-1}
\]
The finite typed source set is
\[
\mathscr S_N={\mathrm{specY},\mathrm{specB},
\mathrm{metricC},\mathrm{metricW},\mathrm{fan}},
\]
with
\[
\begin{aligned}
Q_{\mathrm{specY}}(t;q)
&=\frac{d^3}{dt^3}\Phi_{\alpha_t}(Y_t),\\
Q_{\mathrm{specB}}(t;q)
&=-\frac{d^3}{dt^3}\Phi_{\alpha_t}(B_t),\\
Q_{\mathrm{metricC}}(t;q)
&=\frac{d^3}{dt^3}\mathcal G^{\mathrm{JP}}_{\alpha_t}(C_t),\\
Q_{\mathrm{metricW}}(t;q)
&=-\frac12\frac{d^3}{dt^3}
\mathcal G^{\mathrm{JP}}_{\alpha_t}(W_t),\\
Q_{\mathrm{fan}}(t;q)
&=\frac\kappa2\frac{d^3}{dt^3}\mathcal J_4(\alpha_t).
\end{aligned}
\tag{SRC-2}
\]
Then every term is well-defined and
\[
\boxed{
\partial_q^3\mathbf A_N(tq)
=\frac{d^3}{dt^3}\mathbf A_N(td,tw)
=\sum_{s\in\mathscr S_N}Q_s(t;q).
}
\tag{SRC}
\]

The two spectral sources in (SRC-2) are derivatives of the complete polygon
scalars. Thus any terminal sector and its annular complement remain combined
inside the same full-domain scalar before differentiation. The statement
does not assert a noncanonical endpoint atomization and contains no estimate.

## Dependencies

- JC_SP_MATFLUX supplies C3 material dependence of the two polygon spectral
  scalars along the fixed completed ray.
- JC_SP_COORD supplies C3 dependence of the two moving-metric scalars and the
  fan-defect scalar.
- Definitions supplies the exact scalar $\mathbf A_N$ and the four curves above.

## Proof Strategy
Status: done
- Plan: Kind: mechanism -- substitute the five summands of the exact completed scalar and use linearity of the ordinary third derivative without expanding either full polygon scalar into artificial endpoint pieces.
- Key obstacle: none beyond checking C3 regularity of the five scalar curves.
- Needed dependencies: exactly the two dependencies listed above.
- Failure trigger: interface mismatch if one source curve is not C3 in the topology declared by JC_SP_MATFLUX; statement likely false if direct differentiation of the exact scalar produces a sixth source.

## Experiments and Edge Cases
Status: done

### Check 1: gauge-reallocation invariance
- Model: an analytic redistribution between one terminal power and its annular complement that leaves the full polygon scalar unchanged.
- Method: differentiate only the complete spectral source in (SRC-2).
- Result: the source is unchanged because its definition uses the full scalar rather than either artificial component.
- Interpretation: supports; this removes the noninvariant ownership ambiguity of the stale JC_SP_LEDGER statement.

## Counterexample Search
Status: done

The five-source list was compared term by term with the five summands in the
definition of $\mathbf A_N$. No additional scalar source exists. Endpoint,
ground-state, reduced-DtN, and material-flux terms are descendants generated
inside $Q_{\mathrm{specY}}$ and $Q_{\mathrm{specB}}$, not new summands of the
completed scalar.

## Proof
Status: done

<!-- math-proof-ledger: {"object":"f_q","kind":"local-only","depends_on":["Q8"],"reason":"one-variable restriction of the completed scalar along the fixed proof ray"} -->

Set $f_q(t)=\mathbf A_N(td,tw)$. Substitution of the completed-coordinate
curves into the definition of the exact completed scalar gives the scalar
identity
\[
\begin{aligned}
f_q(t)={}&
\Phi_{\alpha_t}(Y_t)-\Phi_{\alpha_t}(B_t)
+\mathcal G^{\mathrm{JP}}_{\alpha_t}(C_t)
-\frac12\mathcal G^{\mathrm{JP}}_{\alpha_t}(W_t)
+\frac\kappa2\mathcal J_4(\alpha_t).
\end{aligned}
\tag{15}
\]
This equality is taken before any localization of a corner sector. In
particular, the first and second terms in (15) are the two complete polygon
spectral scalars rather than sums of terminal and complementary pieces.

JC_SP_MATFLUX proves that the two spectral curves in (15) are C3 on the
fixed closed material ray. The completed-coordinate definitions give the
same regularity for the two finite-dimensional moving-metric curves and the
fan-defect curve. Hence every ordinary third derivative in (SRC-2) exists.
Taking three derivatives of (15) and using linearity gives
\[
f_q'''(t)=
Q_{\mathrm{specY}}+Q_{\mathrm{specB}}
+Q_{\mathrm{metricC}}+Q_{\mathrm{metricW}}+Q_{\mathrm{fan}}.
\tag{16}
\]
Finally, by the definition (SRC-1),
\[
\partial_q^3\mathbf A_N(tq)
=\left.\frac{d^3}{ds^3}\right|_{s=0}f_q(t+s)
=f_q'''(t).
\]
Combining this identity with (16) proves (SRC).

## Proof Attempt Log
Active attempt: completed by direct differentiation of the exact scalar
Recent failed attempt: none
Superseded attempts: JC_SP_LEDGER used undefined ownership categories and was not falsifiable.

## Local Audit
Status: done

- Independent claim-audit verdict: correct.
- Correction applied: JC_SP_MATFLUX proves C3 dependence along each fixed
  material ray, not ambient Frechet C3 of the two-variable scalar. Therefore
  (SRC-1)--(SRC-2) use ordinary third derivatives of the five scalar curves.
- Sign check: every source retains its outer sign from the definition of
  $\mathbf A_N$; three differentiations introduce no additional sign.
- Scope check: no endpoint atom partition or quantitative estimate is claimed.
- First final proof audit: fail; the algebra passed, but the allowed
  dependencies did not prove the metric/corrector/fan C3 source curves.
- Second final proof audit: fail for the same single interface gap.
- Repair criterion: prove JC_SP_COORD, add it as a dependency, and rerun both
  final audits without altering the five-source algebra.
