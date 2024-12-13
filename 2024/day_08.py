"""
day_08.py

Day 8: Resonant Collinearity

https://adventofcode.com/2024/day/8
"""

from collections import defaultdict
from itertools import combinations
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.map: list[str] = []

        self.antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

        with DATA_PATH.joinpath("08.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.map.append(line.strip())

        for idx, row in enumerate(self.map):
            for jdx, char in enumerate(row):
                if char == ".":
                    continue

                self.antennas[char].append((idx, jdx))

        self.i_length = len(self.map)
        self.j_length = len(self.map[0])

    def part1(self) -> int:
        """part1"""

        antinodes: set[tuple[int, int]] = set()

        for locations in self.antennas.values():
            if len(locations) < 2:
                continue

            antinodes.update(self._calculate_antinodes_1(locations=locations))

        return len(antinodes)

    def _calculate_antinodes_1(
        self, locations: list[tuple[int, int]]
    ) -> set[tuple[int, int]]:
        """calculate antinodes for part 1"""

        antinodes: set[tuple[int, int]] = set()

        for location_1, location_2 in combinations(locations, 2):
            i_1, j_1 = location_1
            i_2, j_2 = location_2

            i_potential_1 = 2 * i_1 - i_2
            j_potential_1 = 2 * j_1 - j_2

            if (
                0 <= i_potential_1 < self.i_length
                and 0 <= j_potential_1 < self.j_length
            ):
                antinodes.add((i_potential_1, j_potential_1))

            i_potential_2 = 2 * i_2 - i_1
            j_potential_2 = 2 * j_2 - j_1

            if (
                0 <= i_potential_2 < self.i_length
                and 0 <= j_potential_2 < self.j_length
            ):
                antinodes.add((i_potential_2, j_potential_2))

        return antinodes

    def part2(self) -> int:
        """part2"""

        antinodes: set[tuple[int, int]] = set()

        for locations in self.antennas.values():
            if len(locations) < 2:
                continue

            antinodes.update(self._calculate_antinodes_2(locations=locations))

        return len(antinodes)

    def _calculate_antinodes_2(  # noqa: C901
        self, locations: list[tuple[int, int]]
    ) -> set[tuple[int, int]]:
        """calculate antinodes for part 2"""

        antinodes: set[tuple[int, int]] = set()

        for location_1, location_2 in combinations(locations, 2):
            antinodes.add(location_1)
            antinodes.add(location_2)

            i_1, j_1 = location_1
            i_2, j_2 = location_2

            diff_i = i_2 - i_1
            diff_j = j_2 - j_1

            if diff_i > 0:
                jdx = j_2

                for idx in range(i_2 + diff_i, self.i_length, diff_i):
                    jdx += diff_j

                    if jdx < 0 or jdx >= self.j_length:
                        break

                    antinodes.add((idx, jdx))

                jdx = j_1

                for idx in range(i_1 - diff_i, -1, -diff_i):
                    jdx -= diff_j

                    if jdx < 0 or jdx >= self.j_length:
                        break

                    antinodes.add((idx, jdx))
            else:
                jdx = j_2

                for idx in range(i_2 - diff_i, self.i_length, -diff_i):
                    jdx += diff_j

                    if jdx < 0 or jdx >= self.j_length:
                        break

                    antinodes.add((idx, jdx))

                jdx = j_1

                for idx in range(i_1 + diff_j, -1, diff_i):
                    jdx -= diff_j

                    if jdx < 0 or jdx >= self.j_length:
                        break

                    antinodes.add((idx, jdx))

        return antinodes


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
