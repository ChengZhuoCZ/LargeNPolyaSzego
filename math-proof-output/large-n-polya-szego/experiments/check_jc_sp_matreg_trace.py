"""Exact Stage 4 type and endpoint checks for JC_SP_MATREG."""

import sympy as sp


def check_cross_edge_trace_obstruction() -> None:
    eps = sp.symbols("eps", positive=True)
    # Two constant edge values, 1 and 0, have zero separate edge seminorms.
    # Across the common vertex their truncated cross term is exact:
    truncated = 2 * sp.log(1 + eps) - sp.log(4 * eps)
    assert sp.limit(truncated, eps, 0, dir="+") == sp.oo


def check_common_jump_coordinates() -> None:
    transform = sp.Matrix(
        [[sp.Rational(1, 2), sp.Rational(1, 2)], [1, -1]]
    )
    assert transform.det() == -1
    assert transform.inv() == sp.Matrix(
        [[1, sp.Rational(1, 2)], [1, -sp.Rational(1, 2)]]
    )


def check_scalar_and_flux_pullbacks() -> None:
    rho, beta, e, r0 = sp.symbols(
        "rho beta e r0", positive=True
    )
    rt = rho * r0
    physical = e * rt ** (beta - 1)
    scalar_material = sp.simplify(physical)
    flux_material = sp.simplify(rho * physical)
    assert sp.simplify(
        scalar_material - e * rho ** (beta - 1) * r0 ** (beta - 1)
    ) == 0
    assert sp.simplify(
        flux_material - e * rho**beta * r0 ** (beta - 1)
    ) == 0


def check_endpoint_profile_derivatives() -> None:
    r, t = sp.symbols("r t", positive=True)
    b0, b1, b2, b3 = sp.symbols("b0 b1 b2 b3", real=True)
    beta = b0 + b1 * t + b2 * t**2 / 2 + b3 * t**3 / 6
    profile = r ** (beta - 1)
    third_at_zero = sp.expand(sp.diff(profile, t, 3).subs(t, 0))
    expected = r ** (b0 - 1) * (
        b3 * sp.log(r)
        + 3 * b1 * b2 * sp.log(r) ** 2
        + b1**3 * sp.log(r) ** 3
    )
    assert sp.simplify(third_at_zero - expected) == 0

    gamma = sp.symbols("gamma", positive=True)
    k = sp.symbols("k", integer=True, positive=True)
    for order in range(4):
        term = 2 ** (-2 * gamma * k) * (1 + k) ** (2 * order)
        ratio = sp.simplify(term.subs(k, k + 1) / term)
        assert sp.simplify(
            sp.limit(ratio, k, sp.oo) - 2 ** (-2 * gamma)
        ) == 0


if __name__ == "__main__":
    check_cross_edge_trace_obstruction()
    check_common_jump_coordinates()
    check_scalar_and_flux_pullbacks()
    check_endpoint_profile_derivatives()
    print("JC_SP_MATREG trace/endpoint checks: PASS")
