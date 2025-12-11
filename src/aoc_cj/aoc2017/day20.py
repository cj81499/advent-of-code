import dataclasses
import re
from collections import Counter


@dataclasses.dataclass(frozen=True, eq=True)
class Particle:
    pos: tuple[int, int, int]
    vel: tuple[int, int, int]
    acc: tuple[int, int, int]

    _PARSE_REGEX = re.compile(
        r"p=< *(-?\d+), *(-?\d+), *(-?\d+)>, v=< *(-?\d+), *(-?\d+), *(-?\d+)>, a=< *(-?\d+), *(-?\d+), *(-?\d+)>"
    )

    @staticmethod
    def parse(particle: str):
        nums = tuple(map(int, Particle._PARSE_REGEX.match(particle).groups()))
        pos = tuple(nums[:3])
        vel = tuple(nums[3:-3])
        acc = tuple(nums[-3:])
        return Particle(pos, vel, acc)

    def advance(self, steps=1):
        assert steps >= 0
        vel = self.vel
        pos = self.pos
        for _step in range(steps):
            vel = tuple(v + a for v, a in zip(vel, self.acc, strict=True))
            pos = tuple(p + v for p, v in zip(pos, vel, strict=True))
        return Particle(pos, vel, self.acc)


# 500 steps was enough for me to get the correct answer, so 1000 seems like a safe bet while still running quickly.
STEPS = 1000


def part_1(txt: str):
    particles = [Particle.parse(line) for line in txt.splitlines()]
    particles_after_delay = [p.advance(STEPS) for p in particles]
    min_particle = min(particles_after_delay, key=lambda p: sum(map(abs, p.pos)))
    return particles_after_delay.index(min_particle)


def part_2(txt: str):
    particles = {Particle.parse(line) for line in txt.splitlines()}
    for _step in range(STEPS):
        particles = {p.advance() for p in particles}
        position_counts = Counter(p.pos for p in particles)
        for pos, n in position_counts.most_common():
            # once we reach a position with only 1 particle, there's no more to remove
            if n == 1:
                break
            particles = {p for p in particles if p.pos != pos}
    return len(particles)


if __name__ == "__main__":
    import aocd

    print(f"part_1: {part_1(aocd.data)}")
    print(f"part_2: {part_2(aocd.data)}")
