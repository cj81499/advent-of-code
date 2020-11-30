import unittest

import path_fix
import day15


class TestDay15(unittest.TestCase):
    s = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip().splitlines()

    def test_day15_score_cookie(self):
        ingredients = [day15.Ingredient(x) for x in TestDay15.s]
        self.assertEqual(62842880, day15.score_cookie(ingredients, [44, 56]))

    def test_day15_part1(self):
        self.assertEqual(62842880, day15.part1(TestDay15.s))

    def test_day15_count_calories(self):
        ingredients = [day15.Ingredient(x) for x in TestDay15.s]
        self.assertEqual(500, day15.count_calories(ingredients, [40, 60]))

    def test_day15_part2(self):
        self.assertEqual(57600000, day15.part2(TestDay15.s))


if __name__ == "__main__":
    unittest.main()
