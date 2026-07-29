# sandbox-for-coding-agent

Small sandbox repo to validate coding agents that handle PRs.

It contains a minimal Python module (`calculator.py`) and its pytest suite
(`test_calculator.py`), plus a set of fixture PRs on top of `main`, each
crafted to exercise one specific path of a PR-review pipeline: a clean PR,
a lint-error PR, a hardcoded-secret PR, a failing-test PR, and a PR with an
unparseable (binary) diff.

Run checks locally with:

```
ruff check .
pytest
```
