"""cj's solutions for https://adventofcode.com/"""

import importlib
import logging
from pathlib import Path
from typing import Union

ADVENT_DIR = Path(__file__).parent
SRC_DIR = ADVENT_DIR.parent
PROJECT_ROOT = SRC_DIR.parent


def _NULL(_):
    return None


logging.basicConfig(
    filename=PROJECT_ROOT / "aoc_cj.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)

Answer = Union[int, str]


def solve(year, day, data) -> tuple[Answer, Answer]:
    day_str = f"{day:02d}"
    logger = logging.getLogger(f"y{year} d{day_str}")

    ans_a: Answer = None
    ans_b: Answer = None

    try:
        module = importlib.import_module(f"aoc_cj.aoc{year}.day{day_str}")
        ans_a = getattr(module, f"parta", _NULL)(data)
        ans_b = getattr(module, f"partb", _NULL)(data)
    except ModuleNotFoundError as e:
        raise NotImplementedError() from e
    except Exception as e:
        logger.exception(e)
        raise e
    finally:
        logger.info("got (%s, %s)", ans_a, ans_b)

    return ans_a, ans_b
