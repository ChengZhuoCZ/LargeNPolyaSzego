"""Exact symbolic calibration checks for the JC_SP pre-proof audit."""

import sympy as sp


def check_full_cell_resummation() -> None:
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


def check_fourth_defect_third_jet() -> None:
    t, a, kappa = sp.symbols("t a kappa", real=True)
    d0, d1, d2 = sp.symbols("d0 d1 d2", real=True)
    directions = (d0, d1, d2)

    defect = sum(
        (t * d) ** 2
        * (6 * a**2 + 4 * a * t * d + (t * d) ** 2)
        for d in directions
    )
    expected = 12 * kappa * (
        a * sum(d**3 for d in directions)
        + t * sum(d**4 for d in directions)
    )
    actual = sp.diff(kappa * defect / 2, t, 3)
    assert sp.expand(actual - expected) == 0


if __name__ == "__main__":
    check_full_cell_resummation()
    check_fourth_defect_third_jet()
    print("JC_SP exact symbolic checks: PASS")
