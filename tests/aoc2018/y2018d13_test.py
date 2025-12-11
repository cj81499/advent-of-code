import aoc_cj.aoc2018.day13 as d

EXAMPLE_INPUT_0 = r"""
/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
""".strip()

EXAMPLE_INPUT_1 = r"""
/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_0) == "7,3"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_1) == "6,4"
