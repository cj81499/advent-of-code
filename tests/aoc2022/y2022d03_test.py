import aoc_cj.aoc2022.day03 as d

EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT) == 157


def test_b() -> None:
    assert d.partb(EXAMPLE_INPUT) == 70
