from __future__ import annotations

ONE_BILLION = 1_000_000_000


def parta(txt: str, num_programs=16, repetitions=1):
    programs = [chr(ord("a") + i) for i in range(num_programs)]
    return dance(programs, txt.split(","), repetitions)


def partb(txt: str):
    return parta(txt, repetitions=ONE_BILLION)


def dance(programs, moves, repetitions):
    seen = {}
    for i in range(repetitions):
        p_str = "".join(programs)
        if p_str in seen:
            loop_size = i - seen[p_str]
            remaining = repetitions % loop_size
            return next(state for state, n in seen.items() if n == remaining)
        seen[p_str] = i

        for move in moves:
            move_type = move[0]
            if move_type == "s":
                programs = spin(programs, int(move[1:]))
            elif move_type == "x":
                programs = exchange(programs, *map(int, move[1:].split("/")))
            elif move_type == "p":
                programs = partner(programs, move[1], move[3])
            else:
                raise Exception("unknown move")
    return "".join(programs)


def spin(programs, n: int):
    return [*programs[-n:], *programs[:-n]]


def exchange(programs, a: int, b: int):
    programs[a], programs[b] = programs[b], programs[a]
    return programs


def partner(programs, a: str, b: str):
    a_i = programs.index(a)
    b_i = programs.index(b)
    return exchange(programs, a_i, b_i)


def main(txt: str):
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data
    main(data)
