"""
day_06.py

Day 6: Custom Customs

https://adventofcode.com/2020/day/6
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.groups: list[list[str]] = []

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            group: list[str] = []

            for line in file:
                if not line.strip():
                    self.groups.append(group)
                    group = []
                else:
                    group.append(line.strip())

            if group:
                self.groups.append(group)

    def part1(self) -> int:
        """part1"""

        out = 0

        for group in self.groups:
            out += len(set("".join(group)))

        return out

    def part2(self) -> int:
        """part2"""

        out = 0

        for group in self.groups:
            out += len(set.intersection(*map(set, group)))

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
