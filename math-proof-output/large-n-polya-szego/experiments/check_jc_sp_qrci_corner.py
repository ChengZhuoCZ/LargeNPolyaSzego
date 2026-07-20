"""Exact Stage 4 calibration for the JC_SP_QRCI regularity interface."""

import math

import sympy as sp


def check_corner_log_moments() -> None:
    p = sp.symbols("p", positive=True)
    base = 1 / p
    for order in range(7):
        moment = (-1) ** order * sp.diff(base, p, order)
        expected = sp.factorial(order) / p ** (order + 1)
        assert sp.simplify(moment - expected) == 0

    # Convex polygon corners have beta > 1.  The worst third material
    # derivative produces at most log(r)^3, whose squared gradient uses
    # the order-six moment with p = 2 beta.
    beta = sp.symbols("beta", positive=True)
    worst = sp.factorial(6) / (2 * beta) ** 7
    assert sp.simplify(worst.subs(beta, 1) - sp.Rational(45, 8)) == 0


def check_piecewise_affine_pullback() -> None:
    t = sp.symbols("t", real=True)
    h11, h12, h21, h22 = sp.symbols("h11 h12 h21 h22", real=True)
    deformation = sp.eye(2) + t * sp.Matrix([[h11, h12], [h21, h22]])
    determinant = sp.factor(deformation.det())
    coefficient = sp.simplify(
        determinant * deformation.inv() * deformation.inv().T
    )

    for entry in coefficient:
        third = sp.factor(sp.diff(entry, t, 3))
        denominator = sp.denom(sp.cancel(third))
        # Every possible pole is a power of the affine Jacobian.  Thus a
        # nondegenerate material triangle gives C^3 coefficients.
        assert sp.rem(denominator, determinant, t) == 0 or denominator == 1


def check_terminal_complement() -> None:
    t = sp.symbols("t", real=True)
    amplitude = sp.Function("A")(t)
    exponent = sp.Function("beta")(t)
    cutoff = sp.Function("theta")(t)
    coefficient = sp.Function("K")(exponent)
    terminal = amplitude**2 * cutoff ** (2 * exponent) * coefficient
    complement = (
        amplitude**2
        * (1 - cutoff ** (2 * exponent))
        * coefficient
    )
    full_cell = amplitude**2 * coefficient
    residual = sp.simplify(terminal + complement - full_cell)
    assert residual == 0
    assert sp.simplify(sp.diff(residual, t, 3)) == 0


if __name__ == "__main__":
    check_corner_log_moments()
    check_piecewise_affine_pullback()
    check_terminal_complement()
    print("JC_SP_QRCI corner/material checks: PASS")
