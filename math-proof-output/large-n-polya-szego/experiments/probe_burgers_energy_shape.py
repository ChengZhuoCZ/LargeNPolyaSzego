"""Heuristic probe for the Cayley/Burgers endpoint energy.

This script searches for simple shape properties of

    E(t) = || b o (id + t b)^{-1} ||_{H^{-1/2}(T)}^2,

for periodic piecewise-linear b with |b'| <= 1 and zero mean.  Its output is
candidate-generation only; no floating-point observation is proof evidence.
"""

from __future__ import annotations

import numpy as np


SEED = 20260721
GRID = 32768
MODES = 8192


def periodic_primitive(slopes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return a zero-mean periodic primitive and its piecewise-constant slope."""
    n = len(slopes)
    samples_per_cell = GRID // n
    derivative = np.repeat(slopes, samples_per_cell)
    if len(derivative) != GRID:
        raise ValueError("number of cells must divide GRID")
    derivative -= derivative.mean()
    scale = max(1.0, float(np.max(np.abs(derivative))))
    derivative /= scale
    b = np.empty(GRID, dtype=float)
    b[0] = 0.0
    b[1:] = np.cumsum(derivative[:-1]) / GRID
    b -= b.mean()
    return b, derivative


def energy_curve(b: np.ndarray, derivative: np.ndarray, times: np.ndarray) -> np.ndarray:
    r = np.arange(GRID, dtype=float) / GRID
    values = []
    for time in times:
        coordinate = r + time * b
        coordinate = np.concatenate((coordinate - 1.0, coordinate, coordinate + 1.0))
        profile = np.tile(b, 3)
        order = np.argsort(coordinate, kind="stable")
        pulled = np.interp(r, coordinate[order], profile[order])
        pulled -= pulled.mean()
        coefficients = np.fft.fft(pulled) / GRID
        modes = np.arange(1, MODES + 1, dtype=float)
        values.append(float(np.sum(2.0 * np.abs(coefficients[1 : MODES + 1]) ** 2 / modes)))
    return np.array(values)


def main() -> None:
    rng = np.random.default_rng(SEED)
    times = np.linspace(-1.0, 1.0, 17)
    worst_convex = 0.0
    worst_log_convex = 0.0
    smallest_ratio = float("inf")
    for cells in (4, 8, 16, 32, 64):
        for sample in range(6):
            slopes = rng.uniform(-1.0, 1.0, size=cells)
            if sample == 0:
                slopes = np.resize(np.array([-1.0, 1.0]), cells)
            b, derivative = periodic_primitive(slopes)
            energies = energy_curve(b, derivative, times)
            second = energies[:-2] - 2.0 * energies[1:-1] + energies[2:]
            log_second = (
                np.log(energies[:-2])
                - 2.0 * np.log(energies[1:-1])
                + np.log(energies[2:])
            )
            worst_convex = min(worst_convex, float(second.min()))
            worst_log_convex = min(worst_log_convex, float(log_second.min()))
            smallest_ratio = min(smallest_ratio, float(energies[-1] / energies[0]))
    print(f"seed={SEED} grid={GRID} modes={MODES}")
    print(f"minimum endpoint ratio={smallest_ratio:.12f}")
    print(f"minimum discrete second difference E={worst_convex:.12e}")
    print(f"minimum discrete second difference log(E)={worst_log_convex:.12e}")


if __name__ == "__main__":
    main()
