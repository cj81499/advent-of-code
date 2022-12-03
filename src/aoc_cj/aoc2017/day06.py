def simulate(txt, partb=False):
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
    return cycles - seen[t] if partb else cycles


def parta(txt):
    return simulate(txt)


def partb(txt):
    return simulate(txt, partb=True)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
