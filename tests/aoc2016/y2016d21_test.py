import aoc_cj.aoc2016.day21 as d

EXAMPLE_INPUT = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT, initial="abcde") == "decab"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT, initial="decab") == "abcde"
