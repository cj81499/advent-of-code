import advent.aoc2020.day10 as d

EXAMPLE_INPUT_0 = """
16
10
15
5
1
11
7
19
6
12
4
""".strip()

EXAMPLE_INPUT_1 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()


def test_a():
    assert d.parta(EXAMPLE_INPUT_0) == 7 * 5
    assert d.parta(EXAMPLE_INPUT_1) == 22 * 10


def test_b():
    assert d.partb(EXAMPLE_INPUT_0) == 8
    assert d.partb(EXAMPLE_INPUT_1) == 19208
