import datetime
import logging
import logging.config
from concurrent.futures import InterpreterPoolExecutor

import aocd
import structlog
from aocd.models import Puzzle

_LOGGER: structlog.stdlib.BoundLogger = structlog.get_logger(__name__)
logging.basicConfig(level=logging.INFO)

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


def solve(p: Puzzle) -> tuple[object, object]:
    _LOGGER.info("Solving %s.", p)
    try:
        result = p.solve()
    except BaseException as e:
        _LOGGER.error(f"Error solving %s/%s: %s.", p.year, p.day, e)
        return None, None
    _LOGGER.info(f"Solved %s/%s: %s.", p.year, p.day, result)
    return result


def now() -> datetime.datetime:
    return datetime.datetime.now(tz=datetime.UTC)


def main() -> None:
    puzzles = Puzzle.all()
    numpy_skip = [
        (2017, 21),
        (2018, 11),
        (2020, 20),
        (2023, 13),
    ]
    futures = []
    with InterpreterPoolExecutor() as executor:
        for p in puzzles:
            if (p.year, p.day) in numpy_skip:
                _LOGGER.warn(f"Skipping {p} due to numpy issues.")
                continue
            f = executor.submit(solve, p)
            f.add_done_callback(
                lambda fut, p=p: aocd.submit(fut.result()[0], part="a", day=p.day, year=p.year)
                if fut.result()[0] is not None
                else None
            )
            f.add_done_callback(
                lambda fut, p=p: aocd.submit(fut.result()[1], part="b", day=p.day, year=p.year)
                if fut.result()[1] is not None
                else None
            )
            futures.append(f)


if __name__ == "__main__":
    main()
