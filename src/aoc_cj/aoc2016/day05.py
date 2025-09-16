import hashlib
import itertools
from collections.abc import Generator
from typing import Literal, cast, overload

NUMBER_OF_ZEROS = 5


@overload
def password_generator(door_id: str, *, index_mode: Literal[False] = False) -> Generator[str]: ...
@overload
def password_generator(door_id: str, *, index_mode: Literal[True]) -> Generator[tuple[int, str]]: ...
def password_generator(door_id: str, *, index_mode: bool = False) -> Generator[str | tuple[int, str]]:
    for i in itertools.count():
        hd = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()
        if hd.startswith("0" * NUMBER_OF_ZEROS):
            x = hd[NUMBER_OF_ZEROS]
            if not index_mode:  # part a
                yield x
            elif x.isnumeric() and (i := int(x)) in range(8):  # part b
                yield i, hd[NUMBER_OF_ZEROS + 1]


def part_1(txt: str) -> str:
    pass_gen = password_generator(txt)
    return "".join(next(pass_gen) for _ in range(8))


def part_2(txt: str) -> str:
    pass_gen = password_generator(txt, index_mode=True)
    password: list[str | None] = [None] * 8
    while None in password:
        i, x = next(pass_gen)
        if password[i] is None:
            password[i] = x
    return "".join(cast(list[str], password))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
