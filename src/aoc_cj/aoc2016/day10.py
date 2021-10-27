from __future__ import annotations

from collections import defaultdict
from math import prod


def parta(txt: str, compare=(61, 17)):
    return simulate(txt, compare)


def partb(txt: str):
    return simulate(txt, None)


def simulate(txt, compare):
    bots = defaultdict(set)
    transitions = {}
    for line in txt.splitlines():
        words = line.split()
        nums = (int(x) for x in words if x.isnumeric())
        if words[0] == "value":
            val, bot_num = nums
            bots[bot_num].add(val)
        else:
            bot_num, low_to_num, high_to_num = nums
            low_to_type, high_to_type = words[5], words[10]
            assert bot_num not in transitions
            transitions[bot_num] = ((low_to_num, low_to_type), (high_to_num, high_to_type))
    outputs = defaultdict(set)
    while any(len(holding) == 2 for holding in bots.values()):
        new_bots = defaultdict(set)
        for bot_num, holding in bots.items():
            if len(holding) == 2:
                if compare is not None and holding == set(compare):
                    return bot_num
                low, high = min(holding), max(holding)
                low_to, high_to = transitions[bot_num]
                num, type = low_to
                (new_bots if type == "bot" else outputs)[num].add(low)
                num, type = high_to
                (new_bots if type == "bot" else outputs)[num].add(high)
            else:
                new_bots[bot_num].update(holding)
        bots = new_bots
    outputs = {k: next(iter(v)) for k, v in outputs.items()}
    return prod(outputs[n] for n in range(3))


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
