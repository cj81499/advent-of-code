from aoc_cj.aoc2018.day16 import run_cmd


def parta(txt):
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])

    registers = [0, 0, 0, 0, 0, 0]
    while registers[ip] >= 0 and registers[ip] < len(lines):
        cmd, a, b, c = [x if len(str(x)) == 4 else int(x) for x in lines[registers[ip]].split()]
        run_cmd(cmd, registers, a, b, c)
        if registers[ip] == 28:
            return max(registers)
        registers[ip] += 1


def partb(txt):
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])

    cmds = [[x if len(str(x)) == 4 else int(x) for x in line.split()] for line in lines]

    seen = set()
    last = None
    registers = [0, 0, 0, 0, 0, 0]
    while registers[ip] >= 0 and registers[ip] < len(lines):
        cmd, a, b, c = cmds[registers[ip]]
        run_cmd(cmd, registers, a, b, c)
        if registers[ip] == 28:
            m = max(registers)
            if m in seen:
                return last
            seen.add(m)
            last = m
        registers[ip] += 1


def main(txt):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")  # SLOWWWWWW. (a few minutes, with pypy)


if __name__ == "__main__":
    from aocd import data

    main(data)
