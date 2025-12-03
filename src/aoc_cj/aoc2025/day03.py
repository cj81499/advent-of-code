def part_1(txt: str) -> int:
    s = 0
    for battery_bank in txt.splitlines():
        max_joltage = 0
        for i, c1 in enumerate(battery_bank):
            for c2 in battery_bank[i + 1 :]:
                max_joltage = max(max_joltage, int(c1 + c2))
        s += max_joltage
    return s


def max_j(battery_bank: str, *, width: int = 2) -> int:
    indices = []
    start = 0
    for i in range(width):
        min_idx = start
        max_idx = len(battery_bank) - width + i + 1
        best_idx = min_idx
        for j in range(min_idx + 1, max_idx):
            if battery_bank[j] > battery_bank[best_idx]:
                best_idx = j
        indices.append(best_idx)
        start = best_idx + 1

    return int("".join(battery_bank[i] for i in indices))


def part_2(txt: str) -> int:
    return sum(max_j(battery_bank, width=12) for battery_bank in txt.splitlines())


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
