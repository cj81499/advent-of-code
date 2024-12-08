import math
from collections import defaultdict


def part_1(txt: str, compare: tuple[int, int] = (61, 17)) -> int:
    return simulate(txt, compare)


def part_2(txt: str) -> int:
    return simulate(txt, None)


def simulate(txt: str, compare: tuple[int, int] | None) -> int:
    bots = defaultdict[int, set[int]](set)
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
    outputs = defaultdict[int, set[int]](set)
    while any(len(holding) == 2 for holding in bots.values()):
        new_bots = defaultdict[int, set[int]](set)
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
    return math.prod(outputs[n] for n in range(3))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
