# Crux Dossier

Family ID: F-QFK-LOCALIZATION

## Core Obligation

Core bottleneck: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality

This family first eliminates competitors outside a shrinking near-disk class and
then seeks a uniform polygonal comparison inside that class.

## D2 Derivation

Let \(B_A\) be the area-\(A\) disk and put \(x_N=\pi/N\). The regular
\(N\)-gon of area \(A\) has inradius
\[
\rho_N^2=\frac{A}{N\tan x_N}.
\]
Since \(B_{\rho_N}\subset R_N(A)\), domain monotonicity gives
\[
0\le
\frac{\lambda_1(R_N(A))}{\lambda_1(B_A)}-1
\le q_N:=\frac{\tan x_N}{x_N}-1.
\]
Moreover,
\[
q_N\le \frac{9(3\sqrt3/\pi-1)}{N^2}.
\]
Indeed \(h(x)=(\tan x-x)/x^3\) is increasing on \((0,\pi/3]\).
The monotonicity of \(\tan t/t\) yields
\(\tan^2t\le(t/x)^2\tan^2x\), hence
\(\int_0^x\tan^2t\,dt\le x\tan^2x/3\) and \(h'(x)\ge0\).
Thus \(N^2q_N=\pi^2h(\pi/N)\) is maximal at \(N=3\).

The sharp quantitative Faber--Krahn theorem of Brasco, De Philippis, and
Velichkov states in dimension two that there is
\(\sigma_{\mathrm{FK}}>0\) such that every finite-measure open set satisfies
\[
|\Omega|\lambda_1(\Omega)-|B|\lambda_1(B)
\ge \sigma_{\mathrm{FK}}\mathcal A(\Omega)^2,
\]
where \(B\) has the same area and \(\mathcal A\) is Fraenkel asymmetry.
The primary paper states this for every open set of finite measure, so convex
polygons are included and no side-ratio hypothesis is imported.

Every potential counterexample or equality competitor satisfying
\(\lambda_1(P)\le\lambda_1(R_N(A))\) therefore obeys
\[
\mathcal A(P)^2
\le \frac{A\lambda_1(B_A)}{\sigma_{\mathrm{FK}}}\,q_N
\le \frac{C_{\mathrm{FK}}^2}{N^2}.
\]
Consequently all polygons with
\(\mathcal A(P)>C_{\mathrm{FK}}/N\) are eliminated.

## Reduction Witness

Reduction witness: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality => prove T for competitors with Fraenkel asymmetry at most C_FK/N; axis=locality

This is a proper quantifier-domain reduction of the global theorem. It is not a
reduction of JC_PL: Fraenkel closeness does not bound the smallest fan angle
or adjacent side ratios.

## Falsification

The localization survives scaling and collapsing-side sequences, but it does
not imply the no-ratio support-chart controls required by the completed action.
Thus it eliminates the far Fraenkel region without proving the remaining
near-disk comparison. The cited theorem and its hypotheses were checked
directly in the primary paper's Main Theorem, equation (1.9).

## Verdict

Verdict: keep-live as a nonselected global localization reserve.
