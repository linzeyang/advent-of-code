"""
day_05.py

Day 5: Binary Boarding

https://adventofcode.com/2020/day/5
"""

from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.passes: list[str] = []

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.passes.append(line.strip())

    def part1(self) -> int:
        """part1"""

        out = 0

        for passcode in self.passes:
            row_code, column_code = passcode[:7], passcode[7:]

            row = self._calc_row(row_code)
            column = self._calc_column(column_code)

            seat_id = row * 8 + column

            if seat_id > out:
                out = seat_id

        return out

    @lru_cache(maxsize=128)  # noqa: B019
    def _calc_row(self, row_code: str) -> int:
        """get the row number of the seat"""

        low, high = 0, 127

        for char in row_code:
            match char:
                case "F":
                    high = (low + high) // 2
                case "B":
                    low = (low + high) // 2 + 1

        return low

    @lru_cache(maxsize=8)  # noqa: B019
    def _calc_column(self, column_code: str) -> int:
        """get the column number of the seat"""

        low, high = 0, 7

        for char in column_code:
            match char:
                case "L":
                    high = (low + high) // 2
                case "R":
                    low = (low + high) // 2 + 1

        return low

    def part2(self) -> int:
        """part2"""

        row_to_column_sum: dict[int, int] = {}

        for passcode in self.passes:
            row_code, column_code = passcode[:7], passcode[7:]

            row = self._calc_row(row_code)
            column = self._calc_column(column_code)

            if row in {0, 127}:
                continue

            if row not in row_to_column_sum:
                row_to_column_sum[row] = column
            else:
                row_to_column_sum[row] += column

        for row, column_sum in row_to_column_sum.items():
            if column_sum != 28:  # 28 = 0 + 1 + 2 + ... + 7
                column = 28 - column_sum

                return row * 8 + column

        return -1


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
