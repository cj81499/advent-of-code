import advent.aoc2016.day08 as d

AFTER_1 = """
###....
###....
.......
""".replace(".", " ").strip()

AFTER_2 = """
#.#....
###....
.#.....
""".replace(".", " ").strip()

AFTER_3 = """
....#.#
###....
.#.....
""".replace(".", " ").strip()

AFTER_4 = """
.#..#.#
#.#....
.#.....
""".replace(".", " ").strip()


def test_a():
    screen = d.create_screen(7, 3)
    d.apply_instruction(screen, "rect 3x2")
    assert d.screen_to_str(screen) == AFTER_1
    d.apply_instruction(screen, "rotate column x=1 by 1")
    assert d.screen_to_str(screen) == AFTER_2
    d.apply_instruction(screen, "rotate row y=0 by 4")
    assert d.screen_to_str(screen) == AFTER_3
    d.apply_instruction(screen, "rotate column x=1 by 1")
    assert d.screen_to_str(screen) == AFTER_4
