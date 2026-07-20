# Crux Dossier

Family ID: F-CELLWISE-SDP

## Core Obligation

Core bottleneck: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality

The proposed reduction sought a cellwise semidefinite certificate after a
radial piecewise-affine pullback.

## D2 Derivation

For a radial map \(F:R_N(A)\to P\), let
\[
M_i=DF|_{T_i},\qquad J_i=\det M_i,\qquad
C_i=J_iM_i^{-1}M_i^{-T}.
\]
Exact change of variables gives
\[
\int_P(|\nabla u|^2-\lambda_Ru^2)
=\sum_i\int_{T_i}
\bigl(\nabla v^TC_i\nabla v-\lambda_RJ_iv^2\bigr),
\qquad v=u\circ F.
\]
The proposed inequalities \(C_i\succeq\gamma I\) and \(J_i\le\gamma\)
would reduce the result to the comparator Poincaré inequality. But
\[
\det C_i=1,\qquad \frac1N\sum_iJ_i=1.
\]
The matrix bound implies \(\gamma\le1\); the scalar bounds and their mean-one
identity then force \(J_i=\gamma=1\). Thus \(C_i=I\) and each
\(M_i\in SO(2)\). Continuity across shared radial edges forces all rotations
to coincide, so \(P\) is congruent to the comparator.

## Reduction Witness

Reduction witness: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality => prove cellwise pullback semidefinite domination; axis=certificate

The finite certificate would be smaller and sufficient, but it is feasible
only at equality.

## Falsification

Any viable pullback certificate must retain nonlocal coupling among cells or
an exact Schur complement. Purely cellwise domination is algebraically
impossible off the congruence class.

## Verdict

Verdict: kill. The cellwise SDP certifies only equality.
