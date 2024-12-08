from collections.abc import Generator, Sequence


def parse(txt: str) -> Generator[tuple[int, tuple[int, ...]], None, None]:
    for line in txt.splitlines():
        target, sep, nums = line.partition(": ")
        assert sep == ": "
        yield int(target), tuple(map(int, nums.split()))


def _possible_results(nums: Sequence[int], *, concat_op: bool = False) -> Generator[int, None, None]:
    if len(nums) == 1:
        yield nums[0]
        return
    *rest, last = nums
    for r in _possible_results(rest, concat_op=concat_op):
        yield r + last
        yield r * last
        if concat_op:
            yield int(str(r) + str(last))


def solve(txt: str, *, concat_op: bool = False) -> int:
    return sum(target for target, nums in parse(txt) if target in _possible_results(nums, concat_op=concat_op))


def part_1(txt: str) -> int:
    return solve(txt)


def part_2(txt: str) -> int:
    return solve(txt, concat_op=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
