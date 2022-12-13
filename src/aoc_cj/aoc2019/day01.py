def fuel_req(mass: int) -> int:
    return mass // 3 - 2


def fuel_req_rec(mass: int) -> int:
    r = fuel_req(mass)
    return 0 if 0 >= r else r + fuel_req_rec(r)


def parta(txt: str) -> int:
    return sum(fuel_req(x) for x in [int(x) for x in txt.splitlines()])


def partb(txt: str) -> int:
    return sum(fuel_req_rec(x) for x in [int(x) for x in txt.splitlines()])


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
