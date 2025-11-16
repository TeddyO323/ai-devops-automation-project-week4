# **`task2_automated_testing/README.md`**

```markdown
# Task 2: Automated Testing (PyTorch Tool)

This task demonstrates automated testing for a PyTorch-based classification tool. It includes unit tests, integration tests, and pipeline validation using `pytest`. The tests ensure that the model, preprocessing utilities, and full prediction pipeline behave correctly and deterministically.

---

## Prerequisites

- Python 3.9+  
- PyTorch  
- NumPy  
- pytest  

Install dependencies via:

```bash
pip install -r requirements.txt
````

---

## Running the Tests

From the `task2_automated_testing/` directory:

```bash
python -m pytest -q tests
```

Expected outcome:

* Unit tests for the model and utilities pass
* Integration test validates the full pipeline
* Deterministic outputs for fixed random seeds
* Probability outputs sum to 1 per sample

---

## Test Details

1. **Model Tests** (`test_model.py`):

   * Forward pass shape validation
   * Deterministic output with same initialization

2. **Utility Tests** (`test_utils.py`):

   * Normalization correctness
   * Handling of constant columns without producing NaNs

3. **Pipeline Test** (`test_pipeline.py`):

   * End-to-end input preprocessing → inference → output probabilities
   * Output shapes and probability sums

---

## Notes

* The saved model fixture (`conftest.py`) initializes a small deterministic model for testing.
* These tests are fast, run on CPU, and provide full coverage for the main PyTorch backend.
* UI automation tests (Selenium `.side` files) are stored separately under `selenium/`.

---

## How to Extend

* Add negative tests for invalid input shapes or types.
* Add performance tests for inference speed.
* Add CI integration (GitHub Actions) to run tests on every push.

```

