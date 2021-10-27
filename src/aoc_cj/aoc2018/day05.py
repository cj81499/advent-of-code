alphabet = "abcdefghijklmnopqrstuvwxyz"


def parta(txt: str):
    prev_len = 0
    while prev_len != len(txt):
        prev_len = len(txt)
        for c in alphabet:
            txt = txt.replace(c + c.upper(), "").replace(c.upper() + c, "")
    return len(txt)


def partb(txt):
    d = {}
    for c in alphabet:
        d[c] = parta(txt.replace(c, "").replace(c.upper(), ""))
    shortest_length = d["a"]
    for c in alphabet:
        if d[c] < shortest_length:
            shortest_length = d[c]
    return shortest_length


def partb_polished(txt):
    shortest_length = parta(txt)
    for c in alphabet:
        length = parta(txt.replace(c, "").replace(c.upper(), ""))
        if length < shortest_length:
            shortest_length = length
    return shortest_length


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
