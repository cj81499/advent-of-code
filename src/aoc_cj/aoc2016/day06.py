from collections import Counter


def part_1(txt: str):
    return error_correct_message(txt)


def part_2(txt: str):
    return error_correct_message(txt, modified=True)


def error_correct_message(txt, modified=False):
    message = []
    for chars in zip(*txt.splitlines()):
        counts = Counter(chars)
        most_common, *_, least_common = counts.most_common()
        message.append((least_common if modified else most_common)[0])
    return "".join(message)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
