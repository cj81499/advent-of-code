from more_itertools import ilen

MAX_32_BIT_INTEGER = 0xFFFF_FFFF


def parta(txt: str):
    return next(valid_ips(txt))


def partb(txt: str, max_ip=MAX_32_BIT_INTEGER):
    return ilen(valid_ips(txt, max_ip))


def valid_ips(txt: str, max_ip=MAX_32_BIT_INTEGER):
    sorted_blacklist = tuple(sorted(tuple(int(n) for n in line.split("-")) for line in txt.splitlines()))
    ip = 0
    for start, stop in sorted_blacklist:
        yield from range(ip, start)
        ip = max(ip, stop + 1)
    yield from range(ip, max_ip)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
