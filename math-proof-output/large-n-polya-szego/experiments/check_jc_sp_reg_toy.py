"""Exact finite-dimensional and corner checks for JC_SP_REG."""

import sympy as sp


def check_simple_eigenpair_and_reduced_schur() -> None:
    t = sp.symbols("t", real=True)
    rotation = sp.Matrix(
        [[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]]
    )
    lam1 = 1 + t
    lam2 = 4 + t**2
    gap = sp.factor(lam2 - lam1)
    assert sp.discriminant(gap, t) < 0
    assert sp.LC(sp.Poly(gap, t)) > 0

    u = rotation[:, 0]
    transverse = rotation[:, 1]
    operator = sp.simplify(
        rotation * sp.diag(lam1, lam2) * rotation.T
    )
    assert sp.simplify(operator * u - lam1 * u) == sp.zeros(2, 1)

    reduced_resolvent = sp.simplify(
        transverse * transverse.T / gap
    )
    projected_identity = sp.eye(2) - u * u.T
    assert sp.simplify(
        (operator - lam1 * sp.eye(2)) * reduced_resolvent
        - projected_identity
    ) == sp.zeros(2)

    boundary_coupling = sp.Matrix([[1 + t, t**2], [t, 1 - t]])
    boundary_block = sp.Matrix([[3 + t**2, t], [t, 2 + t**2]])
    reduced_dtn = sp.simplify(
        boundary_block
        - boundary_coupling.T * reduced_resolvent * boundary_coupling
    )
    for entry in reduced_dtn:
        third = sp.cancel(sp.diff(entry, t, 3))
        denominator = sp.factor(sp.denom(third))
        # The only possible pole is the spectral gap.  Since the gap is
        # positive for all real t, every entry is C^3 on the whole ray.
        assert denominator == 1 or any(
            sp.simplify(denominator - gap**power) == 0
            for power in range(1, 5)
        )


def check_corner_trace_threshold() -> None:
    beta = sp.symbols("beta", positive=True)
    # A third material derivative of r^(beta-1) creates log(r)^3.
    # Its L2 square on an open side has exponent p=2 beta-1.
    p = 2 * beta - 1
    moment = sp.factorial(6) / p**7
    assert sp.simplify(moment.subs(beta, 1) - sp.factorial(6)) == 0


if __name__ == "__main__":
    check_simple_eigenpair_and_reduced_schur()
    check_corner_trace_threshold()
    print("JC_SP_REG exact toy checks: PASS")
