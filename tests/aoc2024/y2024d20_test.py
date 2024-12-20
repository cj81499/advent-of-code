import aoc_cj.aoc2024.day20 as d

EXAMPLE_INPUT = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()


# @pytest.mark.parametrize()
def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, target_savings=65) == 0
    assert d.part_1(EXAMPLE_INPUT, target_savings=64) == 1


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) is None
