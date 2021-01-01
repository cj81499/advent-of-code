import colorama

colorama.init()


def load_input(number, puzzle_name=None):
    if puzzle_name is not None:
        print(f"{colorama.Fore.BLUE}--- Day {number}: {puzzle_name} ---" + colorama.Style.RESET_ALL)
    else:
        print(f"{colorama.Fore.RED}NO PUZZLE NAME GIVEN" + colorama.Style.RESET_ALL)
    try:
        import os
        with open(f"{os.path.dirname(__file__)}/input/day{str(number).zfill(2)}_input.txt") as f:
            input_txt = f.read().strip()
        input_lines = input_txt.split("\n")
        input_lines = input_txt.splitlines()
        print(f"{colorama.Fore.GREEN}SUCCESSFULLY READ INPUT" + colorama.Style.RESET_ALL)
    except FileNotFoundError as _err:  # noqa
        print(f"{colorama.Fore.RED}ERROR: Couldn't read input file." + colorama.Style.RESET_ALL)
        exit()
    return input_txt, input_lines
