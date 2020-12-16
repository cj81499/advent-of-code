# Advent Of Code

[![GitHub Super-Linter](https://github.com/cj81499/advent-of-code/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

## Development

### Create (and activate) a virtual environment

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### Install the project

```shell
pip install -e .
```

Make sure that [aocd](https://github.com/wimglenn/advent-of-code-data) knows where to find your session token.

### Test

```shell
pytest tests
```

Supports [aoc test runner](https://github.com/wimglenn/advent-of-code-data#verify-your-code-against-multiple-different-inputs).
