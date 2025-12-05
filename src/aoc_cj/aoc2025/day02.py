import functools
import itertools
import re

from aoc_cj import util


def solve(txt: str, *, invalid_id_pattern: re.Pattern[str]) -> int:
    return sum(
        filter(
            lambda n: invalid_id_pattern.match(str(n)) is not None,
            itertools.chain.from_iterable(
                map(
                    util.parse_range,
                    txt.replace("\n", "").split(","),
                )
            ),
        )
    )


part_1 = functools.partial(solve, invalid_id_pattern=re.compile(r"^(\d+)\1$"))
part_2 = functools.partial(solve, invalid_id_pattern=re.compile(r"^(\d+)\1+$"))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
