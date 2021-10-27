import aoc_cj.aoc2015.day12 as d


def test_a():
    assert d.sum_of_all_numbers([1, 2, 3]) == 6
    assert d.sum_of_all_numbers({"a": 2, "b": 4}) == 6
    assert d.sum_of_all_numbers([[[3]]]) == 3
    assert d.sum_of_all_numbers({"a": {"b": 4}, "c": -1}) == 3
    assert d.sum_of_all_numbers({"a": [-1, 1]}) == 0
    assert d.sum_of_all_numbers([-1, {"a": 1}]) == 0
    assert d.sum_of_all_numbers([]) == 0
    assert d.sum_of_all_numbers({}) == 0


def test_b():
    assert d.sum_of_all_numbers([1, 2, 3], ignore_red=True) == 6
    assert d.sum_of_all_numbers([1, {"c": "red", "b": 2}, 3], ignore_red=True) == 4
    assert d.sum_of_all_numbers({"d": "red", "e": [1, 2, 3, 4], "f": 5}, ignore_red=True) == 0
    assert d.sum_of_all_numbers([1, "red", 5], ignore_red=True) == 6
