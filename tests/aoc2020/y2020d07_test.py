import pytest

import aoc_cj.aoc2020.day07 as d

EXAMPLE_INPUT_0 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip()

RULES_0 = d.bag_rules(EXAMPLE_INPUT_0)

EXAMPLE_INPUT_1 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip()


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("bright white", True),
        ("muted yellow", True),
        ("dark orange", True),
        ("light red", True),
        ("shiny gold", False),
        ("dark olive", False),
        ("vibrant plum", False),
        ("faded blue", False),
        ("dotted black", False),
    ],
)
def test_can_hold_shiny_gold(example: str, expected) -> None:
    assert expected == d.can_hold_shiny_gold(RULES_0, example)


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT_0) == 4


@pytest.mark.parametrize(
    ("example", "expected"),
    [
        ("faded blue", 0),
        ("dotted black", 0),
        ("vibrant plum", 11),
        ("dark olive", 7),
    ],
)
def test_number_of_bags_inside_of(example: str, expected) -> None:
    assert expected == d.number_of_bags_inside_of(RULES_0, example)


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_0) == 32
    assert d.part_2(EXAMPLE_INPUT_1) == 126
