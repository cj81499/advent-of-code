from aoc_cj.aoc2016.day12 import AssemBunnyComputer


class Day23AssemBunnyComputer(AssemBunnyComputer):
    def tgl(self, x: str) -> None:
        addr = self.pc + self.arg(x)
        if addr < len(self._program):
            ins = self._program[addr]
            if len(ins) == 2:  # one arg instruction
                ins[0] = "dec" if ins[0] == "inc" else "inc"
            elif len(ins) == 3:  # two arg instruction
                ins[0] = "cpy" if ins[0] == "jnz" else "jnz"


def part_1(txt: str) -> int:
    c = Day23AssemBunnyComputer(txt)
    c["a"] = 7
    c.run()
    return c["a"]


def part_2(txt: str) -> int:
    """
    BEWARE: this is super slow (even with pypy).
    I don't really want to finish analyzing the asm, but I started in `day23.md`
    """
    c = Day23AssemBunnyComputer(txt)
    c["a"] = 12
    c.run()
    return c["a"]


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
