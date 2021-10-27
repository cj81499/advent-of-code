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


def test_a():
    assert d.parta(EXAMPLE_INPUT) == "easter"


def test_b():
    assert d.partb(EXAMPLE_INPUT) == "advent"
