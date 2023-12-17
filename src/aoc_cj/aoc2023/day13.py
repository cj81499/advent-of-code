import itertools
from typing import Optional

import numpy as np
import numpy.typing as npt

NDArrayChar = npt.NDArray[np.str_]


class NoReflectionError(RuntimeError):
    pass


def reflection_score(arr: NDArrayChar, *, dont_return: Optional[int] = None) -> int:
    height, width = arr.shape
    for reflect_after in range(1, width):
        num_cols_to_consider = min(reflect_after, width - reflect_after)
        before_cols = arr[:, reflect_after - num_cols_to_consider : reflect_after]
        after_cols = arr[:, reflect_after : reflect_after + num_cols_to_consider]
        mirrored = np.fliplr(after_cols)
        if np.array_equal(before_cols, mirrored) and dont_return != reflect_after:
            return reflect_after

    for reflect_after in range(1, height):
        num_rows_to_consider = min(reflect_after, height - reflect_after)
        before_rows = arr[reflect_after - num_rows_to_consider : reflect_after, :]
        after_rows = arr[reflect_after : reflect_after + num_rows_to_consider, :]
        mirrored = np.flipud(after_rows)
        if np.array_equal(before_rows, mirrored) and dont_return != (res := 100 * reflect_after):
            return res

    raise NoReflectionError()


def smudged_reflection_score(arr: NDArrayChar) -> int:
    original_score = reflection_score(arr)

    height, width = arr.shape

    # since we'll be mutating it and don't want to change it from the caller's
    # perspective, create and use a copy of arr for the rest of the function
    arr = arr.copy()

    for x, y in itertools.product(range(width), range(height)):  # pragma: no branch # we expect to return while looping
        # swap ash w/ rocks or vice versa to try to "fix the smudge"
        arr[y, x] = "#" if arr[y, x] == "." else "."
        try:
            return reflection_score(arr, dont_return=original_score)
        except NoReflectionError:
            # the swap didn't "fix the smudge". undo it
            arr[y, x] = "#" if arr[y, x] == "." else "."

    raise NoReflectionError()  # pragma: no cover # we expect to return while looping


def parta(txt: str) -> int:
    patterns = [np.char.array([[*line] for line in tp.splitlines()]) for tp in txt.split("\n\n")]
    return sum(reflection_score(p) for p in patterns)


def partb(txt: str) -> int:
    patterns = [np.char.array([[*line] for line in tp.splitlines()]) for tp in txt.split("\n\n")]
    return sum(smudged_reflection_score(p) for p in patterns)


if __name__ == "__main__":
    from aocd import data

    print(f"parta: {parta(data)}")
    print(f"partb: {partb(data)}")
