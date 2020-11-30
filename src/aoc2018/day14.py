def part1(txt: str):
    num = int(txt)
    elf1_i = 0
    elf2_i = 1
    board = [3, 7]
    while len(board) <= 10 + num:
        sum_of_recipies = board[elf1_i] + board[elf2_i]

        board.extend(list(map(int, str(sum_of_recipies))))

        elf1_i = (elf1_i + 1 + board[elf1_i]) % len(board)
        elf2_i = (elf2_i + 1 + board[elf2_i]) % len(board)
    return "".join(map(str, board[num:num + 10]))


def part2(txt: str):
    digits = [int(x) for x in txt.strip()]

    elf1_i = 0
    elf2_i = 1
    board = [3, 7]
    while txt not in "".join(map(str, board[-(len(digits) + 1):])):
        sum_of_recipies = board[elf1_i] + board[elf2_i]

        board.extend(list(map(int, str(sum_of_recipies))))

        elf1_i = (elf1_i + 1 + board[elf1_i]) % len(board)
        elf2_i = (elf2_i + 1 + board[elf2_i]) % len(board)
    return len(board) - len(digits) - (0 if "".join(map(str, board[-len(digits):])) == txt else 1)


def main():
    input_txt, _ = helpers.load_input(14, "Chocolate Charts")

    print(f"part1: {part1(input_txt)}")
    print(f"part2: {part2(input_txt)}")


if __name__ == "__main__":
    import helpers
    main()
