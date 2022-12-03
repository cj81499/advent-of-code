from aoc_cj.aoc2018.day16 import run_cmd


def parta(txt):
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])

    registers = [0, 0, 0, 0, 0, 0]
    while registers[ip] < len(lines):
        cmd, a, b, c = (x if len(str(x)) == 4 else int(x) for x in lines[registers[ip]].split())
        run_cmd(cmd, registers, a, b, c)
        registers[ip] += 1
    return registers[0]


def factors(n):
    results = set()
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            results.add(i)
            results.add(n // i)
    return results


def partb(txt):
    ip, *lines = txt.splitlines()
    ip = int(ip[4:])

    registers = [1, 0, 0, 0, 0, 0]
    i = 0
    # 100 times is enough to find the number the main loop will find the sum of the factors of
    while registers[ip] < len(lines) and i < 100:
        cmd, a, b, c = (x if len(str(x)) == 4 else int(x) for x in lines[registers[ip]].split())
        run_cmd(cmd, registers, a, b, c)
        registers[ip] += 1
        i += 1
    return sum(factors(max(registers)))


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
