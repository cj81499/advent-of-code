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


def part_1(txt):
    return play_game(txt, 2020)


def part_2(txt):
    return play_game(txt, 30000000)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
