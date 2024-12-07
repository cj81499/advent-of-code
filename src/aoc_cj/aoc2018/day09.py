from collections import deque


def run(player_count: int, last_marble_value: int) -> int:
    circle = deque([0])
    scores = [0 for _ in range(player_count)]
    for marble_num in range(1, last_marble_value + 1):
        if marble_num % 23 == 0:
            circle.rotate(7)
            scores[(marble_num % player_count) - 1] += marble_num + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble_num)
    return max(scores)


def part_1(txt):
    split = txt.split()
    player_count = int(split[0])
    last_marble_value = int(split[6])
    return run(player_count, last_marble_value)


def part_2(txt):
    split = txt.split()
    player_count = int(split[0])
    last_marble_value = int(split[6])
    return run(player_count, 100 * last_marble_value)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
