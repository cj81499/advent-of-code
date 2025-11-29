import logging.config
import subprocess

import anyio
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


async def main() -> None:
    results = {}

    async def _inner(puzzle: Puzzle, semaphore: anyio.Semaphore) -> None:
        async with semaphore:
            _LOGGER.info("Solving", puzzle=puzzle)
            try:
                result = await anyio.run_process(
                    ["aoc", "-y", str(puzzle.year), "-d", str(puzzle.day), "-t", "60"],
                )
            except subprocess.CalledProcessError as e:
                _LOGGER.error(
                    "Error solving puzzle",
                    puzzle=puzzle,
                    returncode=e.returncode,
                    output=e.output,
                    stderr=e.stderr,
                )
                result = None

            _LOGGER.info("Got result", puzzle=puzzle, result=result)
        results[puzzle] = result

    async with anyio.create_task_group() as tg:
        all_puzzles = tuple(Puzzle.all())

        semaphore = anyio.Semaphore(32)
        for p in all_puzzles:
            _LOGGER.debug("Scheduling", puzzle=p)
            tg.start_soon(_inner, p, semaphore)

        _LOGGER.info("All scheduled")

    _LOGGER.info("Results:", results=results)


if __name__ == "__main__":
    anyio.run(main)
