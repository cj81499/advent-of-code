from __future__ import annotations

MAX_32_BIT_INTEGER = 0xffff_ffff


def parta(txt: str):
    return next(valid_ips(txt))


def partb(txt: str, max_ip=MAX_32_BIT_INTEGER):
    return sum(1 for _ in valid_ips(txt, max_ip))


def valid_ips(txt: str,  max_ip=MAX_32_BIT_INTEGER):
    sorted_blacklist = tuple(sorted(
        tuple(int(n) for n in line.split("-"))
        for line in txt.splitlines()
    ))
    ip = 0
    for start, stop in sorted_blacklist:
        for valid_ip in range(ip, start):
            yield valid_ip
        ip = max(ip, stop + 1)
    for valid_id in range(ip, max_ip):
        yield valid_id


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
