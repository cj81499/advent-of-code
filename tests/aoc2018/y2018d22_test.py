import advent.aoc2018.day22 as d

EXAMPLE_INPUT = """
depth: 510
target: 10,10
""".strip()


def test_example():
    depth = 510
    target = (10, 10)
    cave_system = d.CaveSystem(depth, target)
    r = cave_system.at(*d.CaveSystem.MOUTH)
    assert r.geologic_index == 0
    assert r.erosion_level == 510
    assert r.type == d.Type.ROCKY

    r = cave_system.at(1, 0)
    assert r.geologic_index == 16807
    assert r.erosion_level == 17317
    assert r.type == d.Type.WET

    r = cave_system.at(0, 1)
    assert r.geologic_index == 48271
    assert r.erosion_level == 8415
    assert r.type == d.Type.ROCKY

    r = cave_system.at(1, 1)
    assert r.geologic_index == 145722555
    assert r.erosion_level == 1805
    assert r.type == d.Type.NARROW

    r = cave_system.at(10, 10)
    assert r.geologic_index == 0
    assert r.erosion_level == 510
    assert r.type == d.Type.ROCKY

    assert str(cave_system) == EXAMPLE_CAVE_SYSTEM_STR


def test_a():
    assert d.parta(EXAMPLE_INPUT) == 114


EXAMPLE_CAVE_SYSTEM_STR = """
M=.|=.|.|=.|=|=.
.|=|=|||..|.=...
.==|....||=..|==
=.|....|.==.|==.
=|..==...=.|==..
=||.=.=||=|=..|=
|.=.===|||..=..|
|..==||=.|==|===
.=..===..=|.|||.
.======|||=|=.|=
.===|=|===T===||
=|||...|==..|=.|
=.=|=.=..=.||==|
||=|=...|==.=|==
|=.=||===.|||===
||.|==.|.|.||=||
""".strip()


def test_b():
    assert d.partb(EXAMPLE_INPUT) == 45
