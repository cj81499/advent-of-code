import unittest
import day18


lines = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
""".strip().split("\n")


class TestDay18(unittest.TestCase):
    def test_day18_part1(self):
        self.assertEqual(1147, day18.part1(lines))

    def test_day18_part2(self):
        self.assertEqual(0, day18.part2(lines))


if __name__ == "__main__":
    unittest.main()
