"""
2023 Day 11
https://adventofcode.com/2023/day/11
"""

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path


@dataclass
class Point:
    x: int
    y: int


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "11.txt"

    def part_one(self) -> int:
        """part one answer"""

        lines: list[str] = []
        column_galaxy: dict[int, list[list[int]]] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                galaxy_found = 0

                lines.append(line)

                for idx, spot in enumerate(line):
                    if spot == "#":
                        galaxy_found += 1
                        if idx not in column_galaxy:
                            column_galaxy[idx] = [[idx, len(lines) - 1]]
                        else:
                            column_galaxy[idx].append([idx, len(lines) - 1])

                if not galaxy_found:
                    lines.append(line)

        for idx in range(len(lines[0])):
            column = [line[idx] for line in lines]

            if "#" in column:
                continue

            for col, galaxies in column_galaxy.items():
                if col > idx:
                    for gal in galaxies:
                        gal[0] = gal[0] + 1

        galaxies = []

        for galaxy in column_galaxy.values():
            galaxies.extend(galaxy)

        answer = 0

        for gal1, gal2 in combinations(galaxies, 2):
            answer += abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])

        return answer

    def part_two(self) -> int:
        """part two answer"""

        lines: list[str] = []
        row_galaxy: dict[int, list[Point]] = {}
        column_galaxy: dict[int, list[Point]] = {}
        empty_row_ids: list[int] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                galaxy_found = 0

                lines.append(line)

                for idx, spot in enumerate(line):
                    if spot == "#":
                        galaxy_found += 1

                        point = Point(x=idx, y=len(lines) - 1)

                        if (len(lines) - 1) not in row_galaxy:
                            row_galaxy[len(lines) - 1] = [point]
                        else:
                            row_galaxy[len(lines) - 1].append(point)

                        if idx not in column_galaxy:
                            column_galaxy[idx] = [point]
                        else:
                            column_galaxy[idx].append(point)

                if not galaxy_found:
                    empty_row_ids.append(len(lines) - 1)

        for row_id in empty_row_ids:
            for row, galaxies in row_galaxy.items():
                if row > row_id:
                    for gal in galaxies:
                        gal.y += 999_999

        for idx in range(len(lines[0])):
            column = [line[idx] for line in lines]

            if "#" in column:
                continue

            for col, galaxies in column_galaxy.items():
                if col > idx:
                    for gal in galaxies:
                        gal.x += 999_999

        galaxies = []

        for galaxy in column_galaxy.values():
            galaxies.extend(galaxy)

        answer = 0

        for gal1, gal2 in combinations(galaxies, 2):
            answer += abs(gal1.x - gal2.x) + abs(gal1.y - gal2.y)

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
