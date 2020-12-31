import advent.aoc2018.day07 as d

EXAMPLE_INPUT = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT) == "CABDFE"


def test_b():
    assert d.partb(EXAMPLE_INPUT, offset=0, helper_count=1) == 15
