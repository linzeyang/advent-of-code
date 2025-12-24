"""
day_09.py

Day 9: Smoke Basin

https://adventofcode.com/2021/day/9
"""

import heapq
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rows: list[list[int]] = []

        with DATA_PATH.joinpath("09.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.rows.append([int(char) for char in line.strip()])

        self.low_points: list[tuple[int, int]] = []

    def part1(self) -> int:
        """part1"""

        out: int = 0

        for idx, row in enumerate(self.rows):
            for jdx, height in enumerate(row):
                up: int = self.rows[idx - 1][jdx] if idx > 0 else 10
                down: int = self.rows[idx + 1][jdx] if idx < len(self.rows) - 1 else 10
                left: int = self.rows[idx][jdx - 1] if jdx > 0 else 10
                right: int = self.rows[idx][jdx + 1] if jdx < len(row) - 1 else 10

                if height < up and height < down and height < left and height < right:
                    out += height + 1
                    self.low_points.append((idx, jdx))

        return out

    def part2(self) -> int:
        """
        For each low point, find the basin area.

        The basin area is the number of points in the basin.

        Keep track of the top 3 largest basin areas.

        Return the product of the top 3 largest basin areas.
        """

        top_three_area: list[int] = []
        heapq.heapify(top_three_area)

        for point in self.low_points:
            if len(top_three_area) < 3:
                heapq.heappush(top_three_area, self._find_basin_area(point))
            else:
                heapq.heappushpop(top_three_area, self._find_basin_area(point))

        return top_three_area[0] * top_three_area[1] * top_three_area[2]

    def _find_basin_area(self, point: tuple[int, int]) -> int:
        """
        Get the area of a "basin" starting from a low point.

        A basin is all locations that eventually flow downward to a single low point.

        Maintain a stack of points to visit. For every visited point, flood-fill it
        with 9 to avoid revisiting.

        The area is the number of visited points.
        """

        out: int = 0
        stack: list[tuple[int, int]] = [point]

        while stack:
            idx, jdx = stack.pop()

            if self.rows[idx][jdx] == 9:
                continue

            self.rows[idx][jdx] = 9
            out += 1

            if idx > 0:
                stack.append((idx - 1, jdx))
            if idx < len(self.rows) - 1:
                stack.append((idx + 1, jdx))
            if jdx > 0:
                stack.append((idx, jdx - 1))
            if jdx < len(self.rows[idx]) - 1:
                stack.append((idx, jdx + 1))

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
