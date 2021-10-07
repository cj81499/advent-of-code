import advent.aoc2016.day23 as d

EXAMPLE_INPUT = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
""".strip()


def test_a():
    c = d.Day23AssemBunnyComputer(EXAMPLE_INPUT)
    c.run()
    assert c["a"] == 3
