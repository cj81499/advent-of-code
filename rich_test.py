#!/usr/bin/env python3

import asyncio
import collections
import dataclasses
import enum
import logging
import logging.config
import os
import time
from collections.abc import Callable, Iterable

import anyio
import anyio.to_process
import aocd.models
import click
import rich.color
import rich.columns
import rich.live
import rich.style
import rich.styled
import rich.table

_LOGGER = logging.getLogger(__name__)


_TARGET_FPS = 20

_TIMEOUT_DURATION_S = 10


class FinishReason(enum.Enum):
    RETURNED = enum.auto()
    EXCEPTION = enum.auto()
    TIMEOUT = enum.auto()


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class InProgressPuzzle:
    puzzle: aocd.models.Puzzle
    start_time: float = dataclasses.field(default_factory=time.monotonic)

    def duration(self) -> float:
        return time.monotonic() - self.start_time


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class FinishedPuzzle:
    puzzle: aocd.models.Puzzle
    finish_reason: FinishReason
    ans_a: aocd.types.AnswerValue | None
    ans_b: aocd.types.AnswerValue | None
    start_time: float
    end_time: float = dataclasses.field(default_factory=time.monotonic)

    def duration(self) -> float:
        return self.end_time - self.start_time


_PARALLEL_LIMIT = os.process_cpu_count() or os.cpu_count() or 4


@click.command()
@click.option("--year", "years", multiple=True, type=int)
@click.option("--puzzle", "puzzles", multiple=True, type=int, nargs=2)
def main(years: tuple[int, ...], puzzles: tuple[tuple[int, int], ...]) -> None:

    async def _main() -> None:
        try:
            print(years, puzzles)

            _puzzles = aocd.models.Puzzle.all()
            if years or puzzles:
                _puzzles = (
                    p
                    for p in _puzzles
                    if any(
                        (
                            years and p.year in years,
                            puzzles and ((p.year, p.day) in puzzles),
                        )
                    )
                )
            pending_puzzles = collections.deque(sorted(_puzzles, key=lambda p: (p.year, p.day)))

            processing_puzzles = set[InProgressPuzzle]()
            finished_puzzles = list[FinishedPuzzle]()

            stop_event = anyio.Event()
            with rich.live.Live("", auto_refresh=False, transient=True) as live:

                async def _render(render_frame: Callable[[], rich.console.RenderableType]) -> None:
                    while not stop_event.is_set():
                        live.update(render_frame(), refresh=True)
                        await anyio.sleep(1 / _TARGET_FPS)

                async with anyio.create_task_group() as tg1:

                    def render_frame() -> rich.console.RenderableType:
                        recently_finished_table = _render_finished_puzzles(finished_puzzles[-_PARALLEL_LIMIT:])
                        recently_finished_table.title = "Recently Finished"

                        t = rich.table.Table("Puzzle", "Duration", title="Running Puzzles")
                        for p in sorted(processing_puzzles, key=lambda p: (p.puzzle.year, p.puzzle.day)):
                            t.add_row(f"{p.puzzle.year}/{p.puzzle.day}", f"{p.duration():0.2}")

                        return rich.columns.Columns(renderables=(t, recently_finished_table))

                    _ = tg1.start_soon(_render, render_frame)

                    async def _solve(p: aocd.models.Puzzle) -> None:
                        in_progress_puzzle = InProgressPuzzle(puzzle=p)
                        processing_puzzles.add(in_progress_puzzle)
                        a = b = None
                        try:
                            with anyio.fail_after(_TIMEOUT_DURATION_S):
                                a, b = await anyio.to_process.run_sync(p.solve, cancellable=True)
                        except TimeoutError:
                            finish_reason = FinishReason.TIMEOUT
                        except:
                            finish_reason = FinishReason.EXCEPTION
                        else:
                            finish_reason = FinishReason.RETURNED

                        finished_puzzles.append(
                            FinishedPuzzle(
                                puzzle=p,
                                finish_reason=finish_reason,
                                ans_a=a,
                                ans_b=b,
                                start_time=in_progress_puzzle.start_time,
                            )
                        )
                        processing_puzzles.remove(in_progress_puzzle)

                    # execute puzzles
                    async with anyio.create_task_group() as tg2:
                        while pending_puzzles:
                            while pending_puzzles and len(processing_puzzles) < _PARALLEL_LIMIT:
                                _ = tg2.start_soon(_solve, pending_puzzles.popleft())
                                await asyncio.sleep(0)
                            await asyncio.sleep(0)

                    # await anyio.sleep(10)

                    stop_event.set()

        finally:
            t = _render_finished_puzzles(sorted(finished_puzzles, key=lambda p: (p.puzzle.year, p.puzzle.day)))
            rich.print(t)

    def _render_finished_puzzles(finished_puzzles: Iterable[FinishedPuzzle]) -> rich.color.Table:
        t = rich.table.Table("Puzzle", "Part 1", "Part 2", "Duration")
        for fp in finished_puzzles:
            duration_s = fp.end_time - fp.start_time
            puzzle = fp.puzzle
            a_correct = False
            if fp.ans_a is not None:
                if not puzzle.answered_a:
                    # try to submit the answer
                    puzzle.answer_a = fp.ans_a
                a_correct = puzzle.answer_a == str(fp.ans_a)
            b_correct = False
            if fp.ans_b is not None:
                if not puzzle.answered_b:
                    # try to submit the answer
                    puzzle.answer_b = fp.ans_b
                b_correct = puzzle.answer_b == str(fp.ans_b)

            t.add_row(
                f"{puzzle.year}/{puzzle.day}",
                rich.styled.Styled(str(fp.ans_a), "green" if a_correct else "red")
                if fp.finish_reason == FinishReason.RETURNED and fp.ans_a is not None
                else None,
                rich.styled.Styled(str(fp.ans_b), "green" if b_correct else "red")
                if fp.finish_reason == FinishReason.RETURNED and fp.ans_b is not None
                else None,
                rich.styled.Styled(f"{_TIMEOUT_DURATION_S:5.2f}s (Timeout)", rich.style.Style(color="red"))
                if fp.finish_reason == FinishReason.TIMEOUT
                else rich.styled.Styled(f"{duration_s:5.2f}s", "yellow" if duration_s > 2 else ""),
            )
        return t

    anyio.run(_main)


if __name__ == "__main__":
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

    main()
