# Tests (tests/)

This directory contains unit tests, integration tests, and test fixtures for the Agri-Arch-TR project.

## Running Tests

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## Test Structure

```text
tests/
├── unit/             # Unit tests for individual components
├── integration/      # Integration tests for system workflows
└── fixtures/         # Test data and mock objects
```

---
*Ensure all tests pass before submitting a pull request*
