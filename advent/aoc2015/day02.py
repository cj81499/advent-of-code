from datetime import date


def parta(boxes: list):
    total_paper = 0
    for b in boxes:
        l, w, h = (int(x) for x in b.split("x"))
        a_sides = [l*w, w*h, h*l]
        sa = sum(2*x for x in a_sides)
        total_paper += sa + min(a_sides)
    return total_paper


def partb(boxes: list):
    total_ribbon = 0
    for b in boxes:
        l, w, h = (int(x) for x in b.split("x"))
        smallest_two = []
        for x in (l, w, h):
            if len(smallest_two) < 2:
                smallest_two.append(x)
            else:
                smallest_two.append(x)
                smallest_two.remove(max(smallest_two))
        total_ribbon += sum(2 * x for x in smallest_two) + l * w * h
    return total_ribbon


def main():
    _, input_lines = helpers.get_puzzle(date(2015, 12, 2), "I Was Told There Would Be No Math")  # noqa

    print(f"parta: {parta(input_lines)}")
    print(f"partb: {partb(input_lines)}")


if __name__ == "__main__":
    main()
