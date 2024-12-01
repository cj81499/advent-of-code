from collections import deque

NAUGHTY_SUBSTRINGS = {"ab", "cd", "pq", "xy"}
VOWELS = {x for x in "aeiou"}


def is_nice1(s: str) -> bool:
    if any(x in s for x in NAUGHTY_SUBSTRINGS):
        return False

    vowel_count = 0
    twice_in_a_row = False

    prev = None
    for c in s:
        if c in VOWELS:
            vowel_count += 1
        if c == prev:
            twice_in_a_row = True
        prev = c

    return vowel_count >= 3 and twice_in_a_row


def is_nice2(s: str) -> bool:
    repeating_pair = False
    sandwich = False
    pairs = set()
    prev_pair = None
    history = deque[str]()
    for c in s:
        history.append(c)
        if len(history) == 3:
            if history[0] == history[-1]:
                sandwich = True
            history.popleft()

        if len(history) == 2:
            pair = "".join(history)
            if pair in pairs and pair != prev_pair:
                repeating_pair = True
            pairs.add(pair)
            prev_pair = pair

    return sandwich and repeating_pair


def part_1(txt: str) -> int:
    return sum(is_nice1(s) for s in txt.splitlines())


def part_2(txt: str) -> int:
    return sum(is_nice2(s) for s in txt.splitlines())


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
