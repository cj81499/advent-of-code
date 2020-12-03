from day16 import run_cmd


def run(lines: list, ip):
    seen = set()
    last = None
    registers = [0, 0, 0, 0, 0, 0]
    parta_solved = False
    while registers[ip] >= 0 and registers[ip] < len(lines):
        cmd, a, b, c = [x if len(str(x)) == 4 else int(x)
                        for x in lines[registers[ip]].split()]
        run_cmd(cmd, registers, a, b, c)
        if registers[ip] == 28:
            m = max(registers)
            if m not in seen:
                if not parta_solved:
                    print(f"parta: {m}")
                    parta_solved = True
                seen.add(m)
                last = m
                print(len(seen))
            else:
                print(f"partb: {last}")
                # return seen[-1]
                return
        registers[ip] += 1
    print(registers)


def main():
    _, input_lines = helpers.load_input(21, "Chronal Conversion")

    ip = int(input_lines.pop(0)[4:])

    # WARNING: PART 2 IS SUPER SUPER SLOW
    run(input_lines, ip)


if __name__ == "__main__":
    import helpers
    main()
