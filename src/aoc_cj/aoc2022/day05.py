def parta(txt: str) -> str:
    stacks, moves = txt.split("\n\n")

    stacks_dict: dict[int, list[str]] = {}

    for line in stacks.splitlines():
        for stack_i, line_i in enumerate(range(1, len(line), 4), start=1):
            c = line[line_i]
            if c.isalpha():
                stacks_dict.setdefault(stack_i, []).append(c)

    for k in stacks_dict:
        stacks_dict[k] = list(reversed(stacks_dict[k]))

    for m in moves.splitlines():
        _, count, _, src, _, dest = m.split()
        for _ in range(int(count)):
            stacks_dict[int(dest)].append(stacks_dict[int(src)].pop())

    result = ""
    for i in range(1, max(stacks_dict) + 1):
        result += stacks_dict[i][-1]

    return result


def partb(txt: str) -> str:
    stacks, moves = txt.split("\n\n")

    stacks_dict: dict[int, list[str]] = {}

    for line in stacks.splitlines():
        for stack_i, line_i in enumerate(range(1, len(line), 4), start=1):
            c = line[line_i]
            if c.isalpha():
                stacks_dict.setdefault(stack_i, []).append(c)

    for k in stacks_dict:
        stacks_dict[k] = list(reversed(stacks_dict[k]))

    for m in moves.splitlines():
        _, count, _, src, _, dest = m.split()
        stacks_dict[int(dest)].extend(stacks_dict[int(src)][-int(count) :])
        for _ in range(int(count)):
            stacks_dict[int(src)].pop()

    result = ""
    for i in range(1, max(stacks_dict) + 1):
        result += stacks_dict[i][-1]

    return result


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
