import json
from datetime import date

import helpers


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


def main():
    input_txt, _ = helpers.get_puzzle(date(2015, 12, 12), "JSAbacusFramework.io")  # noqa

    input_json = json.loads(input_txt)

    print(f"part1: {sum_of_all_numbers(input_json)}")
    print(f"part2: {sum_of_all_numbers(input_json, ignore_red=True)}")


if __name__ == "__main__":
    main()
