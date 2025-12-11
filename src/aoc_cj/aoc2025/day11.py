import functools
import re


def parse_device(line: str) -> tuple[str, frozenset[str]]:
    device, *outputs = re.findall(r"\w+", line)
    return device, frozenset(outputs)


def part_1(txt: str) -> int:
    attached_outputs = dict(map(parse_device, txt.splitlines()))

    @functools.cache
    def count_paths(current: str) -> int:
        return 1 if current == "out" else sum(map(count_paths, attached_outputs[current]))

    return count_paths("you")


def part_2(txt: str) -> int:
    attached_outputs = dict(map(parse_device, txt.splitlines()))

    @functools.cache
    def count_paths(current: str, *, seen_fft: bool, seen_dac: bool) -> int:
        if current == "out":
            return 1 if seen_fft and seen_dac else 0
        seen_fft = seen_fft or current == "fft"
        seen_dac = seen_dac or current == "dac"
        f = functools.partial(count_paths, seen_fft=seen_fft, seen_dac=seen_dac)
        return sum(map(f, attached_outputs[current]))

    return count_paths("svr", seen_fft=False, seen_dac=False)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
