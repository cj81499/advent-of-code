import more_itertools as mi

MAX_32_BIT_INTEGER = 0xFFFF_FFFF


def part_1(txt: str):
    return next(valid_ips(txt))


def part_2(txt: str, max_ip=MAX_32_BIT_INTEGER):
    return mi.ilen(valid_ips(txt, max_ip))


def valid_ips(txt: str, max_ip=MAX_32_BIT_INTEGER):
    sorted_blacklist = tuple(sorted(tuple(int(n) for n in line.split("-")) for line in txt.splitlines()))
    ip = 0
    for start, stop in sorted_blacklist:
        yield from range(ip, start)
        ip = max(ip, stop + 1)
    yield from range(ip, max_ip)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
