import pytest

import aoc_cj.aoc2024.day14 as d

EXAMPLE_INPUT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()


@pytest.mark.parametrize(
    ("after", "expected"),
    (
        (1, complex(4, 1)),
        (2, complex(6, 5)),
        (3, complex(8, 2)),
        (4, complex(10, 6)),
        (5, complex(1, 3)),
    ),
)
def test_robot_move(after: int, expected: complex) -> None:
    r = d.Robot(p=complex(2, 4), v=complex(2, -3))
    assert r.after(after, width=11, height=7) == expected


@pytest.mark.parametrize(
    ("p", "expected"),
    (
        (6 + 0j, d.Quadrant.TOP_RIGHT),
        (9 + 0j, d.Quadrant.TOP_RIGHT),
        (0 + 2j, d.Quadrant.TOP_LEFT),
        (1 + 3j, None),
        (2 + 3j, None),
        (5 + 4j, None),
        (3 + 5j, d.Quadrant.BOTTOM_LEFT),
        (4 + 5j, d.Quadrant.BOTTOM_LEFT),
        (1 + 6j, d.Quadrant.BOTTOM_LEFT),
        (6 + 6j, d.Quadrant.BOTTOM_RIGHT),
    ),
)
def test_quadrant(p: complex, expected: d.Quadrant | None) -> None:
    assert d.quadrant(p, width=11, height=7) == expected


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, width=11, height=7) == 12
