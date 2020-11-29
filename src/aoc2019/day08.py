from collections import Counter
from typing import List

from aocd import data

WIDTH = 25
HEIGHT = 6

BLACK = 0
WHITE = 1
TRANSPARENT = 2


def get_layers(nums: List[int], width: int, height: int) -> List[List[int]]:
    layer_size = width * height
    return [nums[i:i + layer_size] for i in range(0, len(nums), layer_size)]


def parta(txt: str) -> int:
    nums = [int(c) for c in txt]

    layers = get_layers(nums, WIDTH, HEIGHT)
    counts = [Counter(l) for l in layers]
    least_zeros = min(counts, key=lambda c: c[0])
    return least_zeros[1] * least_zeros[2]


def render(layers: List[List[int]], row_len: int) -> str:
    def render_pos(layers: List[List[int]], pos: int) -> int:
        for lay in layers:
            val = lay[pos]
            if val != TRANSPARENT:
                return val
        return -1

    def row_to_str(row: List[int]) -> str:
        return "".join(" " if x == BLACK else "X" for x in row)

    pixels = [render_pos(layers, i) for i in range(len(layers[0]))]

    rows = []
    for i in range(0, len(pixels), row_len):
        rows.append(pixels[i:i + row_len])

    return "\n".join(row_to_str(r) for r in rows)


def partb(txt: str) -> str:
    nums = [int(c) for c in txt]

    layers = get_layers(nums, WIDTH, HEIGHT)
    rendered = render(layers, WIDTH)
    return f"\n{rendered}"


def main() -> None:

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")


if __name__ == "__main__":
    main()
