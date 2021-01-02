def parta(txt):
    total_paper = 0
    for box in txt.splitlines():
        l, w, h = (int(x) for x in box.split("x"))
        a_sides = [l*w, w*h, h*l]
        sa = sum(2*x for x in a_sides)
        total_paper += sa + min(a_sides)
    return total_paper


def partb(txt):
    total_ribbon = 0
    for box in txt.splitlines():
        l, w, h = (int(x) for x in box.split("x"))
        smallest_two = []
        for x in (l, w, h):
            if len(smallest_two) < 2:
                smallest_two.append(x)
            else:
                smallest_two.append(x)
                smallest_two.remove(max(smallest_two))
        total_ribbon += sum(2 * x for x in smallest_two) + l * w * h
    return total_ribbon


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
