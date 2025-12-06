"""
day_06.py

Day 06: Trash Compactor

https://adventofcode.com/2025/day/6
"""

import math
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rows: list[list[int]] = []
        self.raw_rows: list[str] = []

        self.operators: list[str] = []
        self.raw_operators: str = ""

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            for line in file:
                if line[0].isdigit() or line[0] == " ":
                    self.rows.append([int(x) for x in line.split()])
                    self.raw_rows.append(line.rstrip("\n"))
                else:
                    self.operators = line.strip().split()
                    self.raw_operators = line.rstrip("\n")

    def part1(self) -> int:
        """part1"""

        out: int = 0

        for idx, operator in enumerate(self.operators):
            match operator:
                case "*":
                    out += math.prod(self.rows[_][idx] for _ in range(len(self.rows)))
                case "+":
                    out += sum(self.rows[_][idx] for _ in range(len(self.rows)))

        return out

    def part2(self) -> int:
        """part2"""

        out: int = 0

        current: int = 0
        operator: str = ""

        for idx in range(len(self.raw_operators)):
            if self.raw_operators[idx] != " ":
                out += current
                operator: str = self.raw_operators[idx]

                if operator == "*":
                    current = 1
                else:
                    current = 0

            digits: list[str] = []

            for _ in range(len(self.raw_rows)):
                char = self.raw_rows[_][idx]

                if char.isdigit():
                    digits.append(char)

            if not digits:
                continue

            if operator == "*":
                current *= int("".join(digits))
            else:
                current += int("".join(digits))

        out += current

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
