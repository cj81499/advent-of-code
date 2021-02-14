

def parta(txt):
    return solver(txt, lambda m, a: (a,), lambda m, v: int(apply_mask(m, bin36(v)), 2))


def partb(txt):
    return solver(txt, lambda m, a: (addresses(apply_mask(m, bin36(a), v2=True))), lambda m, v: v)


def solver(txt, addrs_fn, val_fn):
    mem = {}
    mask = 0
    for instruction in txt.splitlines():
        lhs, rhs = instruction.split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            addr = int(lhs[4:-1])
            val = val_fn(mask, int(rhs))
            for a in addrs_fn(mask, addr):
                mem[a] = val
    return sum(mem.values())


def apply_mask(mask, binary, v2=False):
    masked = []
    append_switch = "0" if v2 else "X"
    for m, b in zip(mask, binary):
        masked.append(b if m == append_switch else m)
    return "".join(masked)


def bin36(n):
    return str(bin(n))[2:].zfill(36)


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


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
