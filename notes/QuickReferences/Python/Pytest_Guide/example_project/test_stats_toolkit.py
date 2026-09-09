"""Worked tests for stats_toolkit.

The pytest guide walks through these tests section by section. Every test here
passes; the guide shows a deliberately failing case in prose only.
"""

import sys

import pytest

from stats_toolkit import clip, mean, sample_variance, zscores


# --- plain asserts ---------------------------------------------------------


def test_mean_of_a_short_list():
    assert mean([2, 4]) == 3


def test_mean_of_one_value():
    assert mean([7]) == 7


# --- checking that an error is raised ------------------------------------


def test_mean_of_empty_list_raises():
    with pytest.raises(ValueError, match="at least one value"):
        mean([])


# --- grouping related tests in a class ---------------------------------


class TestSampleVariance:
    def test_typical(self):
        assert sample_variance([10, 12, 14]) == 4.0

    def test_needs_two_values(self):
        with pytest.raises(ValueError):
            sample_variance([1])


# --- comparing floating-point results --------------------------------


def test_zscores_are_centred_and_scaled():
    result = zscores([1, 2, 4])
    assert result == pytest.approx([-0.872871561, -0.218217890, 1.091089451])


# --- one test, many input rows --------------------------------------


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 1, 1], 1.0),
        ([0, 10], 5.0),
        ([2, 4, 6], 4.0),
        ([-5, 5], 0.0),
        ([3], 3.0),
    ],
)
def test_mean_is_the_average(values, expected):
    assert mean(values) == expected


def test_clip_limits_each_value():
    assert clip([-2, 0, 5, 12], low=0, high=10) == [0, 0, 5, 10]


# --- fixtures from conftest.py ------------------------------------


def test_sample_values_fixture(sample_values):
    assert mean(sample_values) == pytest.approx(5.0)


def test_running_mean_fixture(running_mean):
    running_mean.add(2)
    running_mean.add(4)
    assert running_mean.value == 3


# --- skipping and expected failures --------------------------


@pytest.mark.skipif(
    sys.version_info < (3, 9), reason="requires Python 3.9 or newer"
)
def test_runs_on_supported_python():
    assert sys.version_info >= (3, 9)


@pytest.mark.xfail(reason="weighted_mean is not implemented yet", strict=True)
def test_weighted_mean_not_implemented():
    from stats_toolkit import weighted_mean  # noqa: F401


# --- a custom marker (registered in pyproject.toml) --------


@pytest.mark.slow
def test_large_input_still_averages():
    big = list(range(100_000))
    assert mean(big) == pytest.approx((len(big) - 1) / 2)
