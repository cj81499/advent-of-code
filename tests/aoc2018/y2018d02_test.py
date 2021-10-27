import aoc_cj.aoc2018.day02 as d

EXAMPLE_INPUT_0 = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
""".strip()

EXAMPLE_INPUT_1 = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 12


def test_b():
    assert d.partb(EXAMPLE_INPUT_1) == "fgij"
