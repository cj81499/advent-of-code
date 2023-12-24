def simulate(txt, part_2=False):
    mem = list(map(int, txt.split()))
    seen = {}
    cycles = 0
    while (t := tuple(mem)) not in seen:
        seen[t] = cycles
        redistribute_idx = mem.index(max(mem))
        num_to_redistribute = mem[redistribute_idx]
        mem[redistribute_idx] = 0
        for i in range(num_to_redistribute):
            mem[(redistribute_idx + 1 + i) % len(mem)] += 1
        cycles += 1
    return cycles - seen[t] if part_2 else cycles


def part_1(txt):
    return simulate(txt)


def part_2(txt):
    return simulate(txt, part_2=True)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
