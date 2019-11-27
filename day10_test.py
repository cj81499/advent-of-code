import unittest

import day10


class TestDay10(unittest.TestCase):
    def test_day10(self):
        self.assertEqual("11", day10.look_and_say("1", 1))
        self.assertEqual("21", day10.look_and_say("1", 2))
        self.assertEqual("1211", day10.look_and_say("1", 3))
        self.assertEqual("111221", day10.look_and_say("1", 4))
        self.assertEqual("312211", day10.look_and_say("1", 5))
        self.assertEqual("13112221", day10.look_and_say("1", 6))
        self.assertEqual("1113213211", day10.look_and_say("1", 7))
        self.assertEqual("31131211131221", day10.look_and_say("1", 8))
        self.assertEqual("13211311123113112211", day10.look_and_say("1", 9))
        self.assertEqual("11131221133112132113212221", day10.look_and_say("1", 10))


if __name__ == "__main__":
    unittest.main()
