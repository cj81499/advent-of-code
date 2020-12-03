def parta(txt):
    return -1


def partb(txt):
    return -1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data, submit
    main(data)
