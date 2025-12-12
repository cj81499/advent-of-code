import re

_PARSE_REGION_PATTER = re.compile(r"(\d+)x(\d+): (\d+(?: \d+)*)")


def part_1(txt: str) -> int:
    *shapes, regions = txt.split("\n\n")
    shape_areas = [s.count("#") for s in shapes]

    can_fit = 0
    for region in _PARSE_REGION_PATTER.finditer(regions):
        length, width, shape_counts = region.groups()

        shape_counts = list(map(int, shape_counts.split()))

        area = int(length) * int(width)
        required_area = sum(c * a for c, a in zip(shape_counts, shape_areas, strict=True))

        difference = area - required_area
        if difference < 0:
            pass
        elif difference > 100:
            can_fit += 1
        else:
            msg = f"Nontrivial puzzle detected!"
            raise AssertionError(msg)

    return can_fit


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
