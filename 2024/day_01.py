"""
day_01.py

Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""

from collections import Counter
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.list1: list[int] = []
        self.list2: list[int] = []

        with DATA_PATH.joinpath("01.txt").open("r", encoding="utf-8") as file:
            for line in file:
                number1, number2 = line.strip().split()

                self.list1.append(int(number1))
                self.list2.append(int(number2))

    def part1(self) -> int:
        """part1"""

        return sum(
            abs(num1 - num2)
            for num1, num2 in zip(sorted(self.list1), sorted(self.list2), strict=True)
        )

    def part2(self) -> int:
        """part2"""

        counter = Counter(self.list2)

        return sum(num * counter.get(num, 0) for num in self.list1)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
