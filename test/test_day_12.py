import src.day_12 as d

INPUT_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".splitlines()

INPUT_2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""".splitlines()


def test_day_12_part1_parse():
    assert d.parse_moons(INPUT_1) == [
        d.Moon(-1, 0, 2),
        d.Moon(2, -10, -7),
        d.Moon(4, -8, 8),
        d.Moon(3, 5, -1),
    ]


def test_day_12_part1_step():
    expected = [
        d.Moon(2, 1, -3, d.Vector((-3, -2, 1))),
        d.Moon(1, -8, 0, d.Vector((-1, 1, 3))),
        d.Moon(3, -6, 1, d.Vector((3, 2, -3))),
        d.Moon(2, 0, 4, d.Vector((1, -1, -1))),
    ]
    moons = step_helper(INPUT_1, 10)
    assert moons == expected


def test_day_12_part1_energy_0():
    moons = step_helper(INPUT_1, 10)
    assert d.total_energy(moons) == 179


def test_day_12_part1_energy_1():
    moons = step_helper(INPUT_2, 100)
    assert d.total_energy(moons) == 1940


def step_helper(str, step_count: int):
    moons = d.parse_moons(str)
    for i in range(step_count):
        d.step(moons)
    return moons


# def test_day_12_part2_0():
#     assert d.part2([]) is None
