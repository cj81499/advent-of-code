from __future__ import annotations

from advent.aoc2016.day12 import AssemBunnyComputer


class Day23AssemBunnyComputer(AssemBunnyComputer):
    def tgl(self, x):
        # print(self._registers)
        idx = self.pc + self.arg(x)
        try:
            ins = self._program[idx]
            # old_ins = [x for x in ins]
            if len(ins) == 2:  # one arg instruction
                ins[0] = "dec" if ins[0] == "inc" else "inc"
            elif len(ins) == 3:  # two arg instruction
                ins[0] = "cpy" if ins[0] == "jnz" else "jnz"
            # print(f"tgl at {idx}. {old_ins} -> {ins}")
        except IndexError:
            # print(f"tgl at {idx} failed")
            pass


def parta(txt: str):
    c = Day23AssemBunnyComputer(txt)
    c["a"] = 7
    c.run()
    return c["a"]


def partb(txt: str):
    """
    BEWARE: this is super slow (even with pypy).
    I don't really want to finish analyzing the asm, but I started in `day23.md`
    """
    c = Day23AssemBunnyComputer(txt)
    c["a"] = 12
    c.run()
    return c["a"]


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
