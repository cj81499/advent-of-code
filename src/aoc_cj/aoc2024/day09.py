import dataclasses
import heapq
from collections import defaultdict

import more_itertools as mi


def part_1(txt: str) -> int:
    disk: list[int | None] = []
    for i, length in enumerate(map(int, txt)):
        is_file = i % 2 == 0
        file_id = i // 2
        disk.extend([file_id if is_file else None] * length)

    # defrag the disk
    i = mi.first(idx for idx, n in enumerate(disk) if n is None)
    end = len(disk) - 1
    while i < end:
        assert disk[i] is None
        assert disk[end] is not None
        disk[i], disk[end] = disk[end], None
        while disk[end] is None:
            end -= 1
        while disk[i] is not None:
            i += 1

    # return the filesystem checksum
    return sum(i * n for i, n in enumerate(disk) if n is not None)


@dataclasses.dataclass(kw_only=True, slots=True)
class File:
    id: int
    start: int
    length: int


def part_2(txt: str) -> int:
    disk: list[File] = []
    # mapping from size of free space to heap of indices where free space of that size starts
    # using a heap enables us to efficiently track all free spaces of a particular size AND
    # efficiently find the first (minimum) free space of that size
    free_space = defaultdict[int, list[int]](list)
    start = 0
    for i, length in enumerate(map(int, txt)):
        is_file = i % 2 == 0
        if is_file:
            file_id = i // 2
            disk.append(File(id=file_id, start=start, length=length))
        else:
            heapq.heappush(free_space[length], start)
        start += length

    # defrag the disk
    # solution inspired by https://github.com/ricbit/advent-of-code/blob/main/2024/adv09-r.py
    for f in reversed(disk):
        best_size, best_pos = f.length, f.start
        # it's impossible for any file or free space to be larger than 9 b/c the input
        # represents each size w/ a single int
        for size in range(f.length, 10):
            spaces_of_size = free_space[size]
            if len(spaces_of_size) > 0:
                # To access the smallest item without popping it, use heap[0].
                # via https://docs.python.org/3/library/heapq.html#heapq.heappop
                start_of_first_space_of_size = spaces_of_size[0]
                if start_of_first_space_of_size < best_pos:
                    best_pos = start_of_first_space_of_size
                    best_size = size
        # if we found somewhere to move the file
        if best_pos != f.start:
            # move file to the best position
            f.start = best_pos
            # that space is no longer available
            heapq.heappop(free_space[best_size])
            # but a new space (may) be available!
            remaining_space = best_size - f.length
            if remaining_space > 0:
                remaining_space_start = best_pos + f.length
                heapq.heappush(free_space[remaining_space], remaining_space_start)

    # return the filesystem checksum
    return sum(sum(f.id * i for i in range(f.start, f.start + f.length)) for f in disk)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
