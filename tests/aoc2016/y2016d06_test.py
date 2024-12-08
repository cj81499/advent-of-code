import aoc_cj.aoc2016.day06 as d

EXAMPLE_INPUT = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""".strip()


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == "easter"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT) == "advent"
