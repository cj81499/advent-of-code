def parta(txt: str) -> None:
    nums = list(map(int, txt.split(",")))
    return min(sum(abs(i - n) for n in nums) for i in range(min(nums), max(nums) + 1))


def sum_of_naturals(n: int):
    return n * (n + 1) // 2


def partb(txt: str) -> None:
    nums = list(map(int, txt.split(",")))
    return min(sum(sum_of_naturals(abs(i - n)) for n in nums) for i in range(min(nums), max(nums) + 1))


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
