import unittest

import path_fix
import day14


class TestDay14(unittest.TestCase):
    def test_day14_part1(self):
        self.assertEqual(1120, day14.max_distance_after_t("""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip().splitlines(), 1000))

    def test_day14_part2(self):
        self.assertEqual(689, day14.max_points_after_t("""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip().splitlines(), 1000))


if __name__ == "__main__":
    unittest.main()
