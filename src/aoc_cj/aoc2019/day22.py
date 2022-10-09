DEAL_INTO_NEW_STACK = "deal into new stack"
CUT_N_CARDS = "cut "
DEAL_WITH_INCREMENT_N = "deal with increment "


def deal_into_new_stack(deck):
    return tuple(reversed(deck))


def cut(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment(deck, n):
    new_deck = [None] * len(deck)
    for i, card in enumerate(deck):
        new_deck[(i * n) % len(new_deck)] = card
    return tuple(new_deck)


def shuffle(txt: str, deck_size: int):
    deck = list(range(deck_size))
    for move in txt.splitlines():
        if move == DEAL_INTO_NEW_STACK:
            deck = deal_into_new_stack(deck)
        elif move.startswith(CUT_N_CARDS):
            deck = cut(deck, int(move.split()[-1]))
        elif move.startswith(DEAL_WITH_INCREMENT_N):
            deck = deal_with_increment(deck, int(move.split()[-1]))
    return deck


def parta(txt: str):
    return shuffle(txt, 10007).index(2019)


def partb(txt: str):
    return None


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
