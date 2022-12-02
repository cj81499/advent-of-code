def move_score(op_move: str, my_move: str) -> int:
    points = {"X": 1, "Y": 2, "Z": 3}[my_move]

    if op_move == "A":  # r
        if my_move == "X":  # r
            points += 3
        elif my_move == "Y":  # p
            points += 6
        elif my_move == "Z":  # s
            points += 0
    elif op_move == "B":  # p
        if my_move == "X":  # r
            points += 0
        elif my_move == "Y":  # p
            points += 3
        elif my_move == "Z":  # s
            points += 6
    elif op_move == "C":  # s
        if my_move == "X":  # r
            points += 6
        elif my_move == "Y":  # p
            points += 0
        elif my_move == "Z":  # s
            points += 3

    return points


def parta(txt: str) -> int:
    total_score = 0
    for turn in txt.splitlines():
        op_move, my_move = turn.split()
        total_score += move_score(op_move, my_move)

    return total_score


def partb(txt: str) -> int:
    total_score = 0
    for turn in txt.splitlines():
        op_move, desired_outcome = turn.split()
        my_move = {
            # loss
            "X": {
                "A": "Z",
                "B": "X",
                "C": "Y",
            },
            # draw
            "Y": {
                "A": "X",
                "B": "Y",
                "C": "Z",
            },
            # win
            "Z": {
                "A": "Y",
                "B": "Z",
                "C": "X",
            },
        }[desired_outcome][op_move]

        total_score += move_score(op_move, my_move)

    return total_score


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
