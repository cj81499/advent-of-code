from advent.aoc2019.intcode_interpreter import run_intcode_program


def parta(txt: str):
    nums = tuple(int(x) for x in txt.split(","))
    run_intcode_program(nums, [1])


# def partb(nums: Tuple[int]):
#     run_intcode_program(nums, [5])


def main(txt) -> None:

    print("parta:")
    parta(txt)

    # print("partb:")
    # partb(nums)


if __name__ == "__main__":
    from aocd import data
    main(data)
