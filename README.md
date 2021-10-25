# Advent of Code

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cj81499/advent-of-code/main.svg)](https://results.pre-commit.ci/latest/github/cj81499/advent-of-code/main)

## Development

### Create (and activate) a virtual environment

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install the project

```shell
pip install -e .   # install the python project
pre-commit install # install pre-commit git hook
```

Make sure that [aocd](https://github.com/wimglenn/advent-of-code-data) knows where to find your session token.
My personal preference is to put it in `~/.config/aocd/token`.

### Test

```shell
pytest tests
```

Supports [aoc test runner](https://github.com/wimglenn/advent-of-code-data#verify-your-code-against-multiple-different-inputs).
