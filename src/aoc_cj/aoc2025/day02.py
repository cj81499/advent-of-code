import itertools
import re
from collections.abc import Generator


def ranges(txt: str) -> Generator[range]:
    for r in txt.replace("\n", "").split(","):
        start, sep, end = r.partition("-")
        assert sep == "-"
        yield range(int(start), int(end) + 1)


def part_1(txt: str, *, pattern: re.Pattern[str] = re.compile(r"^(.+)\1$")) -> int:
    return sum(
        filter(
            lambda n: pattern.match(str(n)) is not None,
            itertools.chain.from_iterable(ranges(txt)),
        )
    )


def part_2(txt: str) -> int:
    return part_1(txt, pattern=re.compile(r"^(.+)\1+$"))


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
