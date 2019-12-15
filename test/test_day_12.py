import path_fix
import day_12

INPUT_1 = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".splitlines()

INPUT_2 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""".splitlines()


def test_day_12_part1_parse():
    assert day_12.parse_moons(INPUT_1) == [
        day_12.Moon(-1, 0, 2),
        day_12.Moon(2, -10, -7),
        day_12.Moon(4, -8, 8),
        day_12.Moon(3, 5, -1),
    ]


def test_day_12_part1_step():
    expected = [
        day_12.Moon(2, 1, -3, day_12.Vector((-3, -2, 1))),
        day_12.Moon(1, -8, 0, day_12.Vector((-1, 1, 3))),
        day_12.Moon(3, -6, 1, day_12.Vector((3, 2, -3))),
        day_12.Moon(2, 0, 4, day_12.Vector((1, -1, -1))),
    ]
    moons = step_helper(INPUT_1, 10)
    assert moons == expected


def test_day_12_part1_energy_0():
    moons = step_helper(INPUT_1, 10)
    assert day_12.total_energy(moons) == 179


def test_day_12_part1_energy_1():
    moons = step_helper(INPUT_2, 100)
    assert day_12.total_energy(moons) == 1940


def step_helper(str, step_count: int):
    moons = day_12.parse_moons(str)
    for i in range(step_count):
        day_12.step(moons)
    return moons


# def test_day_12_part2_0():
#     assert day_12.part2([]) is None
