import advent.aoc2015.day06 as d


def test_a():
    ALL_ON = "turn on 0,0 through 999,999"
    ALL_ON_COUNT = 1000 * 1000
    TOGGLE_FIRST_ROW = "toggle 0,0 through 999,0"
    FIRST_ROW_COUNT = 1000
    TURN_OFF_MIDDLE = "turn off 499,499 through 500,500"
    MIDDLE_COUNT = 4
    assert d.parta(ALL_ON) == ALL_ON_COUNT
    assert d.parta(TOGGLE_FIRST_ROW) == FIRST_ROW_COUNT
    assert d.parta(f"{ALL_ON}\n{TOGGLE_FIRST_ROW}") == ALL_ON_COUNT - FIRST_ROW_COUNT
    assert d.parta(TURN_OFF_MIDDLE) == 0
    assert d.parta(f"{ALL_ON}\n{TURN_OFF_MIDDLE}") == ALL_ON_COUNT - MIDDLE_COUNT


def test_b():
    assert d.partb("turn on 0,0 through 0,0") == 1
    assert d.partb("toggle 0,0 through 999,999") == 2000000
