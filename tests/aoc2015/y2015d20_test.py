import aoc_cj.aoc2015.day20 as d


def test_part_1() -> None:
    # 1000 is for large enough to generate the first 10 houses
    presents = d.presents_for_houses(1000, 10)
    assert presents[1] == 10
    assert presents[2] == 30
    assert presents[3] == 40
    assert presents[4] == 70
    assert presents[5] == 60
    assert presents[6] == 120
    assert presents[7] == 80
    assert presents[8] == 150
    assert presents[9] == 130
