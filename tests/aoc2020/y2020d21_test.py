import aoc_cj.aoc2020.day21 as d

EXAMPLE_INPUT = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 5


def test_b():
    assert d.partb(EXAMPLE_INPUT) == "mxmxvkd,sqjhc,fvjkl"
