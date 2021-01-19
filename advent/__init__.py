"""cj's solutions for https://adventofcode.com/"""
import importlib
from pathlib import Path

ADVENT_DIR = Path(__file__).parent


def solve(year, day, data):
    pkg = None
    ans_a, ans_b = None, None
    year_str = f"aoc{year}"
    day_str = f"day{day:02d}"
    try:
        pkg = importlib.import_module(f"advent.{year_str}.{day_str}")
        if hasattr(pkg, "parta"):
            ans_a = pkg.parta(data)
        if hasattr(pkg, "partb"):
            ans_b = pkg.partb(data)
    except ModuleNotFoundError:
        raise NotImplementedError()
    except Exception as e:
        # log the error if the package exists
        if pkg is not None:
            day_log = ADVENT_DIR / year_str / f"{day_str}.log"
            with open(day_log, "w") as log:
                log.write(f"{repr(e)}\n")
                log.write(f"ans a: {ans_a}\n")
                log.write(f"ans b: {ans_b}\n")
        raise e
    return ans_a, ans_b
