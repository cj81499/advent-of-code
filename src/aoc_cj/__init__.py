"""cj's solutions for https://adventofcode.com/"""

import importlib
import inspect
import logging
from pathlib import Path
from types import ModuleType
from typing import Literal, Optional, Union

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(exist_ok=True)

Answer = Optional[Union[int, str]]


logging.basicConfig(
    filename=LOGS_DIR / "aoc_cj.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)


def solve(year: int, day: int, data: str) -> tuple[Answer, Answer]:  # pragma: no cover
    ans_a: Answer = None
    ans_b: Answer = None

    module_name = f"{__name__}.aoc{year}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)

        ans_a = _solve_part(module, data, "a")
        ans_b = _solve_part(module, data, "b")
    except ModuleNotFoundError as e:
        raise NotImplementedError(f"module '{module_name}' not found") from e
    except Exception as e:
        logging.exception("exception thrown while solving year=%s day=%s", year, day)
        raise e
    finally:
        logging.info("result for year=%s day=%s: (parta: %s, partb: %s)", year, day, ans_a, ans_b)

    return ans_a, ans_b


def _solve_part(module: ModuleType, data: str, part: Literal["a", "b"]) -> Answer:  # pragma: no cover
    if f := getattr(module, f"part{part}", None):
        assert inspect.isfunction(f), f"f ({f}) is not a function"
        try:
            # TODO: consider checking that inspect.signature matches expected signature
            resp = f(data)
            assert isinstance(resp, (int, str)) or resp is None, f"resp ({resp}) must be an int, str, or None"
            return resp
        except NotImplementedError:  # unsolved
            return None
    return None
