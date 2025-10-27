"""
day_02.py

Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.reports: list[list[int]] = []

        with DATA_PATH.joinpath("02.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.reports.append([int(number) for number in line.strip().split()])

    def part1(self) -> int:
        """part1"""

        return sum(1 for report in self.reports if self._is_safe_report(report))

    def _is_safe_report(self, report: list[int]) -> bool:
        """Check if a single report is safe"""

        if len(report) < 2:
            return True

        # Check if all differences are in valid range
        diffs: list[int] = [report[i] - report[i - 1] for i in range(1, len(report))]

        # All differences must be between -3 and -1 (decreasing)
        # OR between 1 and 3 (increasing)
        if not all((-3 <= diff <= -1 or 1 <= diff <= 3) for diff in diffs):
            return False

        # Check if all increasing or all decreasing
        increasing = all(diff > 0 for diff in diffs)
        decreasing = all(diff < 0 for diff in diffs)

        return increasing or decreasing

    def part2(self) -> int:
        """part2"""

        num_of_safe_reports: int = 0

        for report in self.reports:
            # First check if the report is already safe
            if self._is_safe_report(report):
                num_of_safe_reports += 1
                continue

            # If not safe, try removing each level one at a time
            for i in range(len(report)):
                # Create a new report with the i-th level removed
                modified_report: list[int] = report[:i] + report[i + 1 :]

                if self._is_safe_report(modified_report):
                    num_of_safe_reports += 1
                    break  # Only need to find one valid removal

        return num_of_safe_reports


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
