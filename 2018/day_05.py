"""
day_05.py

Day 5: Alchemical Reduction

https://adventofcode.com/2018/day/5
"""

from pathlib import Path
from string import ascii_lowercase

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            self.polymer: list[str] = list(file.readline().strip())

    def part1(self) -> int:
        """part1"""

        stack: list[str] = []

        for unit in self.polymer:
            if (
                not stack
                or (unit.islower() and unit.upper() != stack[-1])
                or (unit.isupper() and unit.lower() != stack[-1])
            ):
                stack.append(unit)
            else:
                stack.pop()

        return len(stack)

    def part2(self) -> int:
        """part2"""

        min_length: int = len(self.polymer)

        for letter in ascii_lowercase:
            stack: list[str] = []

            for unit in self.polymer:
                if unit.lower() == letter:
                    continue

                if (
                    not stack
                    or (unit.islower() and unit.upper() != stack[-1])
                    or (unit.isupper() and unit.lower() != stack[-1])
                ):
                    stack.append(unit)
                else:
                    stack.pop()

            min_length = min(min_length, len(stack))

        return min_length


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
