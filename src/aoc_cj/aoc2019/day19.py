import itertools

from aoc_cj.aoc2019.intcode_computer import IntcodeProgram


def get_is_affected(txt: str):
    program = [*map(int, txt.split(","))]

    def is_affected(x, y):
        p = IntcodeProgram(program)
        p.write_input(x)
        p.write_input(y)
        p.run()
        return bool(p.outputs[-1])

    return is_affected


def parta(txt: str, range_size=50):
    is_affected = get_is_affected(txt)
    return sum(is_affected(x, y) for x, y in itertools.product(range(range_size), repeat=2))


def partb(txt: str):
    is_affected = get_is_affected(txt)

    def first_x_at_y(y):
        # 2/3 might be too "aggressive" an optimization for some inputs, but it worked for mine
        return next(x for x in itertools.count(2 * y // 3) if is_affected(x, y))

    lo, hi = 100, 5000
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if not is_affected(first_x_at_y(mid) + (100 - 1), mid - (100 - 1)):
            lo = mid
        else:
            hi = mid

    return first_x_at_y(hi) * 10000 + hi - (100 - 1)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
