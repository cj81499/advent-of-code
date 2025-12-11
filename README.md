# Advent of Code

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cj81499/advent-of-code/main.svg)](https://results.pre-commit.ci/latest/github/cj81499/advent-of-code/main)
[![codecov](https://codecov.io/gh/cj81499/advent-of-code/branch/main/graph/badge.svg?token=C8KWW9KG6Q)](https://codecov.io/gh/cj81499/advent-of-code)

## Development

Install [uv](https://docs.astral.sh/uv/#getting-started)

```shell
# install the project and dependencies (note: this is done implicitly when you `uv run <COMMAND>`)
uv sync

# optionally, install git hooks via pre-commit
uv run pre-commit install
```

Make sure that [`aocd`](https://github.com/wimglenn/advent-of-code-data) knows
about your session token by putting it in `~/.config/aocd/token`.
You can "scrape" it from your browser's cookie storage by running:

```sh
uv run --with browser-cookie3 aocd-token
```

### Test

```shell
uv run pytest
```

Supports [aoc test runner](https://github.com/wimglenn/advent-of-code-data#verify-your-code-against-multiple-different-inputs).
