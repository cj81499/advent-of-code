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


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == "7,3"


def test_b():
    assert d.partb(EXAMPLE_INPUT_1) == "6,4"
