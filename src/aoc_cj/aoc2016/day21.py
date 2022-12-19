import itertools
from collections import deque

INITIAL = "abcdefgh"
SCRAMBLED = "fbgdceah"


def swap(li, i, j):
    li = li.copy()
    li[i], li[j] = li[j], li[i]
    return li


def swap_position(pw, words):
    return swap(pw, int(words[2]), int(words[-1]))


def swap_letter(pw, words):
    return swap(pw, pw.index(words[2]), pw.index(words[-1]))


def rotate(li, n):
    d = deque(li)
    d.rotate(n)
    return list(d)


def rotate_left(pw, words):
    return rotate(pw, -int(words[-2]))


def rotate_right(pw, words):
    return rotate(pw, int(words[-2]))


def rotate_based(pw, words):
    i = pw.index(words[-1])
    return rotate(pw, 1 + i + (1 if i >= 4 else 0))


def reverse_positions(pw, words):
    x, y = int(words[2]), int(words[-1])
    return [*pw[:x], *reversed(pw[x : y + 1]), *pw[y + 1 :]]


def move_position(pw: list, words):
    pw = pw.copy()
    val = pw.pop(int(words[2]))
    pw.insert(int(words[-1]), val)
    return pw


OPS = {
    "swap position": swap_position,
    "swap letter": swap_letter,
    "rotate left": rotate_left,
    "rotate right": rotate_right,
    "rotate based": rotate_based,
    "reverse positions": reverse_positions,
    "move position": move_position,
}


def parta(txt: str, *, initial: str = INITIAL, backwards=False):
    pw = [*initial]
    ops = txt.splitlines()
    if backwards:
        ops = reversed(ops)
    for instruction in ops:
        words = instruction.split()
        op = OPS.get(" ".join(words[:2]))
        if not backwards:
            pw = op(pw, words)
        else:
            pw = list(next(p for p in itertools.permutations(pw) if pw == op(list(p), words)))
    return "".join(pw)


def partb(txt: str, *, initial: str = SCRAMBLED):
    return parta(txt, initial, backwards=True)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
