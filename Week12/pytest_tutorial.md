# pytest

`pytest` is a lightweight yet powerful framework used to write simple as well as scalable test cases in Python. It’s widely preferred because it reduces boilerplate code and is very flexible.

---

## Key Features
* **Simple syntax**: Write tests as normal Python functions
* **Auto-discovery**: Finds tests automatically
* **Rich assertions**: No need for special assert methods
* **Fixtures**: Reusable setup/teardown logic
* **Plugins**: Huge ecosystem (coverage, parallel runs, etc.)

---

## Basic Example

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run:

```bash
pytest
```

---

## Naming Conventions

* Test files: `test_*.py` or `*_test.py`
* Test functions: start with `test_`
* Test classes: start with `Test`

---

## Assertions

```python
def test_example():
    assert 2 + 2 == 4
```

Pytest shows detailed failure output automatically.

---

## Fixtures (Important)

Used for setup/teardown logic.

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 25}

def test_data(sample_data):
    assert sample_data["name"] == "Alice"
```

---

## Parametrization

Run same test with multiple inputs:

```python
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 0, 0)
])
def test_add(a, b, result):
    assert a + b == result
```

---

## Running Specific Tests

```bash
pytest test_file.py
pytest -k "add"
pytest -m slow
```

---

## Useful Command Options

* `-v` → verbose output
* `-q` → quiet mode
* `--maxfail=1` → stop after 1 failure
* `--disable-warnings`
* `--tb=short` → shorter tracebacks

---

## Fixtures Scope

```python
@pytest.fixture(scope="module")
```

Scopes:

* `function` (default)
* `class`
* `module`
* `session`

---

## Common Plugins

* `pytest-cov` → coverage
* `pytest-xdist` → parallel testing
* `pytest-mock` → mocking support

---

## Advantages

* Minimal boilerplate
* Scales from small to large projects
* Strong community support
* Works well with CI/CD

---

## When to Use pytest

Use it when:

* Writing unit tests
* Automating regression tests
* Working in modern Python projects

---