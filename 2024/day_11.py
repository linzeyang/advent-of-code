"""
day_11.py

Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11
"""

from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """Initialize the solution with input data."""

        with DATA_PATH.joinpath("11.txt").open("r", encoding="utf-8") as file:
            self.stones: list[int] = [int(x) for x in file.read().strip().split()]

    # NO need to maintain the actual sequence of stones - we just need to count
    # how many stones each initial stone becomes after a given number of blinks.

    @lru_cache(maxsize=None)  # noqa: B019
    def _count_stones_after_blinks(self, stone: int, blinks: int) -> int:
        """
        Count how many stones a single stone becomes after a given number of blinks.
        Uses memoization (LRU cache) to avoid recalculating the same transformations.
        """

        if blinks == 0:
            return 1

        # Rule 1: If stone is 0, it becomes 1
        if stone == 0:
            return self._count_stones_after_blinks(1, blinks - 1)

        # Rule 2: If stone has even number of digits, split it
        if len(stone_str := str(stone)) % 2 == 0:
            mid: int = len(stone_str) // 2
            left: int = int(stone_str[:mid])
            right: int = int(stone_str[mid:])

            return self._count_stones_after_blinks(
                left, blinks - 1
            ) + self._count_stones_after_blinks(right, blinks - 1)

        # Rule 3: Otherwise, multiply by 2024
        return self._count_stones_after_blinks(stone * 2024, blinks - 1)

    def part1(self) -> int:
        """Solve part 1: count stones after 25 blinks."""

        return sum(self._count_stones_after_blinks(stone, 25) for stone in self.stones)

    def part2(self) -> int:
        """Solve part 2: count stones after 75 blinks."""

        return sum(self._count_stones_after_blinks(stone, 75) for stone in self.stones)


def main() -> None:
    """Main function to run the solution"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
