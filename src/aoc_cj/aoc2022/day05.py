from itertools import zip_longest

Stacks = dict[int, list[str]]


def parse(txt: str) -> tuple[str, Stacks]:
    stacks_str, moves = txt.split("\n\n")

    stacks = {
        int(s[0]): list(s[1:])
        for col in zip_longest(*stacks_str.splitlines(), fillvalue="")
        if (s := ("".join(reversed(col)).strip())).isalnum()
    }

    return moves, stacks


def top_of_stacks(stacks: Stacks) -> str:
    return "".join(stacks[i][-1] for i in range(1, max(stacks) + 1))


def parta(txt: str, reverse: bool = True) -> str:
    moves, stacks = parse(txt)

    for m in moves.splitlines():
        _, count, _, src, _, dest = m.split()
        move = stacks[int(src)][-int(count) :]
        stacks[int(dest)].extend(reversed(move) if reverse else move)
        stacks[int(src)] = stacks[int(src)][: -int(count)]

    return top_of_stacks(stacks)


def partb(txt: str) -> str:
    return parta(txt, False)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
