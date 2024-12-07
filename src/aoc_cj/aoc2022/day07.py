import dataclasses
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Self

MAX_DIR_SIZE = 100000

TOTAL_DISK_SPACE = 70000000
REQUIRED_AVAILABLE_SPACE = 30000000


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    children: list[File | Self] = dataclasses.field(default_factory=list)

    @property
    def size(self) -> int:
        return sum(c.size for c in self.children)


def get_dir_sizes(txt: str) -> list[int]:
    dirs = defaultdict[str, Dir](Dir)
    current_path: list[str] = []
    for cmd in txt.split("\n$ "):
        if m := re.match(r"(\$ )?cd (.*)", cmd):
            cd_to = m.group(2)
            if cd_to == "..":
                current_path.pop()
            else:
                current_path.append(cd_to)
        elif cmd.startswith("ls"):
            dir = dirs[" ".join(current_path)]
            for line in cmd.splitlines()[1:]:
                if line.startswith("dir"):
                    _, subdir_name = line.split()
                    current_path.append(subdir_name)
                    subdir = dirs[" ".join(current_path)]
                    current_path.pop()
                    dir.children.append(subdir)
                else:
                    size, filename = line.split()
                    dir.children.append(File(filename, int(size)))
        else:
            assert False, f"unrecognized command: '{cmd}'"
    return [d.size for d in dirs.values()]


def part_1(txt: str) -> int:
    return sum(s for s in get_dir_sizes(txt) if s <= MAX_DIR_SIZE)


def part_2(txt: str) -> int:
    dir_sizes = get_dir_sizes(txt)

    total_used_space = max(dir_sizes)
    current_unused_space = TOTAL_DISK_SPACE - total_used_space
    must_delete_at_least = REQUIRED_AVAILABLE_SPACE - current_unused_space

    return min(s for s in dir_sizes if s > must_delete_at_least)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
