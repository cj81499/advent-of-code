import functools
import logging
import logging.config
from collections.abc import Generator
from typing import override

import anyio
import anyio.to_interpreter
import aocd
import more_itertools
import structlog
from aocd.models import Puzzle

_LOGGER: structlog.stdlib.BoundLogger = structlog.get_logger(__name__)

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "stderr": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "root": {
                "handlers": ["stderr"],
                "level": "NOTSET",
            },
            "aocd.get": {"level": "WARNING"},
            "aocd.models": {"level": "WARNING"},
        },
    }
)


class MyPuzzle(Puzzle):
    @override
    def __repr__(self) -> str:
        return f"MyPuzzle(year={self.year}, day={self.day})"

    @override
    @classmethod
    def all(cls, user: aocd.models.User | None = None) -> Generator[Puzzle]:
        """
        Return an iterator over all known puzzles that are currently playable.
        """
        for p in super().all(user=user):
            yield cls(year=p.year, day=p.day)


def solve(p: Puzzle) -> tuple[object, object]:
    _LOGGER.info("Solving %s.", p)
    try:
        result = p.solve()
    except BaseException as e:
        _LOGGER.error(f"Error solving %s/%s: %s.", p.year, p.day, e)
        return None, None
    _LOGGER.info(f"Solved %s/%s: %s.", p.year, p.day, result)
    return result


def solve_simple(year: int, day: int) -> tuple[object, object]:
    puzzle = Puzzle(year=year, day=day)
    result = solve(puzzle)
    _LOGGER.info("solve_simple got result", puzzle=puzzle, result=result)
    return result


async def main() -> None:
    puzzles = MyPuzzle.all()
    numpy_skip = {
        (2017, 21),
        (2018, 11),
        (2020, 20),
        (2023, 13),
    }
    to_solve, to_skip = more_itertools.partition(lambda p: (p.year, p.day) in numpy_skip, puzzles)

    to_solve = tuple(p for p in to_solve if p.year == 2016)
    assert len(to_solve) == 25
    _LOGGER.warn(f"Skipping {tuple(to_skip)} due to numpy issues.")
    results = {}

    async def _inner(p: Puzzle, *, timeout: float | None) -> None:
        with anyio.fail_after(timeout):
            result = await anyio.to_interpreter.run_sync(solve_simple, p.year, p.day)
        _LOGGER.info("Got result", puzzle=p, result=result)
        results[p] = result

    async with anyio.create_task_group() as tg:
        for p in to_solve:
            _LOGGER.info("Scheduling", puzzle=p)
            tg.start_soon(functools.partial(_inner, p, timeout=60))
        _LOGGER.info("All scheduled")

        while unsolved := [p for p in to_solve if results.get(p) is None]:
            if len(unsolved) > 5:
                _LOGGER.info("Still unsolved puzzles", count=len(unsolved))
            else:
                _LOGGER.debug("unsolved", unsolved=unsolved)
            await anyio.sleep(5)

    _LOGGER.info("All solved!", results=results)


if __name__ == "__main__":
    anyio.run(main)
