from collections.abc import Iterable


class Point():
    def __init__(self, *args):
        assert len(args) > 0
        if len(args) == 1 and isinstance(args[0], Iterable):
            self.coords = tuple(x for x in args[0])
        else:
            self.coords = tuple(x for x in args)

    def __repr__(self):
        return f"Point{self.coords}"

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        assert isinstance(other, Point)
        assert (len(self) == len(other))
        return Point(x + y for (x, y) in zip(self.coords, other.coords))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        if len(self) != len(other):
            return False
        for (x, y) in zip(self.coords, other.coords):
            if x != y:
                return False
        return True

    def __hash__(self):
        return hash(self.coords)

        # if __name__ == "__main__":
        #     p1 = Point(1, 2, 3)
        #     p2 = Point(5, 4, 2)
        #     p3 = p1 + p2

        #     print(p1, p2, p3)
