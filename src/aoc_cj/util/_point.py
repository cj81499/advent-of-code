import dataclasses
import re
from collections.abc import Generator

__all__ = ("Point3D",)


# TODO: Implement a more general N-dimensional point to replace Point3D.
# NOTE: it'll need to support neighbors w/ and w/o "corners".
# eg: a 2D point could have 4 or 8 neighbors (depending on if you include corners).
# similarly, a 3D point could have 6 or 10 neighbors.
@dataclasses.dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    PARSE_REGEX = re.compile(r"(\d+)\D+(\d+)\D+(\d+)")

    @staticmethod
    def parse(s: str) -> "Point3D":
        m = Point3D.PARSE_REGEX.match(s)
        if m is None:
            msg = "Failed to parse Point3d"
            raise ValueError(msg)
        x, y, z = map(int, m.groups())
        return Point3D(x, y, z)

    def adj(self) -> Generator["Point3D"]:
        yield Point3D(self.x + 1, self.y, self.z)
        yield Point3D(self.x - 1, self.y, self.z)
        yield Point3D(self.x, self.y + 1, self.z)
        yield Point3D(self.x, self.y - 1, self.z)
        yield Point3D(self.x, self.y, self.z + 1)
        yield Point3D(self.x, self.y, self.z - 1)
