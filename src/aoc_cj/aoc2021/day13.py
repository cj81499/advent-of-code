Point = tuple[int, int]


def parta(txt: str) -> int:
    points, folds = parse(txt)

    new_points = do_fold(points, folds[0])

    return len(new_points)


def parse(txt: str) -> tuple[set[Point], list[str]]:
    points_s, folds = txt.split("\n\n")
    points = {tuple(map(int, line.split(","))) for line in points_s.splitlines()}
    return points, folds.splitlines()


def partb(txt: str) -> str:
    points, folds = parse(txt)

    for fold in folds:
        points = do_fold(points, fold)

    max_x = max(x for x, _y in points)
    max_y = max(y for _x, y in points)
    rows = ["".join("#" if (x, y) in points else " " for x in range(max_x + 1)) for y in range(max_y + 1)]

    return "\n" + "\n".join(rows)


def do_fold(points: set[Point], fold: str) -> set[Point]:
    direction, fold_s = fold.split()[-1].split("=")
    fold_n = int(fold_s)

    return {(fold_n - abs(fold_n - x), y) if direction == "x" else (x, fold_n - abs(fold_n - y)) for x, y in points}


def main(txt: str) -> None:
    print(f"parta: {parta(txt)}")
    print(f"partb: {partb(txt)}")


if __name__ == "__main__":
    from aocd import data

    main(data)
