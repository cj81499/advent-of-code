import dataclasses
import itertools

import more_itertools as mi


def part_1(txt: str) -> int:
    disk: list[int | None] = []
    is_file = True
    file_id = 0
    for length in map(int, txt):
        to_append = file_id if is_file else None
        for _ in range(length):
            disk.append(to_append)
        is_file = not is_file
        if is_file:
            file_id += 1

    i = 0
    end = len(disk) - 1
    for i in range(len(disk)):
        if i < end and disk[i] is None:
            while disk[end] is None:
                end -= 1
            if i >= end:
                break
            disk[i] = disk[end]
            disk[end] = None

    return fs_checksum(disk)


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class File:
    id: int
    start: int
    length: int


def part_2(txt: str) -> int:
    disk: list[File] = []
    is_file = True
    file_id = 0
    start = 0
    for length in map(int, txt):
        if is_file:
            disk.append(File(id=file_id, start=start, length=length))

        start += length
        is_file = not is_file
        if is_file:
            file_id += 1

    # for f in disk:
    #     print(f)
    # print()

    max_file_id = disk[-1].id
    for file_id in reversed(range(max_file_id + 1)):
        # find file on disk
        file = mi.one(f for f in disk if f.id == file_id)
        # print(f"attempt to move {file=}")
        # attempt to move file
        # find span of free space that can fit file
        space_needed = file.length
        # print(f"{space_needed=}")
        for i, (f1, f2) in enumerate(itertools.pairwise(disk)):
            if f1 is file:
                break
            space_starts = f1.start + f1.length
            space_ends = f2.start
            available_space = space_ends - space_starts
            # print(f"{available_space=} between {f1} {f2}")
            if available_space >= space_needed:
                # print(f"MOVE {file=} immediately after {f1=}")
                disk.remove(file)
                disk.insert(i + 1, File(id=file.id, start=space_starts, length=file.length))
                break

    # for f in disk:
    #     print(f)

    disk2: list[int | None] = []
    for f in disk:
        while len(disk2) < f.start:
            disk2.append(None)
        for _ in range(f.length):
            disk2.append(f.id)

    # print("".join(str(d) if d is not None else "." for d in disk2))

    fs_checksum = sum(i * n for i, n in enumerate(disk2) if n is not None)
    return fs_checksum


def fs_checksum(disk: list[int | None]) -> int:
    return sum(i * n for i, n in enumerate(disk) if n is not None)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
