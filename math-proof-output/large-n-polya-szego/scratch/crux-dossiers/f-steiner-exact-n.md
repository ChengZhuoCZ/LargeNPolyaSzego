# Crux Dossier

Family ID: F-STEINER-EXACT-N

## Core Obligation

Core bottleneck: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality

The proposed reduction was an exact-\(N\)-side-preserving strict Steiner
descent followed by iteration to the regular polygon.

## D2 Derivation

For \(N\ge5\), take
\[
P_N=\operatorname{conv}\{v_j=(2^j,4^j):0\le j<N\}
\]
and rescale it to the prescribed area. All points are genuine vertices because
they lie on the strictly convex parabola \(y=x^2\). Every chord has slope
\[
\frac{4^j-4^i}{2^j-2^i}=2^i+2^j.
\]
Binary uniqueness shows that distinct unordered vertex pairs have distinct
chord directions. For every projection axis, therefore, at most one pair of
vertices has the same projection.

In fiber coordinates write
\[
P_N=\{(s,t):g(s)<t<f(s)\},\qquad w(s)=f(s)-g(s).
\]
Every distinct internal projected vertex gives a strict downward jump of the
derivative of the concave piecewise-affine width \(w\). Its Steiner symmetral is
\[
S_\ell P_N=\{(s,t):|t|<w(s)/2\}.
\]
If all \(N\) vertex projections are distinct, the \(N-2\) internal
breakpoints give \(N-1\) affine segments on each of the two graphs
\(t=\pm w(s)/2\), hence \(2N-2\) sides. One internal projection collision
deletes one breakpoint on each graph and gives \(2N-4\) sides. If the sole
collision occurs at an extreme support fiber, the two vanishing endpoints are
replaced by one vertical side, giving \(2N-3\) sides. These cases exhaust all
axes because two chord-direction collisions are impossible. Thus
\[
\#\operatorname{Sides}(S_\ell P_N)\ge2N-4>N
\]
for every axis and every \(N\ge5\). Scaling changes none of these incidence
counts.

To see that the displayed points really form the advertised comparison
family, order them by increasing first coordinate. Strict convexity implies
that each intermediate point lies strictly below the chord joining any two
points on opposite sides of it, so every \(v_j\) is exposed by a supporting
line and no side is collinear with its neighbor. The polygon is therefore
convex with exactly \(N\) genuine sides before symmetrization. If two vertices
had the same projection, the projection axis would be perpendicular to their
chord. The binary formula for the chord slope shows that a second colliding
pair would require \(2^i+2^j=2^k+2^\ell\), which forces the unordered pairs to
coincide. Hence the three breakpoint counts above cover every possible
symmetrization axis, including axes parallel to an extreme edge. The
counterexample is thus uniform over the continuum of choices in the proposed
descent lemma, not merely a generic-axis calculation.

## Reduction Witness

Reduction witness: prove T without JC_PL, preserving fixed area, exactly N genuine sides, and equality => prove an exact-N-side-preserving strict Steiner descent lemma; axis=finiteness

The proposed child would be sufficient by iteration and is strictly smaller,
but the D2 calculation proves it false.

## Falsification

The first admissibility clause fails before spectral monotonicity or rigidity
is used: a generic convex \(N\)-gon has no Steiner axis whose symmetral remains
an \(N\)-gon. Allowing more intermediate sides would require a different
mechanism that returns to the exact-\(N\) comparison class.

## Verdict

Verdict: kill. The exact-\(N\)-side-preserving Steiner family is false.
