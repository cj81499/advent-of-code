SAFE = "."
TRAP = "^"


def next_row(row: str) -> str:
    return "".join(TRAP if is_trap(pos, row) else SAFE for pos in range(len(row)))


TRAP_PATTERNS = {"^^.", ".^^", "^..", "..^"}


def is_trap(pos: int, prev_row: str) -> bool:
    left = prev_row[pos - 1] if pos - 1 >= 0 else SAFE
    center = prev_row[pos]
    right = prev_row[pos + 1] if pos + 1 < len(prev_row) else SAFE
    pattern = f"{left}{center}{right}"
    return pattern in TRAP_PATTERNS


def part_1(txt: str, num_rows: int = 40) -> int:
    safe_tiles = 0
    row = txt
    for _ in range(num_rows):
        safe_tiles += row.count(SAFE)
        row = next_row(row)
    return safe_tiles


def part_2(txt: str) -> int:
    return part_1(txt, num_rows=400000)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
