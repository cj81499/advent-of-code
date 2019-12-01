import os
from datetime import date
from pathlib import Path
from typing import List, Tuple

import requests
from dotenv import load_dotenv

from logger import Logger

load_dotenv()

INPUT_DIR = "input"
INPUT_PREFIX = "input-"

SESSION = os.getenv("SESSION_COOKIE")
if SESSION is None:
    Logger.error("SESSION_COOKIE environment variable is not set")


def get_puzzle(target: date, puzzle_name: str = None) -> Tuple[str, List[str]]:
    assert target.month == 12, "Advent of Code is only in December"
    assert 1 <= target.day, "Day must be at least 1"
    assert target.day <= 25, "Day must be at most 25"

    today = date.today()
    puzzle_available = today >= target

    if not puzzle_available:
        Logger.error(f"The puzzle for {target} is not available")
        exit()

    _print_puzzle_message(target, puzzle_name)
    puzzle_path = _get_puzzle_path(target)

    if puzzle_path.exists():
        txt = read_puzzle(puzzle_path)
    else:
        Logger.warn(f"{puzzle_path.name} doesn't exist")
        txt = _download_puzzle(target)
        save_puzzle(txt, puzzle_path)

    txt = txt.strip()
    lines = txt.splitlines()

    return txt, lines


def _print_puzzle_message(d: date, name: str) -> None:
    body = f"--- Day {d.day}: {name if name else '????'} ---"
    fn = Logger.info if name else Logger.warn
    fn(body)


def _get_puzzle_path(target: date) -> Path:
    current_file = Path(__file__).absolute()
    src_dir = current_file.parent
    proj_dir = src_dir.parent
    input_filename = f"{INPUT_PREFIX}{target}.txt"
    return proj_dir / INPUT_DIR / input_filename


def _download_puzzle(target: date) -> str:
    Logger.info(f"Downloading puzzle input for {target}")
    try:
        response = requests.get(
            f"http://adventofcode.com/{target.year}/day/{target.day}/input",
            cookies={"session": SESSION}
        )
        txt = response.text
        Logger.success("Puzzle input downloaded")
        return txt
    except requests.exceptions.RequestException as e:
        Logger.error("Failed to download puzzle input")
        raise e


def save_puzzle(puzzle: str, puzzle_path: Path) -> None:
    puzzle_path.write_text(puzzle)
    Logger.success(f"Puzzle input saved as {puzzle_path.name}")


def read_puzzle(puzzle: Path) -> str:
    return puzzle.read_text().strip()
