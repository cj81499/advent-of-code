import unittest

import day22

cave = day22.Cave(510, (10, 10))


class TestDay22(unittest.TestCase):
    def test_day22_parta(self):
        self.assertEqual(114, cave.risk_level())

    def test_day22_partb(self):
        self.assertEqual(45, cave.fastest_time_to_target())


if __name__ == "__main__":
    unittest.main()
