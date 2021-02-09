import advent.aoc2016.day08 as d

AFTER_1 = """
###....
###....
.......
""".strip()

AFTER_2 = """
#.#....
###....
.#.....
""".strip()

AFTER_3 = """
....#.#
###....
.#.....
""".strip()

AFTER_4 = """
.#..#.#
#.#....
.#.....
""".strip()


def test_a():
    screen = d.create_screen(7, 3)
    d.apply_instruction(screen, "rect 3x2")
    assert d.screen_to_str(screen).replace(" ", ".") == AFTER_1
    d.apply_instruction(screen, "rotate column x=1 by 1")
    assert d.screen_to_str(screen).replace(" ", ".") == AFTER_2
    d.apply_instruction(screen, "rotate row y=0 by 4")
    assert d.screen_to_str(screen).replace(" ", ".") == AFTER_3
    d.apply_instruction(screen, "rotate column x=1 by 1")
    assert d.screen_to_str(screen).replace(" ", ".") == AFTER_4
