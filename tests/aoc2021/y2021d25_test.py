import aoc_cj.aoc2021.day25 as d

EXAMPLE_INPUT = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 58
