import json

J = int | str | dict[str, "J"] | list["J"]


def sum_of_all_numbers(input_json: J, *, ignore_red: bool = False) -> int:
    if isinstance(input_json, int):
        return input_json
    if isinstance(input_json, dict):
        if ignore_red and "red" in input_json.values():
            return 0
        return sum(sum_of_all_numbers(x, ignore_red=ignore_red) for x in input_json.values())
    if isinstance(input_json, list):
        return sum(sum_of_all_numbers(x, ignore_red=ignore_red) for x in input_json)
    return 0


def part_1(txt: str) -> int:
    return sum_of_all_numbers(json.loads(txt))


def part_2(txt: str) -> int:
    return sum_of_all_numbers(json.loads(txt), ignore_red=True)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
