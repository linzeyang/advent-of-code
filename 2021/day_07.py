"""
day_07.py

Day 7: The Treachery of Whales

https://adventofcode.com/2021/day/7
"""

from math import ceil, floor
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    """Solution for day 7"""

    def __init__(self) -> None:
        """Initialize the solution"""

        with DATA_PATH.joinpath("07.txt").open("r", encoding="utf-8") as file:
            lines: list[str] = [line.strip() for line in file]

            self.data: tuple[int] = tuple(int(x) for x in lines[0].split(","))

    def part1(self) -> int:
        """
        Part 1 solution
        The position that minimizes the sum of absolute deviations is
        the median of all positions.
        """

        median: int = sorted(self.data)[len(self.data) // 2]

        return sum(abs(x - median) for x in self.data)

    def part2(self) -> int:
        """
        Part 2 solution
        The position that minimizes the sum of the cost of moving to each position is
        the mean of all positions rounded to the nearest integer.
        """

        mean: float = sum(self.data) / len(self.data)

        floor_mean: int = floor(mean)
        ceil_mean: int = ceil(mean)

        return min(
            sum(
                abs(x - floor_mean) * (abs(x - floor_mean) + 1) // 2 for x in self.data
            ),
            sum(abs(x - ceil_mean) * (abs(x - ceil_mean) + 1) // 2 for x in self.data),
        )


def main() -> None:
    """Run the solution and print results"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
