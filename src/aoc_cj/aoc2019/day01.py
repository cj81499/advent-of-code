def fuel_req(mass: int) -> int:
    return mass // 3 - 2


def fuel_req_rec(mass: int) -> int:
    r = fuel_req(mass)
    return 0 if 0 >= r else r + fuel_req_rec(r)


def part_1(txt: str) -> int:
    return sum(fuel_req(x) for x in [int(x) for x in txt.splitlines()])


def part_2(txt: str) -> int:
    return sum(fuel_req_rec(x) for x in [int(x) for x in txt.splitlines()])


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
