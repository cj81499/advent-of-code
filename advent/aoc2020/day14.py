import collections  # noqa
import itertools  # noqa
import re  # noqa


def apply_mask(mask, binary, v2=False):
    masked = []
    for m, b in zip(mask, binary):
        if not v2:
            masked.append(b if m == "X" else m)
        else:
            if m == "0":
                masked.append(b)
            elif m == "1":
                masked.append("1")
            else:
                masked.append("X")
    return "".join(masked)


def parta(txt):
    mem = {}
    mask = 0
    for instruction in txt.splitlines():
        lhs, rhs = instruction.split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            addr = int(lhs[4:-1])
            val = int(rhs)
            binary = str(bin(val))[2:].zfill(36)
            result = apply_mask(mask, binary)
            mem[addr] = result
    return sum(int(x, 2) for x in mem.values())


def addresses(addr):
    if "X" not in addr:
        return [addr]
    i = addr.index("X")
    prefix = addr[:i]
    remaining = addr[i+1:]

    subs_addrs = addresses(remaining)
    addrs = []
    for sub in subs_addrs:
        addrs.append(prefix + "0" + sub)
        addrs.append(prefix + "1" + sub)
    return addrs


def partb(txt):
    mem = {}
    mask = 0
    for instruction in txt.splitlines():
        lhs, rhs = instruction.split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            addr = int(lhs[4:-1])
            val = int(rhs)
            new_addr = apply_mask(mask, str(bin(addr))[2:].zfill(36), v2=True)
            addrs = addresses(new_addr)
            for a in addrs:
                mem[a] = val
    return sum(mem.values())


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
