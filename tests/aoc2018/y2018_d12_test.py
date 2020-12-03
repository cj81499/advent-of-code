import unittest

import advent.aoc2018.day12 as day12


class TestDay12(unittest.TestCase):
    def test_day12_parta(self):
        input_lines = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".strip().split("\n")

        initial_pots = day12.Pots(input_lines[0][15:], 0)

        input_lines.pop(0)
        input_lines.pop(0)

        # Set of rules that make plants
        # Rules that don't make plants don't matter b/c no plant is the default for each generation
        rules = set([rule_txt[:5]
                     for rule_txt in input_lines if rule_txt[-1] == "#"])

        print(rules)
        self.assertEqual(325, day12.run(initial_pots, rules, 20))


if __name__ == "__main__":
    unittest.main()
