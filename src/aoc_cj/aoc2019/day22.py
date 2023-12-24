def deck_of_size(n):
    return [x for x in range(n)]


def deal_into_new_stack(deck):
    return list(reversed(deck))


def cut(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    new_deck = [None] * len(deck)
    for i, x in enumerate(deck):
        new_deck[(i * n) % len(new_deck)] = x
    return new_deck


def perform_shuffle(txt: str, deck_size=10007, repeat=1):
    deck = deck_of_size(deck_size)
    for _ in range(repeat):
        for instruction in txt.splitlines():
            if instruction == "deal into new stack":
                deck = deal_into_new_stack(deck)
            elif instruction.startswith("cut "):
                deck = cut(deck, int(instruction.split()[-1]))
            elif instruction.startswith("deal with increment "):
                deck = deal_with_increment(deck, int(instruction.split()[-1]))
            else:
                print("unrecognized shuffle instruction:", instruction)
                exit(1)
    return deck


def part_1(txt: str):
    return perform_shuffle(txt).index(2019)


def part_2(txt: str):
    pass


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
