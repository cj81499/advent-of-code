import unittest

import day11


class TestDay11(unittest.TestCase):
    def test_day11_is_valid_password(self):
        self.assertFalse(day11.is_valid_password("hijklmmn"))
        self.assertFalse(day11.is_valid_password("abbceffg"))
        self.assertFalse(day11.is_valid_password("abbcegjk"))
        self.assertTrue(day11.is_valid_password("abcdffaa"))
        self.assertTrue(day11.is_valid_password("ghjaabcc"))

    def test_day11_increment_password(self):
        self.assertEqual("b", day11.increment_password("a"))
        self.assertEqual("c", day11.increment_password("b"))
        self.assertEqual("d", day11.increment_password("c"))
        self.assertEqual("aa", day11.increment_password("z"))
        self.assertEqual("ab", day11.increment_password("aa"))
        self.assertEqual("ac", day11.increment_password("ab"))
        self.assertEqual("ad", day11.increment_password("ac"))
        self.assertEqual("zb", day11.increment_password("za"))
        self.assertEqual("zz", day11.increment_password("zy"))
        self.assertEqual("aaa", day11.increment_password("zz"))

    def test_day11_fast_increment_password(self):
        self.assertEqual("b", day11.fast_increment_password("a"))
        self.assertEqual("c", day11.fast_increment_password("b"))
        self.assertEqual("d", day11.fast_increment_password("c"))
        self.assertEqual("aa", day11.fast_increment_password("z"))
        self.assertEqual("ab", day11.fast_increment_password("aa"))
        self.assertEqual("ac", day11.fast_increment_password("ab"))
        self.assertEqual("ad", day11.fast_increment_password("ac"))
        self.assertEqual("zb", day11.fast_increment_password("za"))
        self.assertEqual("zz", day11.fast_increment_password("zy"))

        self.assertEqual("j", day11.fast_increment_password("i"))
        self.assertEqual("p", day11.fast_increment_password("o"))
        self.assertEqual("m", day11.fast_increment_password("l"))

        self.assertEqual("ja", day11.fast_increment_password("ib"))
        self.assertEqual("pa", day11.fast_increment_password("oa"))
        self.assertEqual("ma", day11.fast_increment_password("lz"))

        self.assertEqual("jaaaaaaaaa", day11.fast_increment_password("ibheqrmnad"))
        self.assertEqual("paaaaaaaaaa", day11.fast_increment_password("omnzvcpqgqe"))
        self.assertEqual("maaaaaaaaa", day11.fast_increment_password("lasdfupafj"))

    def test_day11_part1(self):
        self.assertEqual("abcdffaa", day11.next_valid_password("abcdefgh"))
        self.assertEqual("ghjaabcc", day11.next_valid_password("ghijklmn"))

    # def test_day11_part2(self):
    #     self.assertEqual(None, day11.part2([]))


if __name__ == "__main__":
    unittest.main()
