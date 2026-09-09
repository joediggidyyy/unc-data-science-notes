---
title: "Pytest: Tutorial and Reference"
slug: pytest-guide
summary: "Learn pytest from zero, then use it as a lookup reference. Written for data-science students."
audience: beginner
levels: [beginner, intermediate, advanced]
tags: [python, testing, pytest, data-science, quick-reference]
pytest_version: "9.x"
python_requires: ">=3.9"
last_reviewed: 2026-09-09
---

# Pytest: Tutorial and Reference

pytest is the most common way to write and run tests for Python code. This page
teaches it from the beginning and then doubles as a reference you can jump into
from a search.

It is written for data-science students: the examples are small functions that
work on lists of numbers, and there is a short section on testing numpy and
pandas code.

The current stable release is pytest 9.1.1. The examples here were run against
pytest 9.0.1. Anything on the 8.x or 9.x line behaves the same for this guide.

## Difficulty labels

Every section is labelled so you can stop when you have enough.

- **Beginner** — the core path. Read these first, in order.
- **Intermediate** — useful once the basics are comfortable.
- **Advanced** — pointers and edge cases; skim or skip.

Within each track the Beginner sections come first, then Intermediate, then
Advanced. Nothing you need as a beginner is hidden behind a later label.

## How to use this guide

**Level:** Beginner

**What you'll learn**

- The two ways to read this page.
- Where the runnable example lives.

There are two tracks in one page:

- **Tutorial track** (sections 1–12): read top to bottom. Each section builds on
  the last and uses one small example project.
- **Reference track** (sections 14–24): short, self-contained entries, kept
  deliberately terse — a definition, a small example, the effect. Land here
  from a search; you do not need the tutorial first.

Section 13 is a data-science track. The last section describes the runnable
example project under [`./example_project/`](./example_project/).

Every tutorial section opens with **What you'll learn** and closes with a
**Quick check**. Every section carries a **Level:** label.

**Quick check**

- If you have never used pytest, where do you start? (Section 1, and read in
  order.)

---

## 1. Why pytest

**Level:** Beginner

**What you'll learn**

- What a test and a test runner are.
- How pytest compares with the standard-library `unittest`.

A **test** is a small function that runs your code and checks the result. A
**test runner** finds those functions, runs them, and reports which passed.

pytest is a test runner. You write a function whose name starts with `test_`,
put a plain `assert` in it, and pytest does the rest.

```python
def test_two_plus_two():
    assert 2 + 2 == 4
```

pytest and `unittest` (in the standard library) both run tests. pytest needs
less code:

| Task | unittest | pytest |
|---|---|---|
| Check a value | `self.assertEqual(a, b)` | `assert a == b` |
| Set up shared data | `setUp` method | a fixture |
| Run one test many times | write a loop | `@pytest.mark.parametrize` |
| Add features | subclass | install a plugin |

pytest also runs existing `unittest` tests unchanged, so you can adopt it
gradually.

**Quick check**

- What must a test function's name start with so pytest finds it? (`test_`.)

---

## 2. Install pytest and lay out a project

**Level:** Beginner

**What you'll learn**

- How to install pytest into a virtual environment.
- Where test files go and how pytest discovers them.

Work inside a virtual environment so the install stays local to the project.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -U pytest
pytest --version
```

```text
pytest 9.0.1
```

pytest discovers tests by name:

- Files named `test_*.py` or `*_test.py`.
- Functions named `test_*`.
- Classes named `Test*` (with no `__init__` method).

A common layout keeps tests in their own folder next to the code:

```text
my_project/
    stats_toolkit.py
    tests/
        test_stats_toolkit.py
```

The example project in this guide keeps the module and its tests in one folder
to stay small; both layouts work.

**Quick check**

- Will pytest collect a function called `check_mean`? (No — it must start with
  `test_`.)

---

## 3. Write and run your first test

**Level:** Beginner

**What you'll learn**

- How to write a test file and run it.
- How to read a passing run and a failing run.

Create `test_stats_toolkit.py` next to `stats_toolkit.py`:

```python
from stats_toolkit import mean


def test_mean_of_a_short_list():
    assert mean([2, 4]) == 3
```

Run pytest from the project folder:

```bash
pytest
```

```text
test_stats_toolkit.py .                                              [100%]
1 passed in 0.01s
```

The dot is the passing test. Add `-v` for one line per test, or `-q` for less
output.

Now change the expected value to something wrong (`== 4`) and run again:

```text
================================== FAILURES ===================================
_________________________ test_mean_of_a_short_list ___________________________

    def test_mean_of_a_short_list():
>       assert mean([2, 4]) == 4
E       assert 3.0 == 4
E        +  where 3.0 = mean([2, 4])

test_stats_toolkit.py:4: AssertionError
========================== short test summary info ===========================
FAILED test_stats_toolkit.py::test_mean_of_a_short_list - assert 3.0 == 4
```

pytest rewrites the `assert` so the message shows both sides and where the
value came from. Change the expectation back to `== 3` and the test passes.

**Quick check**

- In the failure above, what did `mean([2, 4])` actually return? (`3.0`.)

---

## 4. Assertions

**Level:** Beginner

**What you'll learn**

- How to assert on values, collections, exceptions, and floats.

Use a plain `assert`. pytest shows a useful message on failure without any
special method.

```python
def test_lists_compare_element_by_element():
    assert mean([1, 2, 3, 4]) == 2.5
    assert sorted([3, 1, 2]) == [1, 2, 3]
```

To check that code raises an error, use `pytest.raises` as a context manager.
`match=` checks the message with a regular expression.

```python
import pytest
from stats_toolkit import mean


def test_mean_of_empty_list_raises():
    with pytest.raises(ValueError, match="at least one value"):
        mean([])
```

Floating-point results are almost never exactly equal. Use `pytest.approx`.

```python
from stats_toolkit import zscores


def test_zscores_are_scaled():
    assert zscores([1, 2, 4]) == pytest.approx(
        [-0.872871561, -0.218217890, 1.091089451]
    )
```

`pytest.approx` also works on single numbers, dicts, and nested sequences. See
[section 16](#16-reference-assertions) for the full set.

**Quick check**

- Why not write `assert result == 0.1 + 0.2`? (Float rounding — use
  `pytest.approx`.)

---

## 5. Organize tests

**Level:** Beginner

**What you'll learn**

- How to group related tests.
- The arrange–act–assert shape.

Keep each test focused on one behaviour and name it after that behaviour.
A helpful shape is **arrange** (set up inputs), **act** (call the code),
**assert** (check the result).

```python
def test_clip_limits_each_value():
    values = [-2, 0, 5, 12]          # arrange
    result = clip(values, low=0, high=10)   # act
    assert result == [0, 0, 5, 10]   # assert
```

Group related tests in a `Test*` class. pytest gives each test its own
instance, so they stay isolated.

```python
class TestSampleVariance:
    def test_typical(self):
        assert sample_variance([10, 12, 14]) == 4.0

    def test_needs_two_values(self):
        with pytest.raises(ValueError):
            sample_variance([1])
```

Run one test by its node id (`file::Class::test`):

```bash
pytest test_stats_toolkit.py::TestSampleVariance::test_typical
```

**Quick check**

- What does pytest give each method in a `Test*` class? (Its own fresh
  instance.)

---

## 6. Fixtures

**Level:** Beginner

**What you'll learn**

- How to share setup between tests with a fixture.
- How to clean up with a `yield` fixture.

A **fixture** is a function that builds something a test needs. A test asks for
it by putting the fixture's name in its parameter list.

```python
import pytest


@pytest.fixture
def sample_values():
    return [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]


def test_mean_of_sample(sample_values):
    assert mean(sample_values) == pytest.approx(5.0)
```

Put a fixture in `conftest.py` and every test file in that folder can use it
without importing anything.

To clean up after a test, `yield` the value and put teardown code after the
`yield`. It runs even if the test fails.

```python
@pytest.fixture
def running_mean():
    accumulator = RunningMean()
    yield accumulator          # setup done; test runs here
    accumulator.reset()        # teardown
```

Fixtures have a **scope**: `function` (default, rebuilt per test), `class`,
`module`, `package`, or `session` (built once and shared). Use a wider scope
only for read-only setup that is expensive to build.

**Quick check**

- Where do you put a fixture so several test files share it? (`conftest.py`.)

---

## 7. Parametrize tests

**Level:** Intermediate

**What you'll learn**

- How to run one test against many inputs.

`@pytest.mark.parametrize` runs a test once per row of data. The first argument
names the parameters; the second is a list of value rows.

```python
import pytest


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
```

Run with `-v` and pytest shows one line per row:

```text
test_stats_toolkit.py::test_mean_is_the_average[values0-1.0] PASSED
test_stats_toolkit.py::test_mean_is_the_average[values1-5.0] PASSED
...
```

Give rows readable names with `ids=`, mark a single row with
`pytest.param(..., marks=pytest.mark.xfail)`, or stack two `parametrize`
decorators to get every combination. See
[section 19](#19-reference-parametrize).

**Quick check**

- Five rows and one test function — how many test runs? (Five.)

---

## 8. Markers: skip, xfail, and custom marks

**Level:** Intermediate

**What you'll learn**

- How to skip a test, expect a failure, and tag tests.

A **marker** attaches metadata to a test.

```python
import sys
import pytest


@pytest.mark.skip(reason="feature not built yet")
def test_placeholder():
    ...


@pytest.mark.skipif(sys.version_info < (3, 9), reason="needs Python 3.9+")
def test_new_syntax():
    ...


@pytest.mark.xfail(reason="weighted_mean is not implemented yet", strict=True)
def test_weighted_mean():
    from stats_toolkit import weighted_mean
```

- `skip` — never run this test.
- `skipif(condition, reason=)` — skip when the condition is true.
- `xfail(reason=, strict=)` — expect this to fail. With `strict=True`, an
  unexpected pass fails the run so you remember to remove the marker.

Define your own marker and select with `-m`:

```python
@pytest.mark.slow
def test_large_input():
    ...
```

```bash
pytest -m "not slow"
```

Register custom markers in the config file (see
[section 10](#10-configuration)) or pytest warns about them.

**Quick check**

- Which marker means "I know this fails, run it anyway and expect that"?
  (`xfail`.)

---

## 9. Isolation helpers: tmp_path, monkeypatch, capsys

**Level:** Intermediate

**What you'll learn**

- Built-in fixtures that keep a test from touching real state.

Request these by name; pytest provides them.

**`tmp_path`** — a fresh empty directory (a `pathlib.Path`) for this test only.

```python
def test_reads_numbers_from_a_file(tmp_path):
    data_file = tmp_path / "values.txt"
    data_file.write_text("2\n4\n6\n")
    numbers = [float(line) for line in data_file.read_text().split()]
    assert mean(numbers) == 4.0
```

**`monkeypatch`** — change an attribute, dict entry, or environment variable
for one test; pytest undoes it afterwards.

```python
import os


def test_uses_env_precision(monkeypatch):
    monkeypatch.setenv("STATS_PRECISION", "3")
    assert os.environ["STATS_PRECISION"] == "3"
```

**`capsys`** — capture text printed to stdout and stderr.

```python
def test_prints_a_summary(capsys):
    print("mean = 4.0")
    captured = capsys.readouterr()
    assert "mean = 4.0" in captured.out
```

Use `caplog` the same way for log records.

**Quick check**

- After a `monkeypatch.setenv` test finishes, is the variable still set?
  (No — pytest restores it.)

---

## 10. Configuration

**Level:** Intermediate

**What you'll learn**

- Where pytest settings live and the keys you will use first.

pytest reads settings from one file, in this order of preference:
`pyproject.toml`, then `pytest.ini`, then `tox.ini`, then `setup.cfg`.

In `pyproject.toml` the settings go under `[tool.pytest.ini_options]`:

```toml
[tool.pytest.ini_options]
minversion = "9.0"
testpaths = ["tests"]
addopts = "-ra -q"
markers = [
    "slow: a slower test; deselect with -m 'not slow'",
]
filterwarnings = ["default"]
```

- `testpaths` — where pytest looks when you give it no path.
- `addopts` — flags applied on every run.
- `markers` — registers your custom markers.
- `filterwarnings` — how to treat warnings.
- `minversion` — fail fast if pytest is too old.

The example project's [`pyproject.toml`](./example_project/pyproject.toml) is a
working copy of the above. `conftest.py` is for fixtures and hooks; the config
file is for settings.

**Quick check**

- You keep passing `-q` by hand. Where do you put it once? (`addopts`.)

---

## 11. Coverage and continuous integration

**Level:** Intermediate

**What you'll learn**

- How to measure which lines your tests run.
- A minimal CI job (CI = continuous integration).

Install the coverage plugin and ask for a report:

```bash
pip install pytest-cov
pytest --cov=stats_toolkit --cov-report=term-missing
```

```text
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
stats_toolkit.py      39      3    92%   46, 53, 75
------------------------------------------------
TOTAL                 39      3    92%
```

The `Missing` column lists line numbers no test exercised — here, three
error branches: the all-identical guard in `zscores`, the `low > high`
guard in `clip`, and the empty guard in `RunningMean.value`. Aim for the
behaviour that matters, not a perfect number.

A minimal GitHub Actions workflow at `.github/workflows/tests.yml`:

```yaml
name: tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -U pytest pytest-cov
      - run: pytest --cov=stats_toolkit
```

**Quick check**

- What does `term-missing` add to the coverage report? (The line numbers with
  no coverage.)

---

## 12. Where to go next

**Level:** Advanced

**What you'll learn**

- Named next topics, with links. This guide does not teach these.

- **Fixtures as plugins** — move shared fixtures into an installable package;
  layer `conftest.py` files by directory.
- **tox / nox** — run the test suite across several Python versions.
- **Hypothesis** — generate test inputs instead of listing them
  (property-based testing): <https://hypothesis.readthedocs.io/>.
- **pytest-xdist** — run tests in parallel with `-n auto`.
- **pytest-randomly** — shuffle test order to catch hidden dependencies.
- **pytest-asyncio** — test `async def` code.
- **Writing a plugin / hook functions** —
  <https://docs.pytest.org/en/stable/how-to/writing_plugins.html>.

**Quick check**

- Which tool runs your suite on several Python versions? (tox or nox.)

---

## 13. Testing numeric and data code

**Level:** Beginner to Advanced (per sub-section)

**What you'll learn**

- How to compare floats, numpy arrays, and pandas objects in a test.

numpy and pandas are optional. Install what you need:

```bash
pip install numpy pandas
```

### Comparing floats

**Level:** Beginner

`==` fails on floats because of rounding. Use `pytest.approx`, which accepts a
relative tolerance `rel=` and an absolute tolerance `abs=`.

```python
import pytest
from stats_toolkit import zscores


def test_zscores():
    assert zscores([1, 2, 4]) == pytest.approx(
        [-0.872871561, -0.218217890, 1.091089451], rel=1e-6
    )
```

`pytest.approx` also compares dicts and single numbers.

### numpy array assertions

**Level:** Intermediate

Do not use a plain `assert` on arrays — `a == b` is itself an array and its
truth value is ambiguous. Use `numpy.testing`.

```python
import numpy as np
from numpy.testing import assert_allclose


def test_column_means():
    data = np.array([[1.0, 2.0], [3.0, 4.0]])
    assert_allclose(data.mean(axis=0), [2.0, 3.0])
```

`assert_allclose(actual, desired, rtol=, atol=)` for floats;
`assert_array_equal` for exact integer or boolean arrays.

### pandas frame and series assertions

**Level:** Intermediate

Use `pandas.testing`. It reports the first differing cell.

```python
import pandas as pd
from pandas.testing import assert_frame_equal


def test_group_means():
    frame = pd.DataFrame({"g": ["a", "a", "b"], "x": [1.0, 3.0, 5.0]})
    result = frame.groupby("g", as_index=False)["x"].mean()
    expected = pd.DataFrame({"g": ["a", "b"], "x": [2.0, 5.0]})
    assert_frame_equal(result, expected)
```

Useful keywords: `check_dtype`, `check_like` (ignore column or row order),
`check_exact`, `rtol`. `assert_series_equal` is the one-column version.

### Fixtures for sample data

**Level:** Intermediate

Build small data in a fixture so every test starts from the same known frame.

```python
import pandas as pd
import pytest


@pytest.fixture
def sample_frame():
    return pd.DataFrame({"x": [1.0, 2.0, 3.0], "y": [10.0, 20.0, 30.0]})


def test_total(sample_frame):
    assert sample_frame["x"].sum() == 6.0
```

For a read-only frame loaded from a file, use `scope="session"` so it is built
once for the whole run.

### Testing randomized code

**Level:** Intermediate

Seed the generator so results repeat. Pass the seed through a fixture so every
test shares it.

```python
import numpy as np
import pytest


@pytest.fixture
def rng():
    return np.random.default_rng(12345)


def test_sample_mean_is_close(rng):
    draws = rng.normal(loc=0.0, scale=1.0, size=10_000)
    assert draws.mean() == pytest.approx(0.0, abs=0.05)
```

The `pytest-randomly` plugin shuffles test order (and reseeds) each run to
catch tests that secretly depend on each other.

### Testing notebook logic

**Level:** Advanced

Notebooks are hard to test directly. Two practical options:

- Move the real logic into a `.py` module and test that. The notebook then just
  calls tested functions.
- Run the notebook end to end in CI with the `nbmake` plugin
  (`pytest --nbmake notebooks/`), or `nbval` as an alternative.

**Quick check**

- Why not `assert numpy_array_a == numpy_array_b`? (The result is an array; its
  truth value is ambiguous. Use `assert_allclose`.)

---

## 14. Reference: command-line flags

**Level:** Beginner

Run `pytest` from the project root. Common flags:

| Flag | Effect |
|---|---|
| `-k EXPR` | run tests whose name matches the expression (`-k "mean and not empty"`) |
| `-m EXPR` | run tests with matching markers (`-m "not slow"`) |
| `-x` | stop at the first failure |
| `--maxfail=N` | stop after N failures |
| `-q` / `-v` | quieter / more verbose output |
| `-s` | do not capture output (let `print` show) |
| `-ra` | summary of everything except passes, at the end |
| `--lf` | run only the tests that failed last time |
| `--ff` | run the last failures first, then the rest |
| `--collect-only` (`--co`) | list the tests without running them |
| `--durations=N` | show the N slowest tests |

---

## 15. Reference: test discovery

**Level:** Beginner

pytest collects, by default:

- files matching `test_*.py` or `*_test.py`, under `testpaths` or the current
  directory;
- functions prefixed `test_`;
- classes prefixed `Test` with no `__init__` method, and their `test_` methods.

A **node id** names one test: `path/to/test_file.py::TestClass::test_method`.
Pass a node id to run just that test. `rootdir` is the folder pytest treats as
the project root; it is printed in the run header and anchors config discovery.

---

## 16. Reference: assertions

**Level:** Beginner

| Need | Write |
|---|---|
| Compare values | `assert a == b` |
| Add a message | `assert a == b, "means differ"` |
| Expect an exception | `with pytest.raises(ValueError): ...` |
| Check the message | `pytest.raises(ValueError, match="regex")` |
| Expect a warning | `with pytest.warns(UserWarning): ...` |
| Compare floats | `assert x == pytest.approx(y)` |
| Float tolerance | `pytest.approx(y, rel=1e-6, abs=1e-12)` |
| Approx a list or dict | `pytest.approx([1.0, 2.0])` |

`pytest.raises` binds the exception via `as`:

```python
with pytest.raises(ValueError) as info:
    mean([])
assert "one value" in str(info.value)
```

---

## 17. Reference: built-in fixtures

**Level:** Beginner

| Fixture | Gives you |
|---|---|
| `tmp_path` | a fresh `Path` directory for this test |
| `tmp_path_factory` | make temp dirs at session scope |
| `monkeypatch` | `setattr` / `setitem` / `setenv` / `chdir`, auto-undone |
| `capsys` / `capfd` | captured stdout and stderr (Python-level / file-level) |
| `caplog` | captured log records |
| `recwarn` | recorded warnings |
| `request` | info about the running test; `request.param` for parametrized fixtures |
| `pytestconfig` | access to config values and CLI options |
| `cache` | small key–value store across runs (backs `--lf`) |

---

## 18. Reference: fixtures

**Level:** Intermediate

```python
@pytest.fixture(scope="module", autouse=False, params=None, ids=None)
def my_fixture(request):
    ...
```

- **scope** — `function` (default), `class`, `module`, `package`, `session`.
- **autouse=True** — every test in scope gets it without asking.
- **params=[...]** — the fixture (and tests using it) run once per value;
  read the value with `request.param`; label with `ids=`.
- **teardown** — either `yield value` then cleanup, or
  `request.addfinalizer(fn)`.
- **factory as fixture** — return a function so a test can build several
  objects:

```python
@pytest.fixture
def make_values():
    def _make(n, fill=0.0):
        return [fill] * n
    return _make
```

- **override** — a fixture defined in a lower `conftest.py` or in the test file
  replaces one with the same name from higher up.

---

## 19. Reference: parametrize

**Level:** Intermediate

```python
@pytest.mark.parametrize("a, expected", [(1, 1), (2, 4), (3, 9)])
def test_square(a, expected):
    assert a * a == expected
```

- Names: one comma string (`"a, expected"`) or a list (`["a", "expected"]`).
- Rows: tuples matching the names; a single-name param takes bare values.
- `ids=["one", "two", "three"]` — readable test names.
- `pytest.param(3, 9, id="three", marks=pytest.mark.xfail)` — per-row id and
  marks.
- Stacked decorators multiply:

```python
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_pairs(x, y):
    ...   # runs 4 times
```

- `indirect=True` sends the value through a fixture of the same name first.

---

## 20. Reference: markers

**Level:** Intermediate

| Marker | Purpose |
|---|---|
| `@pytest.mark.skip(reason=)` | never run |
| `@pytest.mark.skipif(cond, reason=)` | run unless `cond` |
| `@pytest.mark.xfail(reason=, strict=, raises=)` | expected to fail |
| `@pytest.mark.parametrize(...)` | many input rows |
| `@pytest.mark.usefixtures("name")` | require a fixture without an argument |
| `@pytest.mark.filterwarnings("error")` | warning rules for one test |
| `@pytest.mark.slow` (custom) | your own tag; select with `-m` |

Register custom markers in config:

```toml
markers = ["slow: a slower test"]
```

Select with an expression: `pytest -m "slow and not network"`.

---

## 21. Reference: conftest.py

**Level:** Intermediate

- A file named `conftest.py` that pytest imports automatically — you never
  import it yourself.
- Fixtures and hooks in it are available to every test in that folder and every
  sub-folder.
- The nearest `conftest.py` wins; several can layer from the root down.
- Common uses: shared fixtures, custom command-line options, hook functions,
  adjusting the import path.

---

## 22. Reference: configuration files

**Level:** Intermediate

| File | Section header |
|---|---|
| `pyproject.toml` | `[tool.pytest.ini_options]` |
| `pytest.ini` | `[pytest]` |
| `tox.ini` | `[pytest]` |
| `setup.cfg` | `[tool:pytest]` |

pytest uses the first it finds, preferring `pyproject.toml`. Keys you will meet
early:

- `testpaths`, `addopts`, `markers`, `filterwarnings`, `minversion`
- `norecursedirs` — folders to skip during collection
- `xfail_strict = true` — make every `xfail` strict by default
- `log_cli = true` — show log output live

---

## 23. Reference: common plugins

**Level:** Intermediate

Install with `pip install <name>`.

| Plugin | Adds |
|---|---|
| `pytest-cov` | `--cov` coverage reporting |
| `pytest-mock` | a `mocker` fixture wrapping `unittest.mock` |
| `pytest-xdist` | `-n auto` to run tests in parallel |
| `pytest-randomly` | random test order and seed each run |
| `pytest-asyncio` | run `async def` tests |
| `pytest-timeout` | fail a test that runs too long |
| `pytest-sugar` | a progress bar and nicer failure list |
| `nbmake` | `--nbmake` to execute notebooks as tests |

---

## 24. Reference: exit codes

**Level:** Advanced

`pytest` returns a numeric exit code. CI uses it to pass or fail the job.

| Code | `pytest.ExitCode` name | Meaning |
|---|---|---|
| 0 | `OK` | all collected tests passed |
| 1 | `TESTS_FAILED` | tests ran; some failed |
| 2 | `INTERRUPTED` | the run was interrupted (for example, Ctrl-C) |
| 3 | `INTERNAL_ERROR` | an internal error in pytest |
| 4 | `USAGE_ERROR` | a command-line usage error |
| 5 | `NO_TESTS_COLLECTED` | pytest found nothing to run |

Code 5 is the one that catches a misconfigured CI job — the run "passes" only
because no tests were found. Guard against it with `--strict-markers` and an
explicit `testpaths`.

---

## The example project

**Level:** Beginner

[`./example_project/`](./example_project/) is a small, runnable project the
tutorial track uses throughout.

| File | What it holds |
|---|---|
| [`stats_toolkit.py`](./example_project/stats_toolkit.py) | `mean`, `sample_variance`, `zscores`, `clip`, and a `RunningMean` class |
| [`test_stats_toolkit.py`](./example_project/test_stats_toolkit.py) | the worked tests from sections 3–8 |
| [`conftest.py`](./example_project/conftest.py) | the `sample_values` and `running_mean` fixtures |
| [`pyproject.toml`](./example_project/pyproject.toml) | the configuration from section 10 |

Run it:

```bash
cd example_project
python -m pytest -ra
```

```text
...............x.                                                    [100%]
XFAIL test_stats_toolkit.py::test_weighted_mean_not_implemented
16 passed, 1 xfailed in 0.12s
```

The one `xfail` is deliberate: it marks a function that does not exist yet, so
the marker is a reminder to write it.

---

## References

- pytest documentation (stable): <https://docs.pytest.org/en/stable/>
- Get started: <https://docs.pytest.org/en/stable/getting-started.html>
- How-to guides: <https://docs.pytest.org/en/stable/how-to/index.html>
- Fixtures: <https://docs.pytest.org/en/stable/how-to/fixtures.html>
- Parametrize: <https://docs.pytest.org/en/stable/how-to/parametrize.html>
- Exit codes: <https://docs.pytest.org/en/stable/reference/exit-codes.html>
- pytest on PyPI: <https://pypi.org/project/pytest/>
- freeCodeCamp, "How to Use Pytest":
  <https://www.freecodecamp.org/news/how-to-use-pytest-a-guide-to-testing-in-python/>
- Python Developer Tooling Handbook, pytest reference:
  <https://pydevtools.com/handbook/reference/pytest/>
