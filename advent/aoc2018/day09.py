from collections import deque


def run(player_count: int, last_marble_value: int) -> int:
    circle = deque([0])
    scores = [0 for _ in range(player_count)]
    for marble_num in range(1, last_marble_value + 1):
        if marble_num % 23 == 0:
            circle.rotate(7)
            scores[(marble_num % player_count) -
                   1] += marble_num + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble_num)
    return max(scores)


def parta(txt):
    split = txt.split()
    player_count = int(split[0])
    last_marble_value = int(split[6])
    return run(player_count, last_marble_value)


def partb(txt):
    split = txt.split()
    player_count = int(split[0])
    last_marble_value = int(split[6])
    return run(player_count, 100 * last_marble_value)


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
