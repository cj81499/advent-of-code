from __future__ import annotations

SAFE = "."
TRAP = "^"


def next_row(row):
    return "".join(TRAP if is_trap(pos, row) else SAFE for pos in range(len(row)))


TRAP_PATTERNS = {"^^.", ".^^", "^..", "..^"}


def is_trap(pos, prev_row):
    left = prev_row[pos - 1] if pos - 1 >= 0 else SAFE
    center = prev_row[pos]
    right = prev_row[pos + 1] if pos + 1 < len(prev_row) else SAFE
    pattern = f"{left}{center}{right}"
    return pattern in TRAP_PATTERNS


def parta(txt: str, num_rows=40):
    safe_tiles = 0
    row = txt
    for _ in range(num_rows):
        safe_tiles += row.count(SAFE)
        row = next_row(row)
    return safe_tiles


def partb(txt: str):
    return parta(txt, num_rows=400000)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
