"""
day_09.py

Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.points: list[tuple[int, ...]] = []

        with DATA_PATH.joinpath("09.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.points.append(tuple(map(int, line.split(","))))

    def part1(self) -> int:
        """part1"""

        out: int = 2
        length: int = len(self.points)

        # brute force: total number of points < 500
        for idx in range(length - 1):
            for jdx in range(idx + 1, length):
                out = max(
                    out,
                    (abs(self.points[idx][0] - self.points[jdx][0]) + 1)
                    * (abs(self.points[idx][1] - self.points[jdx][1]) + 1),
                )

        return out

    def part2(self) -> int:
        """part2"""

        return -1


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
