import aoc_cj.aoc2018.day07 as d

EXAMPLE_INPUT = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip()


def test_part_1():
    assert d.part_1(EXAMPLE_INPUT) == "CABDFE"


def test_part_2():
    assert d.part_2(EXAMPLE_INPUT, num_workers=2, base_duration=0) == 15
