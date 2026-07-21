"""Heuristic probe for the critical Burgers cubic estimate.

For periodic profiles ``h`` on a unit circle, the script samples piecewise
constant slopes subject to the two endpoint monotonicity bounds along the
Burgers interpolation and records

    mean((H h)^3) / <H h, |D|^{-1} H h>.

The output is candidate-generation only and is not proof evidence.
"""

from __future__ import annotations

import numpy as np


SEED = 20260721
GRID = 32768
SAMPLES = 400


def hilbert(values: np.ndarray) -> np.ndarray:
    coefficients = np.fft.fft(values)
    modes = np.fft.fftfreq(len(values)) * len(values)
    multiplier = -1j * np.sign(modes)
    return np.fft.ifft(multiplier * coefficients).real


def inverse_half_energy(values: np.ndarray) -> float:
    coefficients = np.fft.fft(values) / len(values)
    modes = np.fft.fftfreq(len(values)) * len(values)
    mask = modes != 0
    return float(np.sum(np.abs(coefficients[mask]) ** 2 / np.abs(modes[mask])))


def primitive_from_slopes(slopes: np.ndarray) -> np.ndarray:
    repeats = GRID // len(slopes)
    derivative = np.repeat(slopes, repeats)
    if len(derivative) != GRID:
        raise ValueError("the cell count must divide GRID")
    derivative -= derivative.mean()
    profile = np.empty(GRID, dtype=float)
    profile[0] = 0.0
    profile[1:] = np.cumsum(derivative[:-1]) / GRID
    profile -= profile.mean()
    return profile


def pull_burgers(profile: np.ndarray, time: float) -> np.ndarray:
    r = np.arange(GRID, dtype=float) / GRID
    coordinate = r + time * profile
    coordinate = np.concatenate((coordinate - 1.0, coordinate, coordinate + 1.0))
    values = np.tile(profile, 3)
    order = np.argsort(coordinate, kind="stable")
    pulled = np.interp(r, coordinate[order], values[order])
    pulled -= pulled.mean()
    return pulled


def cubic_ratio(profile: np.ndarray) -> float:
    conjugate = hilbert(profile)
    denominator = inverse_half_energy(conjugate)
    if denominator <= 1e-18:
        return 0.0
    return float(np.mean(conjugate**3) / denominator)


def main() -> None:
    rng = np.random.default_rng(SEED)
    best = (-np.inf, 0, 0.0)
    worst = (np.inf, 0, 0.0)
    for cells in (4, 8, 16, 32, 64, 128):
        if GRID % cells:
            continue
        for sample in range(SAMPLES // 6):
            slopes = rng.uniform(-1.0, 1.0, size=cells)
            if sample == 0:
                slopes = np.resize(np.array([-1.0, 1.0]), cells)
            initial = primitive_from_slopes(slopes)
            for time in np.linspace(0.0, 1.0, 17):
                profile = pull_burgers(initial, time)
                ratio = cubic_ratio(profile)
                if ratio > best[0]:
                    best = (ratio, cells, time)
                if ratio < worst[0]:
                    worst = (ratio, cells, time)
    print(f"seed={SEED} grid={GRID} samples={SAMPLES}")
    print(f"largest cubic ratio={best[0]:.12f} cells={best[1]} time={best[2]:.4f}")
    print(f"smallest cubic ratio={worst[0]:.12f} cells={worst[1]} time={worst[2]:.4f}")


if __name__ == "__main__":
    main()
