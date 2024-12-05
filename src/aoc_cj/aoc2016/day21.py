import itertools
from collections import deque
from collections.abc import Callable, Mapping, Sequence
from typing import TypeVar

INITIAL = "abcdefgh"
SCRAMBLED = "fbgdceah"

StrSeq = list[str] | tuple[str, ...]


def swap(li: StrSeq, i: int, j: int) -> list[str]:
    li = list(li)
    li[i], li[j] = li[j], li[i]
    return li


def swap_position(pw: StrSeq, words: StrSeq) -> list[str]:
    return swap(pw, int(words[2]), int(words[-1]))


def swap_letter(pw: StrSeq, words: StrSeq) -> list[str]:
    return swap(pw, pw.index(words[2]), pw.index(words[-1]))


_T = TypeVar("_T")


def rotate(li: Sequence[_T], n: int) -> list[_T]:
    d = deque(li)
    d.rotate(n)
    return list(d)


def rotate_left(pw: StrSeq, words: StrSeq) -> list[str]:
    return rotate(pw, -int(words[-2]))


def rotate_right(pw: StrSeq, words: StrSeq) -> list[str]:
    return rotate(pw, int(words[-2]))


def rotate_based(pw: StrSeq, words: StrSeq) -> list[str]:
    i = pw.index(words[-1])
    return rotate(pw, 1 + i + (1 if i >= 4 else 0))


def reverse_positions(pw: StrSeq, words: StrSeq) -> list[str]:
    x, y = int(words[2]), int(words[-1])
    return [*pw[:x], *reversed(pw[x : y + 1]), *pw[y + 1 :]]


def move_position(pw: StrSeq, words: StrSeq) -> list[str]:
    pw = list(pw)
    val = pw.pop(int(words[2]))
    pw.insert(int(words[-1]), val)
    return pw


OPS: Mapping[str, Callable[[StrSeq, StrSeq], list[str]]] = {
    "swap position": swap_position,
    "swap letter": swap_letter,
    "rotate left": rotate_left,
    "rotate right": rotate_right,
    "rotate based": rotate_based,
    "reverse positions": reverse_positions,
    "move position": move_position,
}


def part_1(txt: str, *, initial: str = INITIAL, backwards: bool = False) -> str:
    pw = [*initial]
    lines = txt.splitlines()
    ops = reversed(lines) if backwards else lines
    for instruction in ops:
        words = instruction.split()
        op = OPS[" ".join(words[:2])]
        if not backwards:
            pw = op(pw, words)
        else:
            pw = list(next(p for p in itertools.permutations(pw) if pw == op(list(p), words)))
    return "".join(pw)


def part_2(txt: str, *, initial: str = SCRAMBLED) -> str:
    return part_1(txt, initial=initial, backwards=True)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
