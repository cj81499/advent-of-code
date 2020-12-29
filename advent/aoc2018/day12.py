class Pots:
    def __init__(self, state: str, start_index):
        self._pots = {}
        for i, pot in enumerate(state):
            if pot == "#":
                self._pots[start_index + i] = True

    def __len__(self):
        return max(self._pots) - min(self._pots) + 1

    def __getitem__(self, position):
        return "#" if position in self._pots else "."

    def __str__(self):
        return "".join(["#" if x in self._pots else "." for x in range(min(self._pots), max(self._pots) + 1)])

    def first_pot_index(self):
        return min(self._pots.keys())

    def sum_of_pots_with_plants(self):
        return sum(self._pots)


def run(pots, rules, loops):
    prev_sum = 0
    prev_change = 0
    same_change_counter = 0

    for generation in range(loops):
        next_pots_state = ""
        for i in range(- 2,  len(pots) + 2):
            slice_of_five = "".join(
                [pots[pots.first_pot_index() + i + x] for x in range(-2, 3)])
            # print(str(i).rjust(2), slice_of_five, str(pots))
            next_pots_state += "#" if slice_of_five in rules else "."
        pots = Pots(next_pots_state, pots.first_pot_index() - 2)

        current_sum = pots.sum_of_pots_with_plants()
        current_change = current_sum - prev_sum
        if current_change == prev_change:
            same_change_counter += 1
            if same_change_counter > 10:  # If change is consistent, we found a pattern
                return (loops - (generation + 1)) * current_change + current_sum
        else:
            same_change_counter = 0
        prev_sum = current_sum
        prev_change = current_change
    return pots.sum_of_pots_with_plants()


def parse_input(txt):
    lines = txt.splitlines()
    initial_pots = Pots(lines[0][15:], 0)

    lines.pop(0)
    lines.pop(0)

    # Set of rules that make plants
    # Rules that don't make plants don't matter b/c no plant is the default for each generation
    rules = set(rule_txt[:5] for rule_txt in lines if rule_txt[-1] == "#")

    return initial_pots, rules


def parta(txt):
    pots, rules = parse_input(txt)
    return run(pots, rules, 20)


def partb(txt):
    pots, rules = parse_input(txt)
    return run(pots, rules, 50000000000)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
