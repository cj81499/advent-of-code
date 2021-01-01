import collections  # noqa
import itertools  # noqa
import re  # noqa


def play_game(txt, rounds):
    nums = [int(x) for x in txt.split(",")]
    spoken = {}
    last_num = None
    for i in range(rounds):
        to_speak = 0
        if i < len(nums):
            to_speak = nums[i]
        elif last_num in spoken:
            to_speak = (i - 1) - spoken[last_num]
        spoken[last_num] = i - 1
        last_num = to_speak
    return last_num


def parta(txt):
    return play_game(txt, 2020)


def partb(txt):
    return play_game(txt, 30000000)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
