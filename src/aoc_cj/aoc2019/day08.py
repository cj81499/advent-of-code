from collections import Counter

WIDTH = 25
HEIGHT = 6

BLACK = 0
WHITE = 1
TRANSPARENT = 2


def get_layers(nums: list[int], width: int, height: int) -> list[list[int]]:
    layer_size = width * height
    return [nums[i : i + layer_size] for i in range(0, len(nums), layer_size)]


def part_1(txt: str) -> int:
    nums = [int(c) for c in txt]

    layers = get_layers(nums, WIDTH, HEIGHT)
    counts = [Counter(line) for line in layers]
    least_zeros = min(counts, key=lambda c: c[0])
    return least_zeros[1] * least_zeros[2]


def render(layers: list[list[int]], row_len: int) -> str:
    def render_pos(layers: list[list[int]], pos: int) -> int:
        for lay in layers:
            val = lay[pos]
            if val != TRANSPARENT:
                return val
        return -1

    def row_to_str(row: list[int]) -> str:
        return "".join(" " if x == BLACK else "#" for x in row)

    pixels = [render_pos(layers, i) for i in range(len(layers[0]))]

    rows = []
    for i in range(0, len(pixels), row_len):
        rows.append(pixels[i : i + row_len])

    return "\n".join(row_to_str(r) for r in rows)


def part_2(txt: str) -> str:
    nums = [int(c) for c in txt]

    layers = get_layers(nums, WIDTH, HEIGHT)
    rendered = render(layers, WIDTH)
    return f"\n{rendered}"


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
