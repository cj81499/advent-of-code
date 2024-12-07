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


def part_1(txt):
    return max(seat_ids(txt))


def part_2(txt):
    ids = set(seat_ids(txt))
    for i in count(min(ids)):  # start counting at the first id
        if i not in ids:
            return i


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
