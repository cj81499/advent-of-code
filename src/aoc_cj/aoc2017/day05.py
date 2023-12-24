def simulate(txt, part_2=False):
    instructions = [int(line) for line in txt.splitlines()]
    ip = 0
    steps = 0
    while ip < len(instructions):
        new_ip = ip + instructions[ip]
        instructions[ip] += -1 if part_2 and instructions[ip] >= 3 else 1
        ip = new_ip
        steps += 1
    return steps


def part_1(txt):
    return simulate(txt)


def part_2(txt):
    return simulate(txt, part_2)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
