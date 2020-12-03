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
    def test_day18_parta(self):
        self.assertEqual(1147, day18.parta(lines))

    def test_day18_partb(self):
        self.assertEqual(0, day18.partb(lines))


if __name__ == "__main__":
    unittest.main()
