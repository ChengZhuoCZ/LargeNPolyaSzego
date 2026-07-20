# Crux Dossier

Family ID: F-QRCI-MATERIAL-FLUX

## Core Obligation

Freeze the exact pullback convention for strong scalar conormal traces and
weak conormal flux densities before defining endpoint coefficients.

## Exact First Failure

On an incident side let \(r_0=\ell_0s\), \(r_t=\ell_ts\), and
\(\rho=\ell_t/\ell_0\).  If the physical corner trace is
\(\partial_{\nu_t}u_t\sim\pm e(t)r_t^{\beta(t)-1}\), then the scalar material
pullback has coefficient \(e(t)\rho^{\beta(t)-1}\), while the weak flux-density
pullback includes the boundary Jacobian and has coefficient
\(e(t)\rho^{\beta(t)}\).  JC_SP_MATREG subtracted
\(e(t)r_0^{\beta(t)-1}\) without choosing either convention.  Moreover the two
incident side-length ratios can differ, so one endpoint coefficient per vertex
and branch is insufficient in fixed side coordinates.

## Minimal Repair

Define both pullbacks and their exact boundary-Jacobian relation.  Keep the
single physical sector amplitude \(c_i^\varepsilon\) and
\(e_i^\varepsilon=\beta_i c_i^\varepsilon\), but define scalar material
endpoint coefficients
\[
\widehat e_{i,\sigma}^\varepsilon
=e_i^\varepsilon(\rho_{i,\sigma}^\varepsilon)^{\beta_i-1},
\qquad \sigma\in\{-,+\}.
\]
Take average/difference across the \(Y/B\) families for every incident side.
Thus the endpoint block is \(\mathbb R_E^{4N}\), not
\(\mathbb R_E^{2N}\).  The weak flux coefficient is then
\(\rho_{i,\sigma}^\varepsilon\widehat e_{i,\sigma}^\varepsilon\).

## Reduction Witness

This is a local coordinate repair.  It changes no hypothesis, completed
scalar, derivative order, branch split, or estimate.  It makes the exact
material data imported by JC_SP_LEDGER typed and invertible.

## Verdict

Verdict: replace JC_SP_MATREG by JC_SP_MATFLUX and re-audit the corrected
strong/weak endpoint convention.

