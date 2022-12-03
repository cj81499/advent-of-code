def simulate(txt, partb=False):
    instructions = [int(line) for line in txt.splitlines()]
    ip = 0
    steps = 0
    while ip < len(instructions):
        new_ip = ip + instructions[ip]
        instructions[ip] += -1 if partb and instructions[ip] >= 3 else 1
        ip = new_ip
        steps += 1
    return steps


def parta(txt):
    return simulate(txt)


def partb(txt):
    return simulate(txt, partb)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
