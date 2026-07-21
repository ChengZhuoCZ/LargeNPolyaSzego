"""Deterministic Stage-4 falsification scan for the JC_CL gap simplex.

This is deliberately a floating-point candidate search.  It is not a proof
of the all-period lower bound.  The period-three value is checked against its
known exact ratio 10/13 as a normalization guard.
"""

from __future__ import annotations

import math
import random
import sys

import mpmath as mp
import numpy as np


SEED = 20260721
QUAD_ORDER = 256


def q_symbol(x: float) -> float:
    xx = mp.mpf(x)
    return float(
        2
        * mp.sin(mp.pi * xx) ** 4
        / mp.pi**3
        * (mp.zeta(3, xx) + mp.zeta(3, 1 - xx))
    )


def gaps_from_u(u: np.ndarray) -> np.ndarray:
    v = np.roll(u, -1) - u
    return 1.0 + v - np.roll(v, 1)


def u_from_gaps(g: np.ndarray) -> np.ndarray:
    """Solve g_i = 1 + v_i-v_{i-1}, v_i=u_{i+1}-u_i, with mean u=0."""
    p = len(g)
    lap = np.zeros((p, p), dtype=float)
    for i in range(p):
        lap[i, i] = -2.0
        lap[i, (i - 1) % p] += 1.0
        lap[i, (i + 1) % p] += 1.0
    # g-1 = u_{i+1}-2u_i+u_{i-1}; replace one singular row by the gauge.
    rhs = g.astype(float) - 1.0
    matrix = lap.copy()
    matrix[-1, :] = 1.0
    rhs[-1] = 0.0
    return np.linalg.solve(matrix, rhs)


_nodes, _weights = np.polynomial.legendre.leggauss(QUAD_ORDER)
_times = 0.5 * (_nodes + 1.0)
_time_weights = 0.5 * _weights * (1.0 - _times)


def leading_ratio(u: np.ndarray) -> float:
    """Return 2*pi*(S_p(1)-S_p(0))/Q_p[u] by the pair ledger."""
    p = len(u)
    v = np.roll(u, -1) - u
    s_second_integral = 0.0
    for i in range(p):
        for j in range(p):
            dv = v[i] - v[j]
            if abs(dv) < 1.0e-15:
                continue
            phase = math.pi * ((i - j) + _times * dv) / p
            log_kernel = np.log(np.maximum(np.abs(2.0 * np.sin(phase)), 1.0e-300))
            s_second_integral += dv * dv * float(np.dot(_time_weights, log_kernel))
    s_difference = s_second_integral / (math.pi * p)

    uhat = np.fft.fft(u) / p
    q_value = 0.0
    for k in range(1, p):
        q_value += abs(uhat[k]) ** 2 * q_symbol(k / p)
    q_value *= 2.0 * math.pi
    if q_value <= 1.0e-24:
        return math.nan
    return 2.0 * math.pi * s_difference / q_value


def exact_models() -> list[tuple[str, float, float]]:
    models: list[tuple[str, np.ndarray, float]] = [
        ("p2_boundary", np.array([0.25, -0.25]), math.nan),
        ("p3_collapse", np.array([1.0 / 3.0, -1.0 / 6.0, -1.0 / 6.0]), 10.0 / 13.0),
        ("p4_alternating_boundary", np.array([0.25, -0.25, 0.25, -0.25]), math.nan),
    ]
    return [(name, leading_ratio(u), expected) for name, u, expected in models]


def random_scan() -> list[tuple[int, float, list[float]]]:
    rng = random.Random(SEED)
    results: list[tuple[int, float, list[float]]] = []
    for p, samples in [(2, 100), (3, 150), (4, 200), (8, 200), (16, 100), (32, 40)]:
        best = math.inf
        best_g: list[float] = []
        for _ in range(samples):
            # Include both interior Dirichlet samples and boundary faces.
            raw = np.array([rng.expovariate(1.0) for _ in range(p)])
            if rng.random() < 0.5:
                zero_count = rng.randrange(1, max(2, p // 3 + 1))
                for index in rng.sample(range(p), min(zero_count, p - 1)):
                    raw[index] = 0.0
            g = p * raw / raw.sum()
            ratio = leading_ratio(u_from_gaps(g))
            if math.isfinite(ratio) and ratio < best:
                best = ratio
                best_g = g.tolist()
        results.append((p, best, best_g))
    return results


def structured_scan() -> list[tuple[int, str, float]]:
    """Probe low-frequency, localized, alternating, and collision faces."""
    results: list[tuple[int, str, float]] = []
    for p in (4, 8, 16, 32, 64):
        index = np.arange(p, dtype=float)
        families: list[tuple[str, np.ndarray]] = []
        for mode in sorted({1, 2, max(1, p // 4), max(1, p // 2)}):
            families.append((f"cos_mode_{mode}", 1.0 + np.cos(2.0 * math.pi * mode * index / p)))
        spike = np.zeros(p)
        spike[0] = p
        families.append(("single_spike", spike))
        if p % 2 == 0:
            alternating = np.zeros(p)
            alternating[::2] = 2.0
            families.append(("alternating_collisions", alternating))
            half_block = np.zeros(p)
            half_block[: p // 2] = 2.0
            families.append(("half_block", half_block))
        for name, gaps in families:
            u = u_from_gaps(gaps)
            reconstructed = gaps_from_u(u)
            if float(np.max(np.abs(reconstructed - gaps))) > 2.0e-10:
                raise SystemExit(f"gap reconstruction failed for p={p} {name}")
            results.append((p, name, leading_ratio(u)))
    return results


def optimize_scan() -> list[tuple[int, float, list[float]]]:
    """Local SLSQP candidate search; still floating-point and non-probative."""
    from scipy.optimize import minimize

    rng = random.Random(SEED + 1)
    results: list[tuple[int, float, list[float]]] = []
    for p in (4, 6, 8, 12, 16):
        best = math.inf
        best_g: list[float] = []

        def objective(g: np.ndarray) -> float:
            if np.min(g) < -1.0e-8 or abs(float(np.sum(g)) - p) > 1.0e-5:
                return 10.0
            ratio = leading_ratio(u_from_gaps(np.maximum(g, 0.0)))
            return ratio if math.isfinite(ratio) else 10.0

        starts: list[np.ndarray] = []
        half = np.zeros(p)
        half[: p // 2] = p / max(1, p // 2)
        starts.append(half)
        for _ in range(3):
            raw = np.array([rng.expovariate(0.6) for _ in range(p)])
            starts.append(p * raw / raw.sum())
        for start in starts:
            result = minimize(
                objective,
                start,
                method="SLSQP",
                bounds=[(0.0, float(p))] * p,
                constraints={"type": "eq", "fun": lambda g, pp=p: float(np.sum(g) - pp)},
                options={"maxiter": 120, "ftol": 2.0e-9, "disp": False},
            )
            value = objective(result.x)
            if value < best:
                best = value
                best_g = np.maximum(result.x, 0.0).tolist()
        results.append((p, best, best_g))
    return results


def main() -> None:
    print(f"seed={SEED} quadrature_order={QUAD_ORDER}")
    for name, ratio, expected in exact_models():
        if math.isfinite(expected):
            error = abs(ratio - expected)
            print(f"{name}: ratio={ratio:.12f} expected={expected:.12f} error={error:.3e}")
            if error > 2.0e-5:
                raise SystemExit("normalization guard failed")
        else:
            print(f"{name}: ratio={ratio:.12f}")
    for p, name, ratio in structured_scan():
        print(
            f"structured p={p} family={name}: ratio={ratio:.12f} "
            f"action_margin={ratio - 0.5:.12f}"
        )
    for p, ratio, gaps in random_scan():
        print(f"random p={p}: min_ratio={ratio:.12f} action_margin={ratio - 0.5:.12f}")
        print("  gaps=" + ",".join(f"{value:.6g}" for value in gaps))
    if "--optimize" in sys.argv:
        for p, ratio, gaps in optimize_scan():
            print(f"optimized p={p}: min_ratio={ratio:.12f} action_margin={ratio - 0.5:.12f}")
            print("  gaps=" + ",".join(f"{value:.6g}" for value in gaps))


if __name__ == "__main__":
    main()
