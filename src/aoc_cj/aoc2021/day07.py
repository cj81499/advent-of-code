def parta(txt: str) -> int:
    nums = list(map(int, txt.split(",")))
    return min(sum(abs(i - n) for n in nums) for i in range(min(nums), max(nums) + 1))


def sum_of_naturals(n: int) -> int:
    return n * (n + 1) // 2


def partb(txt: str) -> int:
    nums = list(map(int, txt.split(",")))
    return min(sum(sum_of_naturals(abs(i - n)) for n in nums) for i in range(min(nums), max(nums) + 1))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
