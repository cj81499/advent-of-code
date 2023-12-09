import pytest

import aoc_cj.aoc2023.day08 as d

EXAMPLE_INPUT_1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()

EXAMPLE_INPUT_2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()

EXAMPLE_INPUT_3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip()


@pytest.mark.parametrize(
    ("example_input", "expected"),
    (
        (EXAMPLE_INPUT_1, 2),
        (EXAMPLE_INPUT_2, 6),
    ),
)
def test_a(example_input: str, expected: int) -> None:
    assert d.parta(example_input) == expected


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT_3) == 6
