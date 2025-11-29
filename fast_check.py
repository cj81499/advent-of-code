import asyncio
import functools
import logging
import logging.config
import os
import time
from collections.abc import Generator
from typing import override

import anyio
import anyio.to_interpreter
import anyio.to_process
import aocd
import rich.containers
import rich.live
import rich.measure
import rich.panel
import rich.spinner
import rich.table
import rich.text
from aocd.models import Puzzle

_LOGGER = logging.getLogger(__name__)


class Slot(rich.console.ConsoleRenderable):
    def __init__(self, child: rich.console.RenderableType) -> None:
        self._child = child

    @property
    def child(self) -> rich.console.RenderableType:
        return self._child

    @child.setter
    def child(self, new_child: rich.console.RenderableType) -> None:
        self._child = new_child

    @override
    def __rich_console__(
        self, console: rich.console.Console, options: rich.console.ConsoleOptions
    ) -> rich.console.RenderResult:
        yield self._child

    def __rich_measure__(
        self,
        console: rich.console.Console,
        options: rich.console.ConsoleOptions,
    ) -> rich.measure.Measurement:
        # Delegate sizing to the child so the table sees the real width
        return rich.measure.Measurement.get(console, options, self.child)


class Timer:
    def __init__(self) -> None:
        self._started_at = time.monotonic()
        self._stopped_at: float | None = None

    @property
    def elapsed(self) -> float:
        return (self._stopped_at or time.monotonic()) - self._started_at

    def stop(self) -> None:
        assert self._stopped_at is None
        self._stopped_at = time.monotonic()

    def _render(self) -> str:
        return f"{self.elapsed:.2f}"

    def __rich_console__(
        self, console: rich.console.Console, options: rich.console.ConsoleOptions
    ) -> rich.console.RenderResult:
        yield self._render()

    def __rich_measure__(
        self, console: rich.console.Console, options: rich.console.ConsoleOptions
    ) -> rich.measure.Measurement:
        return rich.measure.Measurement.get(console, options, self._render())


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


def _solve_simple(year: int, day: int) -> tuple[object, object]:
    async def _inner() -> tuple[object, object]:
        puzzle = Puzzle(year=year, day=day)
        try:
            return puzzle.solve()
        except BaseException as e:
            logging.exception(f"failed to solve {puzzle=}")
            return None, None

    return anyio.run(_inner)


async def main() -> None:
    # TODO: implement filtering
    to_solve = tuple(p for p in MyPuzzle.all() if p.year >= 2024)

    table = rich.table.Table(
        collapse_padding=True,
        pad_edge=False,
        show_header=False,
        box=None,
    )
    table.add_column("ID")
    table.add_column("Duration", justify="right")
    table.add_column("Part 1")
    table.add_column("Part 2")

    async with anyio.create_task_group() as tg:
        # HACK: there's likely a better way to track this. Ideally, we'd "wait" until we're notified somehow...?
        waiting = set(to_solve)

        async def _inner(p: Puzzle, limiter: anyio.CapacityLimiter, *, timeout: float | None) -> None:
            async with limiter:
                timer = Timer()
                slot_a = Slot(rich.spinner.Spinner("dots"))
                slot_b = Slot(rich.spinner.Spinner("dots"))
                table.add_row(f"{p.year}/{p.day:02} - {p.title}", timer, slot_a, slot_b)
                try:
                    with anyio.fail_after(delay=timeout):
                        # TODO: maybe one day we can use `anyio.to_interpreter`. For now, there's no good way to cancel.
                        ans_a, ans_b = await anyio.to_process.run_sync(p.solve, cancellable=True)
                except TimeoutError:
                    result_a = result_b = rich.text.Text("TIMEOUT", style="yellow")
                except NotImplementedError:
                    result_a = result_b = rich.text.Text("NOT IMPLEMENTED", style="purple")
                except Exception as e:
                    result_a = result_b = rich.text.Text("FAILED", style="red")
                    _LOGGER.exception(f"Unexpected error while solving puzzle {p=}")
                else:
                    correct_ans_a = getattr(p, "answer_a", None)
                    is_correct_a = str(correct_ans_a) == str(ans_a)
                    result_a = rich.text.Text.assemble(
                        *(
                            "part 1: ",
                            (f"{ans_a}", "green" if is_correct_a else "red"),
                            "" if is_correct_a else f" (expected {correct_ans_a=})",
                        ),
                        overflow="ellipsis",
                        no_wrap=True,
                    )
                    correct_ans_b = getattr(p, "answer_b", None)
                    is_correct_b = str(correct_ans_b) == str(ans_b)
                    result_b = rich.text.Text.assemble(
                        *(
                            "part 2: ",
                            (f"{ans_b}", "green" if is_correct_b else "red"),
                            "" if is_correct_b else f" (expected {correct_ans_b=})",
                        ),
                        overflow="ellipsis",
                        no_wrap=True,
                    )
                timer.stop()
                slot_a.child = result_a
                slot_b.child = result_b
                waiting.remove(p)

        # TODO: allow user-override
        limiter = anyio.CapacityLimiter(os.process_cpu_count() or os.cpu_count() or 4)
        for p in to_solve:
            tg.start_soon(functools.partial(_inner, p, limiter, timeout=10))

        with rich.live.Live(
            table,
            refresh_per_second=20,
            transient=True,
        ) as _live:
            while waiting:
                await asyncio.sleep(1)

    print("All solved!")


if __name__ == "__main__":
    import rich.logging

    rich.logging.RichHandler()
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "stderr": {
                    "class": "rich.logging.RichHandler",
                    # "class": "logging.StreamHandler",
                    "formatter": "rich",
                    "level": "NOTSET",
                    "show_time": True,
                    "omit_repeated_times": True,
                    "show_level": True,
                    "show_path": True,
                    "log_time_format": "%Y-%m-%dT%H:%M:%S%z",
                    "rich_tracebacks": True,
                    # "stream": "ext://sys.stderr",
                },
            },
            "formatters": {
                "rich": {
                    "format": "%(name)s | %(module)s | %(message)s",
                    "datefmt": "%Y-%m-%dT%H:%M:%S%z",
                },
            },
            "loggers": {
                "root": {"handlers": ["stderr"], "level": "NOTSET"},
                "aocd": {"level": "INFO"},
                "asyncio": {"level": "INFO"},
                "urllib3.connectionpool": {"level": "INFO"},
            },
        }
    )

    anyio.run(main)
