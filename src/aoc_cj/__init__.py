"""cj's solutions for https://adventofcode.com/"""

import importlib
import logging
from types import ModuleType
from typing import Literal

type Answer = int | str | None
type Part = Literal[1, 2]

_LOGGER = logging.getLogger(__name__)


def solve(year: int, day: int, data: str) -> tuple[Answer, Answer]:  # pragma: no cover
    ans_1: Answer = None
    ans_2: Answer = None

    module_name = f"{__name__}.aoc{year}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)

        ans_1 = _solve_part(module, data, 1)
        ans_2 = _solve_part(module, data, 2)
    except ModuleNotFoundError as e:
        msg = f"module '{module_name}' not found"
        raise NotImplementedError(msg) from e
    except Exception:
        _LOGGER.exception("exception thrown while solving year=%s day=%s", year, day)
        raise
    finally:
        _LOGGER.info("result for year=%s day=%s: (part_1: %s, part_2: %s)", year, day, ans_1, ans_2)

    return ans_1, ans_2


def _solve_part(module: ModuleType, data: str, part: Part) -> Answer:  # pragma: no cover
    if f := getattr(module, f"part_{part}", None):
        assert callable(f), f"f ({f}) is not callable"
        try:
            # TODO: consider checking that inspect.signature matches expected signature
            resp = f(data)
        except NotImplementedError:  # unsolved
            return None
        assert resp is None or isinstance(resp, (int, str)), f"resp ({resp}) must be an int, str, or None"
        return resp
    return None
