import aoc_cj.aoc2016.day12 as d

EXAMPLE_INPUT = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
""".strip()


def test_part_1() -> None:
    c = d.AssemBunnyComputer(EXAMPLE_INPUT)
    c.run()
    assert c["a"] == 42
