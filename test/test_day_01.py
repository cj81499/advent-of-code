import path_fix
import day_01

INPUT_0 = 12
INPUT_1 = 14
INPUT_2 = 1969
INPUT_3 = 100756


def test_day_01_part1_0():
    assert day_01.fuel_req(INPUT_0) == 2


def test_day_01_part1_1():
    assert day_01.fuel_req(INPUT_1) == 2


def test_day_01_part1_2():
    assert day_01.fuel_req(INPUT_2) == 654


def test_day_01_part1_3():
    assert day_01.fuel_req(INPUT_3) == 33583


def test_day_01_part2_0():
    assert day_01.fuel_req_rec(INPUT_0) == 2


def test_day_01_part2_1():
    assert day_01.fuel_req_rec(INPUT_1) == 2


def test_day_01_part2_2():
    assert day_01.fuel_req_rec(INPUT_2) == 966


def test_day_01_part2_3():
    assert day_01.fuel_req_rec(INPUT_3) == 50346
