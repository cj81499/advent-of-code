import aoc_cj.aoc2022.day09 as d

EXAMPLE_INPUT_1 = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()

EXAMPLE_INPUT_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()


def test_pull() -> None:
    assert d.pull(d.ORIGIN, d.ORIGIN) == d.ORIGIN

    assert d.pull(1 + 0j, d.ORIGIN) == d.ORIGIN
    assert d.pull(-1 + 0j, d.ORIGIN) == d.ORIGIN
    assert d.pull(0 + 1j, d.ORIGIN) == d.ORIGIN
    assert d.pull(0 - 1j, d.ORIGIN) == d.ORIGIN

    assert d.pull(2 + 0j, d.ORIGIN) == 1 + 0j
    assert d.pull(-2 + 0j, d.ORIGIN) == -1 + 0j
    assert d.pull(0 + 2j, d.ORIGIN) == 0 + 1j
    assert d.pull(0 - 2j, d.ORIGIN) == 0 - 1j

    # up 1, right 2
    assert d.pull(2 + 1j, d.ORIGIN) == 1 + 1j
    # up 2, right 1
    assert d.pull(1 + 2j, d.ORIGIN) == 1 + 1j

    # down 1, right 2
    assert d.pull(2 - 1j, d.ORIGIN) == 1 - 1j
    # down 2, right 1
    assert d.pull(1 - 2j, d.ORIGIN) == 1 - 1j

    assert d.pull(-2 + 1j, d.ORIGIN) == -1 + 1j
    assert d.pull(-2 - 1j, d.ORIGIN) == -1 - 1j
    assert d.pull(-1 + 2j, d.ORIGIN) == -1 + 1j
    assert d.pull(-1 - 2j, d.ORIGIN) == -1 - 1j


def test_a() -> None:
    assert d.parta(EXAMPLE_INPUT_1) == 13


def test_b() -> None:
    print("EXAMPLE 1")
    assert d.partb(EXAMPLE_INPUT_1) == 1

    print("EXAMPLE 2")
    assert d.partb(EXAMPLE_INPUT_2) == 36
