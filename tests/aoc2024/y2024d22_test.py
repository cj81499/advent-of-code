import more_itertools as mi

import aoc_cj.aoc2024.day22 as d

EXAMPLE_INPUT1 = """
1
10
100
2024
""".strip()

EXAMPLE_INPUT2 = """
1
2
3
2024
""".strip()


def test_generate_secrets() -> None:
    assert mi.take(10, d.secret_generator(123)) == [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT1) == 37327623


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT2) == 23
