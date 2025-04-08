"""
day_05.py

Day 05: Hydrothermal Venture

https://adventofcode.com/2021/day/5
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.lines: list[tuple[int, int, int, int]] = []

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                left, right = line.split(" -> ")

                x1, y1 = left.split(",")
                x2, y2 = right.split(",")

                self.lines.append((int(x1), int(y1), int(x2), int(y2)))

    def part1(self) -> int:
        """part1"""

        coordinate_counter: dict[tuple[int, int], int] = {}

        for x1, y1, x2, y2 in self.lines:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    coordinate_counter[(x1, y)] = coordinate_counter.get((x1, y), 0) + 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    coordinate_counter[(x, y1)] = coordinate_counter.get((x, y1), 0) + 1

        return len([v for v in coordinate_counter.values() if v > 1])

    def part2(self) -> int:
        """part2"""

        coordinate_counter: dict[tuple[int, int], int] = {}

        for x1, y1, x2, y2 in self.lines:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    coordinate_counter[(x1, y)] = coordinate_counter.get((x1, y), 0) + 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    coordinate_counter[(x, y1)] = coordinate_counter.get((x, y1), 0) + 1
            else:
                dx = 1 if x1 < x2 else -1
                dy = 1 if y1 < y2 else -1

                for x, y in zip(
                    range(x1, x2 + dx, dx), range(y1, y2 + dy, dy), strict=True
                ):
                    coordinate_counter[(x, y)] = coordinate_counter.get((x, y), 0) + 1

        return len([v for v in coordinate_counter.values() if v > 1])


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
