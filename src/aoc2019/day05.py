from typing import Tuple

from aocd import data

from intcode_interpreter import run_intcode_program


def parta(txt: str):
    nums = tuple(int(x) for x in txt.split(","))
    run_intcode_program(nums, [1])


# def partb(nums: Tuple[int]):
#     run_intcode_program(nums, [5])


def main() -> None:

    print("parta:")
    parta(data)

    # print("partb:")
    # partb(nums)


if __name__ == "__main__":
    main()
