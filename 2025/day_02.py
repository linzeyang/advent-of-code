"""
day_02.py

Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """Initialize the solution by parsing the input ranges."""

        self.ranges: list[tuple[int, ...]] = []

        with DATA_PATH.joinpath("02.txt").open("r", encoding="utf-8") as file:
            # Input format: "11-22,95-115,..."
            for segment in file.readline().split(","):
                self.ranges.append(tuple(int(x) for x in segment.split("-")))

    def part1(self) -> int:
        """
        Calculate the sum of invalid IDs for Part 1.
        An ID is invalid if it consists of a digit sequence repeated exactly twice.
        Example: 123123 (invalid), 1212 (invalid), 12345 (valid).
        """

        out: int = 0

        for start, end in self.ranges:
            for num in range(start, end + 1):
                if self._is_invalid_1(num):
                    out += num

        return out

    def _is_invalid_1(self, num: int) -> bool:
        """Check if a number is invalid (repeated exactly twice)."""

        num_str: str = str(num)
        length: int = len(num_str)

        # Must have even length to be split into two equal halves
        if length % 2:
            return False

        return num_str[: length // 2] == num_str[length // 2 :]

    def part2(self) -> int:
        """
        Calculate the sum of invalid IDs for Part 2.
        An ID is invalid if it consists of a digit sequence repeated AT LEAST twice.
        Example: 123123 (invalid), 111 (invalid), 121212 (invalid).
        """

        out: int = 0

        for start, end in self.ranges:
            for num in range(start, end + 1):
                if self._is_invalid_2(num):
                    out += num

        return out

    def _is_invalid_2(self, num: int) -> bool:
        """Check if a number is invalid for Part 2 rules (repeated at least twice)."""

        if num <= 10:
            return False

        num_str: str = str(num)
        half_length: int = len(num_str) // 2

        # Try all possible sub-sequence lengths
        for delta in range(1, half_length + 1):
            # If total length is not a multiple of sub-sequence length, it's impossible
            if len(num_str) % delta:
                continue

            # Split the number string into chunks of size 'delta'
            parts: tuple[str, ...] = tuple(
                num_str[i : i + delta] for i in range(0, len(num_str), delta)
            )

            # Check if all chunks are identical
            if all(parts[j] == parts[0] for j in range(1, len(parts))):
                return True

        return False


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
