import unittest

import path_fix
import day12


class TestDay12(unittest.TestCase):
    def test_day12_part1(self):
        self.assertEqual(6, day12.sum_of_all_numbers([1, 2, 3]))
        self.assertEqual(6, day12.sum_of_all_numbers({"a": 2, "b": 4}))
        self.assertEqual(3, day12.sum_of_all_numbers([[[3]]]))
        self.assertEqual(3, day12.sum_of_all_numbers({"a": {"b": 4}, "c": -1}))
        self.assertEqual(0, day12.sum_of_all_numbers({"a": [-1, 1]}))
        self.assertEqual(0, day12.sum_of_all_numbers([-1, {"a": 1}]))
        self.assertEqual(0, day12.sum_of_all_numbers([]))
        self.assertEqual(0, day12.sum_of_all_numbers({}))

    def test_day12_part2(self):
        self.assertEqual(6, day12.sum_of_all_numbers([1, 2, 3], ignore_red=True))
        self.assertEqual(4, day12.sum_of_all_numbers([1, {"c": "red", "b": 2}, 3], ignore_red=True))
        self.assertEqual(0, day12.sum_of_all_numbers({"d": "red", "e": [1, 2, 3, 4], "f": 5}, ignore_red=True))
        self.assertEqual(6, day12.sum_of_all_numbers([1, "red", 5], ignore_red=True))


if __name__ == "__main__":
    unittest.main()
