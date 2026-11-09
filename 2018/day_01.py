"""
day_01.py

Day 1: Chronal Calibration

https://adventofcode.com/2018/day/1
"""

from itertools import cycle
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("01.txt").open("r", encoding="utf-8") as file:
            self.deltas: list[int] = [int(line.strip()) for line in file]

    def part1(self) -> int:
        """part1"""

        return sum(self.deltas)

    def part2(self) -> int:
        """part2"""

        known_freqs: set[int] = set()
        freq: int = 0

        for delta in cycle(self.deltas):
            freq += delta

            if freq in known_freqs:
                return freq
            else:
                known_freqs.add(freq)

        return -1  # should never reach here


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
