import pytest

import aoc_cj.aoc2023.day20 as d

EXAMPLE_INPUT = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""".strip()

EXAMPLE_INPUT2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    (
        (EXAMPLE_INPUT, 32000000),
        (EXAMPLE_INPUT2, 11687500),
    ),
)
def test_part_1(example: str, expected: int) -> None:
    assert d.part_1(example) == expected
