"""A tiny statistics toolkit used as the running example in the pytest guide.

Every function works on a plain list of numbers so the behaviour is easy to
check by hand. The functions raise ``ValueError`` on bad input so the guide has
a natural reason to show ``pytest.raises``.
"""

from __future__ import annotations

from collections.abc import Iterable


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of ``values``.

    Raise ``ValueError`` when ``values`` is empty.
    """
    values = list(values)
    if not values:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)


def sample_variance(values: Iterable[float]) -> float:
    """Return the sample variance of ``values`` (divisor ``n - 1``).

    Raise ``ValueError`` when fewer than two values are given.
    """
    values = list(values)
    if len(values) < 2:
        raise ValueError("sample_variance() needs at least two values")
    centre = mean(values)
    return sum((x - centre) ** 2 for x in values) / (len(values) - 1)


def zscores(values: Iterable[float]) -> list[float]:
    """Return the z-score of each value: ``(x - mean) / standard_deviation``.

    Raise ``ValueError`` when fewer than two values are given, or when every
    value is identical (the standard deviation would be zero).
    """
    values = list(values)
    centre = mean(values)
    spread = sample_variance(values) ** 0.5
    if spread == 0:
        raise ValueError("zscores() needs values that are not all identical")
    return [(x - centre) / spread for x in values]


def clip(values: Iterable[float], low: float, high: float) -> list[float]:
    """Return ``values`` with every element limited to the range ``[low, high]``."""
    if low > high:
        raise ValueError("clip() needs low <= high")
    return [min(max(x, low), high) for x in values]


class RunningMean:
    """Accumulate numbers one at a time and report their mean so far."""

    def __init__(self) -> None:
        self._count = 0
        self._total = 0.0

    def add(self, value: float) -> None:
        self._count += 1
        self._total += value

    def reset(self) -> None:
        self._count = 0
        self._total = 0.0

    @property
    def value(self) -> float:
        if self._count == 0:
            raise ValueError("RunningMean has no values yet")
        return self._total / self._count
