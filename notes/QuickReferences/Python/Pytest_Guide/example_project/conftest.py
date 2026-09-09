"""Fixtures shared by the example project's tests.

pytest imports ``conftest.py`` automatically for every test file in this
directory, so the fixtures below can be requested by name without an import.
"""

import pytest

from stats_toolkit import RunningMean


@pytest.fixture
def sample_values() -> list[float]:
    """A small, fixed list of numbers used across several tests."""
    return [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]


@pytest.fixture
def running_mean():
    """A fresh RunningMean for one test, cleaned up afterwards.

    Everything before ``yield`` is setup. Everything after ``yield`` is
    teardown and runs even if the test fails. With a real resource (a file, a
    database handle) you would close it here instead of resetting.
    """
    accumulator = RunningMean()
    yield accumulator
    accumulator.reset()
