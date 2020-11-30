import unittest

import path_fix
import day06


class TestDay06(unittest.TestCase):
    def test_day06_part1(self):
        ALL_ON = "turn on 0,0 through 999,999"
        ALL_ON_COUNT = 1000 * 1000
        TOGGLE_FIRST_ROW = "toggle 0,0 through 999,0"
        FIRST_ROW_COUNT = 1000
        TURN_OFF_MIDDLE = "turn off 499,499 through 500,500"
        MIDDLE_COUNT = 4
        self.assertEqual(day06.part1([ALL_ON]), ALL_ON_COUNT)
        self.assertEqual(day06.part1([TOGGLE_FIRST_ROW]), FIRST_ROW_COUNT)
        self.assertEqual(day06.part1([ALL_ON, TOGGLE_FIRST_ROW]), ALL_ON_COUNT - FIRST_ROW_COUNT)  # noqa
        self.assertEqual(day06.part1([TURN_OFF_MIDDLE]), 0)
        self.assertEqual(day06.part1([ALL_ON, TURN_OFF_MIDDLE]), ALL_ON_COUNT - MIDDLE_COUNT)  # noqa

    def test_day06_part2(self):
        self.assertEqual(day06.part2(["turn on 0,0 through 0,0"]), 1)
        self.assertEqual(day06.part2(["toggle 0,0 through 999,999"]), 2000000)


if __name__ == "__main__":
    unittest.main()
