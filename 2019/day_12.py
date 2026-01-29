"""
day_12.py

Day 12: The N-Body Problem

https://adventofcode.com/2019/day/12
"""

import math
import re
from itertools import combinations
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Moon:
    def __init__(self, x: int, y: int, z: int) -> None:
        """initiation"""

        self.x: int = x
        self.y: int = y
        self.z: int = z

        self.vx: int = 0
        self.vy: int = 0
        self.vz: int = 0


class Solution:
    def __init__(self) -> None:
        """initiation"""

        pattern: re.Pattern[str] = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
        self.moons: list[Moon] = []
        self.initial_positions: list[tuple[int, int, int]] = []

        with DATA_PATH.joinpath("12.txt").open("r", encoding="utf-8") as file:
            for line in file:
                match: re.Match[str] | None = pattern.match(line.strip())

                if match:
                    x, y, z = map(int, match.groups())
                    self.moons.append(Moon(x=x, y=y, z=z))
                    self.initial_positions.append((x, y, z))

    def part1(self) -> int:
        """part1"""

        for _ in range(1000):
            self._step()

        return sum(
            (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.vx) + abs(m.vy) + abs(m.vz))
            for m in self.moons
        )

    def _step(self) -> None:
        """one step"""

        for moon_a, moon_b in combinations(self.moons, 2):
            if moon_a.x < moon_b.x:
                moon_a.vx += 1
                moon_b.vx -= 1
            elif moon_a.x > moon_b.x:
                moon_a.vx -= 1
                moon_b.vx += 1

            if moon_a.y < moon_b.y:
                moon_a.vy += 1
                moon_b.vy -= 1
            elif moon_a.y > moon_b.y:
                moon_a.vy -= 1
                moon_b.vy += 1

            if moon_a.z < moon_b.z:
                moon_a.vz += 1
                moon_b.vz -= 1
            elif moon_a.z > moon_b.z:
                moon_a.vz -= 1
                moon_b.vz += 1

        for moon in self.moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz

    def part2(self) -> int:
        """part2"""

        def axis_period(positions: list[int]) -> int:
            velocities: list[int] = [0 for _ in positions]

            initial_positions: list[int] = positions[:]
            initial_velocities: list[int] = velocities[:]

            steps: int = 0

            while True:
                for i, j in combinations(range(len(positions)), 2):
                    if positions[i] < positions[j]:
                        velocities[i] += 1
                        velocities[j] -= 1
                    elif positions[i] > positions[j]:
                        velocities[i] -= 1
                        velocities[j] += 1

                for k in range(len(positions)):
                    positions[k] += velocities[k]

                steps += 1

                if positions == initial_positions and velocities == initial_velocities:
                    return steps

        px: int = axis_period([p[0] for p in self.initial_positions])
        py: int = axis_period([p[1] for p in self.initial_positions])
        pz: int = axis_period([p[2] for p in self.initial_positions])

        return math.lcm(px, py, pz)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
