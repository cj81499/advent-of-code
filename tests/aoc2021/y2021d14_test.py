import itertools

import aoc_cj.aoc2021.day14 as d

EXAMPLE_INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


def test_step():
    polymer, rules = d.parse(EXAMPLE_INPUT)
    assert polymer == "NNCB"
    for start, end in itertools.pairwise(
        (
            polymer,
            "NCNBCHB",
            "NBCCNBBBCBHCB",
            "NBBBCNCCNBBNBNBBCHBHHBCHB",
            "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB",
        )
    ):
        assert d.step(start, rules) == end


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == 1588


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT) == 2188189693529
