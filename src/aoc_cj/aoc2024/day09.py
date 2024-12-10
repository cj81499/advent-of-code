import dataclasses
import itertools

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


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class File:
    id: int
    start: int
    length: int


def part_2(txt: str) -> int:
    disk: list[File] = []
    start = 0
    for i, length in enumerate(map(int, txt)):
        is_file = i % 2 == 0
        if is_file:
            file_id = i // 2
            disk.append(File(id=file_id, start=start, length=length))

        start += length

    # defrag the disk
    max_file_id = disk[-1].id
    for file_id in reversed(range(max_file_id + 1)):
        # find file on disk
        file = mi.one(f for f in disk if f.id == file_id)
        # attempt to move file
        # find span of free space that can fit file
        space_needed = file.length
        for i, (f1, f2) in enumerate(itertools.pairwise(disk)):
            if f1 is file:
                break
            space_starts = f1.start + f1.length
            space_ends = f2.start
            available_space = space_ends - space_starts
            if available_space >= space_needed:
                disk.remove(file)
                disk.insert(i + 1, File(id=file.id, start=space_starts, length=file.length))
                break

    # return the filesystem checksum
    return sum(sum(f.id * i for i in range(f.start, f.start + f.length)) for f in disk)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
