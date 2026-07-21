# Legacy revision-24 proof module index

This directory is retained migration evidence. It is conditional on `JC-PL`,
is not part of the active `math-proof` workspace, and must not be cited as an
unconditional proof.

`conditional-proof.tex` is the only LaTeX entry point. It loads `preamble.tex`
and the following modules in topological reading order.

| Order | Module file | DAG role | Direct assembly dependencies |
|---:|---|---|---|
| 01 | `01-f51-disk-hessian.tex` | F51: exact disk Hessian | none |
| 02 | `02-h0-homogeneous-gap.tex` | H0: homogeneous gap | none |
| 03 | `03-f65-disk-endpoint.tex` | F65: angular disk endpoint | F51, H0 |
| 04 | `04-f129-source-envelope.tex` | F129: disk-source envelope | F51 |
| 05 | `05-tr-physical-trace.tex` | TR: physical trace transfer | F51, F65, F129 |
| 06 | `06-ct-cubic-tensor.tex` | CT: complete cubic tensor | F51 |
| 07 | `07-qb-bubble-reduction.tex` | QB: quadratic-bubble reduction | F51, TR, CT |
| 08 | `08-f144-midpoint-identity.tex` | F144: midpoint identity | none |
| 09 | `09-f148-material-matrix.tex` | F148: material matrix | F144 |
| 10 | `10-df0a-intrinsic-variance.tex` | DF0A: intrinsic variance | F144 |
| 11 | `11-df0b-good-grid.tex` | DF0B: comparable-grid square | F148 |
| 12 | `12-zg-zero-gap.tex` | ZG: zero-gap source decomposition | F144, DF0A, DF0B |
| 13 | `13-pt-material-transport.tex` | PT/DM: mixed material row | F51, CT |
| 14 | `14-jp-joint-principal.tex` | JP: exact support Hessian and disk endpoint | TR, CT, QB, ZG, PT |
| 15 | `15-jc-joint-comparison.tex` | JC: completed action and open JC-PL frontier | JP |
| 16 | `16-nr-assembly.tex` | NR/J0 handoff | JC |
| 17 | `17-f57-side-mass-moment.tex` | F57: stationary side moments | none |
| 18 | `18-a0-side-activation.tex` | A0: strict side activation | F57 |
| 19 | `19-g0-global-assembly.tex` | G0/MAIN: global conditional assembly | NR, F57, A0 |

Every local label/reference is namespaced by the stable module ID. Keep the
numeric filename prefix separate from that namespace.
