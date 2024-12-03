import aoc_cj.aoc2024.day03 as d

EXAMPLE_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def test_part_1() -> None:
    assert d.part_1(EXAMPLE_INPUT) == 161


EXAMPLE_INPUT_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_part_2() -> None:
    assert d.part_2(EXAMPLE_INPUT_2) == 48
