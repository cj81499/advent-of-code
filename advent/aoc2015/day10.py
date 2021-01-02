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


def parta(txt: str):
    return len(look_and_say(txt, 40))


def partb(txt: str):
    return len(look_and_say(txt, 50))


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
