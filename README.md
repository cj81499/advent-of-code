# Advent of Code

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cj81499/advent-of-code/main.svg)](https://results.pre-commit.ci/latest/github/cj81499/advent-of-code/main)

## Development

Install [poetry](https://python-poetry.org/docs/#installation)

```shell
poetry install      # install the project
pre-commit install  # install pre-commit git hook
```

Make sure that [aocd](https://github.com/wimglenn/advent-of-code-data) knows where to find your session token.
My personal preference is to put it in `~/.config/aocd/token`.

### Test

```shell
pytest tests    # run the tests
```

Supports [aoc test runner](https://github.com/wimglenn/advent-of-code-data#verify-your-code-against-multiple-different-inputs).
