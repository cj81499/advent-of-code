import aoc_cj.aoc2016.day13 as d

EXAMPLE_SPACE = """
.#.####.##
..#..#...#
#....##...
###.#.###.
.##..#..#.
..##....#.
#...##.###
""".strip()


def test_is_wall():
    lines = EXAMPLE_SPACE.splitlines()
    fav_num = 10
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            assert lines[y][x] == "." if d.is_open(x, y, fav_num) else "#"


def test_a():
    assert d.parta("10", target_pos=(7, 4)) == 11
