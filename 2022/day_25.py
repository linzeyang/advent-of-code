"""
2022 Day 25
https://adventofcode.com/2022/day/25
"""

from pathlib import Path


def snafu_to_decimal(snafu: str) -> int:
    """Convert SNFAU string to decimal number.

    Eg. 1=11-2 -> 2022

    Args:
        snafu (str): SNAFU string

    Returns:
        int: equivalent decimal number
    """
    out = base = 0

    for char in reversed(snafu):
        if char == "-":
            digit = -1
        elif char == "=":
            digit = -2
        else:
            digit = int(char)

        out += digit * 5**base
        base += 1

    return out


def decimal_to_snafu(decimal: int) -> str:
    """Convert decimal number to SNAFU representation.

    Eg. 2022 -> 1=11-2

    Args:
        decimal (int): decimal number

    Returns:
        str: equivalent SNAFU string
    """
    if decimal < 3:
        return str(decimal)

    out = []

    while decimal > 0:
        quotient, remainder = divmod(decimal, 5)

        if remainder in {0, 1, 2}:
            out.append(str(remainder))
        elif remainder == 3:
            out.append("=")
            quotient += 1
        else:
            out.append("-")
            quotient += 1

        decimal = quotient

    return "".join(reversed(out))


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "25.txt"

    def part_one(self) -> str:
        """part one answer"""

        count = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                count += snafu_to_decimal(line)

        return decimal_to_snafu(count)

    def part_two(self) -> None:
        """part two answer"""

        # There is no puzzle in part two

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
