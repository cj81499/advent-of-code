# Advent of Code

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cj81499/advent-of-code/main.svg)](https://results.pre-commit.ci/latest/github/cj81499/advent-of-code/main)
[![codecov](https://codecov.io/gh/cj81499/advent-of-code/branch/main/graph/badge.svg?token=C8KWW9KG6Q)](https://codecov.io/gh/cj81499/advent-of-code)

## Development

Install [pdm](https://pdm-project.org/latest/)

```shell
# optionally, create a virtual environment using python 3.12
# if you skip this, pdm will use the system default python version
pdm venv create $(which python3.12)

# install the project
pdm install

# optionally, install git hooks via pre-commit
pdm run pre-commit install
```

Make sure that [aocd](https://github.com/wimglenn/advent-of-code-data) knows where to find your session token.
My personal preference is to put it in `~/.config/aocd/token`.

### Test

```shell
pdm run pytest tests
```

Supports [aoc test runner](https://github.com/wimglenn/advent-of-code-data#verify-your-code-against-multiple-different-inputs).
