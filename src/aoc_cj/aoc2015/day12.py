import json


def sum_of_all_numbers(input_json, ignore_red=False):
    if isinstance(input_json, int):
        return input_json
    elif isinstance(input_json, dict):
        if ignore_red and "red" in input_json.values():
            return 0
        return sum(sum_of_all_numbers(x, ignore_red=ignore_red) for x in input_json.values())
    elif isinstance(input_json, list):
        return sum(sum_of_all_numbers(x, ignore_red=ignore_red) for x in input_json)
    return 0


def part_1(txt):
    j = json.loads(txt)
    return sum_of_all_numbers(j)


def part_2(txt):
    j = json.loads(txt)
    return sum_of_all_numbers(j, ignore_red=True)


if __name__ == "__main__":
    from aocd import data

    print(f"part_1: {part_1(data)}")
    print(f"part_2: {part_2(data)}")
