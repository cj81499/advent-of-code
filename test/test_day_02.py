from src.intcode_interpreter import run_intcode_program


def test_part1_0() -> None:
    assert run_intcode_program(
        (1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50),
    ) == (3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50)


def test_part1_1() -> None:
    assert run_intcode_program(
        (1, 0, 0, 0, 99),
    ) == (2, 0, 0, 0, 99)


def test_part1_2() -> None:
    assert run_intcode_program(
        (2, 3, 0, 3, 99),
    ) == (2, 3, 0, 6, 99)


def test_part1_3() -> None:
    assert run_intcode_program(
        (2, 4, 4, 5, 99, 0),
    ) == (2, 4, 4, 5, 99, 9801)


def test_part1_4() -> None:
    assert run_intcode_program(
        (1, 1, 1, 4, 99, 5, 6, 0, 99),
    ) == (30, 1, 1, 4, 2, 5, 6, 0, 99)
