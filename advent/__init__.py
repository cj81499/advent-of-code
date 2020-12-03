"""cj's solutions for https://adventofcode.com/"""
import importlib
from pathlib import Path


def solve(year, day, data):
    ans_a, ans_b = "unknown", "unknown"
    try:
        pkg = importlib.import_module(f"src.aoc{year}.day{day:02d}")
        ans_a = pkg.parta(data) if hasattr(pkg, "parta") else "unknown"
        ans_b = pkg.partb(data) if hasattr(pkg, "partb") else "unknown"
        return ans_a, ans_b
    except Exception as e:
        p = Path(__file__).parent / f"aoc{year}/day{day:02d}.log"
        with open(p, "w+") as f:
            for x in [data, ans_a, ans_b, str(e), str(e.with_traceback)]:
                f.write(f"{x}\n\n")
    return ans_a, ans_b
