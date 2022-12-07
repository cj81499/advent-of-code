import re
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Union

TOTAL_DISK_SPACE = 70000000
REQUIRED_AVAILABLE_SPACE = 30000000


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    children: list[Union["Dir", File]]

    @property
    def size(self) -> int:
        return sum(c.size for c in self.children)


def parta(txt: str) -> int:
    dirs = parse(txt)

    return sum(d.size for d in dirs.values() if d.size <= 100000)


def parse(txt: str) -> dict[str, Dir]:
    dirs: DefaultDict[str, Dir] = defaultdict(lambda: Dir([]))
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
    return dirs


def partb(txt: str) -> int:
    dirs = parse(txt)

    dir_sizes = {d.size for d in dirs.values()}
    total_used_space = max(dir_sizes)
    current_unused_space = TOTAL_DISK_SPACE - total_used_space
    must_delete_at_least = REQUIRED_AVAILABLE_SPACE - current_unused_space

    delete_candidates = {s for s in dir_sizes if s > must_delete_at_least}

    return min(delete_candidates)


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
