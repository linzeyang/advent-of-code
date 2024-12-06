"""
day_03.py

Day 3: Mull It Over

https://adventofcode.com/2024/day/3
"""

import re
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.lines: list[str] = []

        with DATA_PATH.joinpath("03.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.lines.append(line)

    def part1(self) -> int:
        """part1"""

        pattern = re.compile(r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)")

        out = 0

        for line in self.lines:
            for match in re.finditer(pattern, line.strip()):
                group = match.groupdict()

                out += int(group["num1"]) * int(group["num2"])

        return out

    def part2(self) -> int:
        """part2"""

        pattern = re.compile(
            r"(mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\))|(don\'t\(\))|(do\(\))"
        )

        out = 0

        enabled = True

        for line in self.lines:
            for match in re.finditer(pattern, line.strip()):
                if match.group().startswith("don't"):  # don't() found
                    enabled = False
                elif match.group().startswith("do"):  # do() found
                    enabled = True
                elif enabled:  # mul(?,?) found, and enabled is True
                    group_dict = match.groupdict()

                    out += int(group_dict["num1"]) * int(group_dict["num2"])

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
