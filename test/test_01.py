from test import path_fix
import day_01


def test_day01_part1():
    assert day_01.fuel_req(12) == 2
    assert day_01.fuel_req(14) == 2
    assert day_01.fuel_req(1969) == 654
    assert day_01.fuel_req(100756) == 33583


def test_day01_part2():
    assert day_01.fuel_req_rec(14) == 2
    assert day_01.fuel_req_rec(1969) == 966
    assert day_01.fuel_req_rec(100756) == 50346
