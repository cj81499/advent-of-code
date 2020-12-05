from itertools import count


def binary_search(lo, hi, lo_ele, hi_ele, iterable):
    for c in iterable:
        mid = (hi + lo) // 2
        if c == lo_ele:
            hi = mid
        elif c == hi_ele:
            lo = mid + 1
        else:
            raise Exception("invalid element in iterable")
    if lo != hi:
        raise Exception("search did not converge")
    return lo


def seat_id(seat_str):
    row = binary_search(0, 127, "F", "B", seat_str[:7])
    col = binary_search(0, 7, "L", "R", seat_str[7:])
    return row * 8 + col


def seat_ids(txt):
    return (seat_id(seat) for seat in txt.splitlines())


def parta(txt):
    return max(seat_ids(txt))


def partb(txt):
    ids = set(seat_ids(txt))
    for i in count(min(ids)):  # start counting at the first id
        if i not in ids:
            return i


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
