import unittest

import advent.aoc2018.day04 as day04
import advent.aoc2018.day04 as day04_polished

txt_unsorted = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:50] wakes up
[1518-11-01 00:55] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:45] falls asleep
[1518-11-02 00:40] falls asleep
[1518-11-04 00:36] falls asleep
[1518-11-03 00:24] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-03 00:29] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:55] wakes up""".split("\n")

txt_presorted = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split("\n")


class TestDay04(unittest.TestCase):

    def test_day04_parta_unsorted(self):
        self.assertEqual(240, day04.parta(day04.events_list(txt_unsorted)))

    def test_day04_partb_unsorted(self):
        self.assertEqual(4455, day04.partb(day04.events_list(txt_unsorted)))

    def test_day04_parta_presorted(self):
        self.assertEqual(240, day04.parta(day04.events_list(txt_presorted)))

    def test_day04_partb_presorted(self):
        self.assertEqual(4455, day04.partb(day04.events_list(txt_presorted)))

    def test_day04_unsorted_polished(self):
        self.assertEqual((240, 4455), day04_polished.run(
            day04_polished.events_list(txt_unsorted)))

    def test_day04_presorted_polished(self):
        self.assertEqual((240, 4455), day04_polished.run(
            day04_polished.events_list(txt_presorted)))


if __name__ == "__main__":
    unittest.main()
