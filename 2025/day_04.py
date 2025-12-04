"""
day_04.py

Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.grid: list[list[str]] = []

        with DATA_PATH.joinpath("04.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.grid.append(list(line.strip()))

    def part1(self) -> int:
        """part1"""

        out: int = 0

        for jdx, row in enumerate(self.grid):
            for idx, char in enumerate(row):
                if char == ".":
                    continue
                if self._can_fork(idx, jdx):
                    out += 1

        return out

    def _can_fork(self, idx: int, jdx: int) -> bool:
        """check if the cell can fork"""

        adjacent_coordinates: tuple[tuple[int, int], ...] = (
            (idx - 1, jdx - 1),
            (idx, jdx - 1),
            (idx + 1, jdx - 1),
            (idx - 1, jdx),
            (idx + 1, jdx),
            (idx - 1, jdx + 1),
            (idx, jdx + 1),
            (idx + 1, jdx + 1),
        )

        out: int = 0

        for x, y in adjacent_coordinates:
            if (
                0 <= x < len(self.grid[0])
                and 0 <= y < len(self.grid)
                and self.grid[y][x] == "@"
            ):
                out += 1

        return out < 4

    def part2(self) -> int:
        """part2"""

        total: int = 0

        while True:
            single_round: int = 0

            for jdx, row in enumerate(self.grid):
                for idx, char in enumerate(row):
                    if char == ".":
                        continue
                    if self._can_fork(idx, jdx):
                        self.grid[jdx][idx] = "."
                        single_round += 1

            if not single_round:
                break

            total += single_round

        return total


def main() -> None:
    """main"""

    print(f"Answer for part 1 is {Solution().part1()}")
    print(f"Answer for part 2 is {Solution().part2()}")


if __name__ == "__main__":
    main()
