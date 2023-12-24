from collections import Counter


def parse(txt: str) -> list[int]:
    return list(map(int, txt.split(",")))


def solve(fish: list[int], days: int = 80) -> int:
    fish_counts = Counter(fish)
    for _day in range(days):
        # all fish w/ timer 0 become fish w/ timer 6 and new fish w/ timer 8
        new_counts = Counter({6: fish_counts[0], 8: fish_counts[0]})
        # decrease the timers of all fish
        new_counts.update({timer - 1: count for timer, count in fish_counts.items() if timer > 0})
        # set the counts to the new counts
        fish_counts = new_counts
    return sum(fish_counts.values())


def part_1(txt: str) -> int:
    return solve(parse(txt))


def part_2(txt: str) -> int:
    return solve(parse(txt), 256)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
