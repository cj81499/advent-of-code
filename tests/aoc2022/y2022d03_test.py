import aoc_cj.aoc2022.day03 as d

EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 157


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == 70
