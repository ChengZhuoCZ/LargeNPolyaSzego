# Crux Dossier

Family ID: F-CONFORMAL-LOEWNER

## Core Obligation

Core bottleneck: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality

This family pulls both polygons conformally to the disk and seeks Loewner
domination of the resulting weighted Green operators.

## D2 Derivation

For a conformal bijection \(f_P:\mathbb D\to P\), put
\(w_P=|f_P'|^2\). With the Dirichlet inner product on
\(H_0^1(\mathbb D)\), define
\[
\langle K_wu,v\rangle_\nabla
=\int_{\mathbb D}w\,u\overline v.
\]
The exact pullback Rayleigh principle gives
\[
\lambda_1(P)^{-1}
=\sup_{u\ne0}
\frac{\int_{\mathbb D}w_P|u|^2}
{\int_{\mathbb D}|\nabla u|^2}
=\|K_{w_P}\|.
\]
Suppose the proposed certificate \(K_{w_P}\preceq K_{w_R}\) held.
Testing on every \(u\in C_c^\infty(\mathbb D)\) yields
\[
\int_{\mathbb D}(w_R-w_P)|u|^2\ge0.
\]
Shrinking the support of \(u\) around Lebesgue points gives
\(w_P\le w_R\) almost everywhere. The conformal area formula and the
fixed-area hypothesis give
\[
\int_{\mathbb D}w_P=|P|=|R|=\int_{\mathbb D}w_R,
\]
so \(w_P=w_R\) almost everywhere. Since the conformal derivatives do not
vanish, \(f_P'/f_R'\) is analytic and has constant modulus one. It is constant,
so \(f_P=cf_R+b\), with \(|c|=1\), and \(P\) is congruent to \(R\).

The obstruction is independent of \(N\), the conformal gauge, fan ratios, or
collapsing sides. It acts already on compactly supported test functions and
therefore does not require boundary regularity.

## Reduction Witness

Reduction witness: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality => prove conformal weighted-Green Loewner domination; axis=dependency

The proposed operator statement is a single smaller sufficient obligation, but
the D2 calculation proves it false for every noncongruent equal-area pair.

## Falsification

A norm-only comparison \(\|K_{w_P}\|\le\|K_{w_R}\|\) is weaker and is not
refuted by pointwise localization, but it would need sign-changing
cancellations absent from Loewner order. No such successor estimate is
produced by this family.

## Verdict

Verdict: kill. Conformal Loewner domination collapses to equality.
