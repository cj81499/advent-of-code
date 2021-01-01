import unittest

import advent.aoc2018.day25 as day25


class TestDay25(unittest.TestCase):
    def test_day25_parta_0(self):
        s = """
0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0
""".strip().split("\n")
        self.assertEqual(2, day25.parta(s))

    def test_day25_parta_1(self):
        s = """
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
""".strip().split("\n")
        self.assertEqual(4, day25.parta(s))

    def test_day25_parta_2(self):
        s = """
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
""".strip().split("\n")
        self.assertEqual(3, day25.parta(s))

    def test_day25_parta_3(self):
        s = """
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
""".strip().split("\n")
        self.assertEqual(8, day25.parta(s))

    # def test_day25_partb(self):
    #     self.assertEqual(51, day25.remaining_immune_with_min_boost(s))


if __name__ == "__main__":
    unittest.main()
