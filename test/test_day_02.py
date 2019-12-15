import path_fix

from test_intcode_interpreter import run_intcode_test


def test_day_02_part1_0():
    run_intcode_test(
        (1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50),
        (3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50)
    )


def test_day_02_part1_1():
    run_intcode_test(
        (1, 0, 0, 0, 99),
        (2, 0, 0, 0, 99)
    )


def test_day_02_part1_2():
    run_intcode_test(
        (2, 3, 0, 3, 99),
        (2, 3, 0, 6, 99)
    )


def test_day_02_part1_3():
    run_intcode_test(
        (2, 4, 4, 5, 99, 0),
        (2, 4, 4, 5, 99, 9801)
    )


def test_day_02_part1_4():
    run_intcode_test(
        (1, 1, 1, 4, 99, 5, 6, 0, 99),
        (30, 1, 1, 4, 2, 5, 6, 0, 99)
    )
