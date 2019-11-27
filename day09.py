from collections import deque


def run(player_count, last_marble_value):
    circle = [0]
    marble_num = 1
    current_marble_index = 0
    scores = [0 for _ in range(player_count)]
    while marble_num < last_marble_value:
        for elf in range(player_count):
            if marble_num > last_marble_value:
                break
            if marble_num % 23 != 0:
                current_marble_index = (current_marble_index + 1) % len(circle) + 1
                circle.insert(current_marble_index, marble_num)
            else:
                current_marble_index -= 7
                if current_marble_index < 0:
                    current_marble_index += len(circle)

                removed = circle.pop(current_marble_index)
                scores[elf] += marble_num + removed
            marble_num += 1
    return max(scores)


def run_polished(player_count: int, last_marble_value: int) -> int:
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


def main():
    input_txt, _ = helpers.load_input(9, "Marble Mania")

    split = input_txt.split()
    player_count = int(split[0])
    last_marble_value = int(split[6])

    print(f"part1: {run(player_count, last_marble_value)}")
    print(f"part2: {run_polished(player_count, 100 * last_marble_value)}")


if __name__ == "__main__":
    import helpers
    main()
