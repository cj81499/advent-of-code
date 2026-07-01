import pytest

import aoc_cj.aoc2022.day19 as d

EXAMPLE_INPUT = (
    """
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
""".strip()
    .replace("\n  ", " ")
    .replace("\n\n", "\n")
)


@pytest.mark.parametrize(
    ("example", "expected"),
    zip(
        EXAMPLE_INPUT.splitlines(),
        (9, 12),
    ),
)
def test_simulate(example: str, expected: int) -> None:
    bp = d.Blueprint.parse(example)
    assert d.SimulationState(bp).run() == expected


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 3


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) is None
