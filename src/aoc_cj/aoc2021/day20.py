import itertools
from collections import defaultdict

import more_itertools as mi

Pixels = defaultdict[tuple[int, int], bool]


def part_1(txt: str, *, loops: int = 2) -> int:
    assert loops % 2 == 0, "odd number of loops will result in image w/ infinitely many lit pixels"

    image_enhancement_algorithm, lit_pixels = parse(txt)

    for _ in range(loops):
        lit_pixels = enhance(image_enhancement_algorithm, lit_pixels)

    return sum(lit_pixels.values())


def part_2(txt: str) -> int:
    return part_1(txt, loops=50)


def parse(txt: str) -> tuple[str, Pixels]:
    image_enhancement_algorithm, input_image_s = txt.split("\n\n")

    # assert image is flashing between lit/dark (like it is in my input)
    assert image_enhancement_algorithm[0] == "#"
    assert image_enhancement_algorithm[-1] == "."

    lit_pixels = defaultdict(
        bool,
        {(x, y): True for y, line in enumerate(input_image_s.splitlines()) for x, c in enumerate(line) if c == "#"},
    )

    return image_enhancement_algorithm, lit_pixels


def enhance(image_enhancement_algorithm: str, lit_pixels: Pixels) -> Pixels:
    df = lit_pixels.default_factory
    assert df is not None
    new_default = not df()
    new_lit_pixels: Pixels = defaultdict(lambda: new_default)

    min_x, max_x = mi.minmax(x for x, y in lit_pixels)
    min_y, max_y = mi.minmax(y for x, y in lit_pixels)

    # the "litness" of any (x, y) outside of this range will be lit in allignment with `new_default`
    for x, y in itertools.product(range(min_x - 1, max_x + 2), range(min_y - 1, max_y + 2)):
        binary = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                binary <<= 1
                binary |= int(lit_pixels[(x + dx, y + dy)])
        is_lit = image_enhancement_algorithm[binary] == "#"
        if is_lit != new_default:
            new_lit_pixels[(x, y)] = is_lit

    return new_lit_pixels


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
