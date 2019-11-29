from datetime import date

import helpers


def look_and_say(txt: str, count: int):
    chars = txt
    for _ in range(count):
        next_chars = []
        count = 0
        prev = None
        for c in chars:
            if c != prev and count > 0:
                next_chars.append(str(count))
                next_chars.append(prev)
                count = 1
            else:
                count += 1
            prev = c
        next_chars.append(str(count))
        next_chars.append(prev)
        chars = next_chars
    return ''.join(chars)


def part1(txt: str):
    return len(look_and_say(txt, 40))


def part2(txt: str):
    return len(look_and_say(txt, 50))


def main():
    input_txt, _ = helpers.get_puzzle(
        date(2015, 12, 10), "Elves Look, Elves Say")

    print(f"part1: {part1(input_txt)}")
    print(f"part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
