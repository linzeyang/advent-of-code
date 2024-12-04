"""
day_02.py

Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.reports: list[list[int]] = []

        with DATA_PATH.joinpath("02.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.reports.append([int(number) for number in line.strip().split()])

    def part1(self) -> int:
        """part1"""

        num_of_safe_reports = 0

        for report in self.reports:
            diff = report[1] - report[0]

            if abs(diff) < 1 or abs(diff) > 3:
                continue

            increasing: bool = diff > 0

            for idx in range(2, len(report)):
                diff = report[idx] - report[idx - 1]

                if (increasing and (diff < 1 or diff > 3)) or (
                    not increasing and (diff < -3 or diff > -1)
                ):
                    break
            else:
                num_of_safe_reports += 1

        return num_of_safe_reports

    def part2(self) -> int:
        """part2"""

        num_of_safe_reports = 0

        ...  # TODO

        return num_of_safe_reports


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
