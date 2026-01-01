"""
day_01.py

Day 1: The Tyranny of the Rocket Equation

https://adventofcode.com/2019/day/1
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.modules: list[int] = []

        with DATA_PATH.joinpath("01.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.modules.append(int(line.strip()))

    def part1(self) -> int:
        """part1"""

        return sum([module // 3 - 2 for module in self.modules])

    def part2(self) -> int:
        """part2"""

        out: int = 0

        for module in self.modules:
            fuel: int = module // 3 - 2

            while fuel > 0:
                out += fuel
                fuel = fuel // 3 - 2

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
