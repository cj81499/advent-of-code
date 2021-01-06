import pytest

import advent.aoc2018.day25 as d

EXAMPLE_INPUT_0 = """
0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0
""".strip()

EXAMPLE_INPUT_1 = """
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
""".strip()


EXAMPLE_INPUT_2 = """
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
""".strip()


EXAMPLE_INPUT_3 = """
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
""".strip()


@pytest.mark.parametrize("input, expected", [
    (EXAMPLE_INPUT_0, 2),
    (EXAMPLE_INPUT_1, 4),
    (EXAMPLE_INPUT_2, 3),
    (EXAMPLE_INPUT_3, 8),
])
def test_a(input, expected):
    assert d.parta(input) == expected
    assert d.parta(input) == expected
    assert d.parta(input) == expected
    assert d.parta(input) == expected
