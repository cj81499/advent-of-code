import pytest

import advent.aoc2016.day09 as d


@pytest.mark.parametrize("compressed, length", [
    ("ADVENT", 6),
    ("A(1x5)BC", 7),
    ("(3x3)XYZ", 9),
    ("A(2x2)BCD(2x2)EFG", 11),
    ("(6x1)(1x3)A", 6),
    ("X(8x2)(3x3)ABCY", 18),
])
def test_a(compressed, length):
    assert d.parta(compressed) == length


@pytest.mark.parametrize("compressed, length", [
    ("(3x3)XYZ", len("XYZXYZXYZ")),
    ("X(8x2)(3x3)ABCY", len("XABCABCABCABCABCABCY")),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445)
])
def test_b(compressed, length):
    assert d.partb(compressed) == length
