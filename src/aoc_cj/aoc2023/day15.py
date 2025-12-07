import dataclasses
import re

import more_itertools as mi

STEP_PATTERN = re.compile("^([a-z]+)(-|=)([1-9])?$")


def hash_algorithm(s: str) -> int:
    """HASH (Holiday ASCII String Helper) algorithm"""
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def part_1(txt: str) -> int:
    return sum(hash_algorithm(step) for step in txt.split(","))


@dataclasses.dataclass(frozen=True)
class Lens:
    focal_length: int
    label: str


def focusing_power(box_number: int, slot_number: int, focal_length: int) -> int:
    return (1 + box_number) * slot_number * focal_length


def hashmap_algorithm(s: str) -> list[list[Lens]]:
    """HASHMAP (Holiday ASCII String Helper Manual Arrangement Procedure) algorithm"""
    boxes: list[list[Lens]] = [[] for _ in range(256)]

    for step in s.split(","):
        match = STEP_PATTERN.match(step)
        assert match
        label, op, focal_length = match.group(1, 2, 3)
        assert isinstance(label, str)
        assert isinstance(op, str)
        box = boxes[hash_algorithm(label)]
        lens_idx = mi.first((i for i, l in enumerate(box) if l.label == label), None)
        if op == "-":
            if lens_idx is not None:
                box.pop(lens_idx)
        elif op == "=":
            assert isinstance(focal_length, str)
            lens = Lens(int(focal_length), label)
            if lens_idx is not None:
                box[lens_idx] = lens
            else:
                box.append(lens)
        else:
            msg = "unreachable"
            raise AssertionError(msg)

    return boxes


def part_2(txt: str) -> int:
    lens_configuration = hashmap_algorithm(txt)

    return sum(
        focusing_power(box_number, slot_number, lens.focal_length)
        for box_number, box in enumerate(lens_configuration)
        for slot_number, lens in enumerate(box, start=1)
    )


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
