"""
day_10.py

Day 10: Adapter Array

https://adventofcode.com/2020/day/10
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.adapters: list[int] = [0]

        with DATA_PATH.joinpath("10.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.adapters.append(int(line.strip()))

        self.adapters.sort()
        self.adapters.append(self.adapters[-1] + 3)

    def part1(self) -> int:
        """part1"""

        num_diff_1 = num_diff_3 = 0

        for idx in range(1, len(self.adapters)):
            diff = self.adapters[idx] - self.adapters[idx - 1]

            if diff == 1:
                num_diff_1 += 1
            elif diff == 3:
                num_diff_3 += 1

        return num_diff_1 * num_diff_3

    def part2(self) -> int:
        """part2"""

        # let's try backtracking
        num_ways: list[int] = [0] * len(self.adapters)

        num_ways[-1] = 1

        for idx in range(2, len(num_ways) + 1):
            val = self.adapters[-idx]

            for diff in range(1, 4):
                if -idx + diff >= len(num_ways):
                    break

                if self.adapters[-idx + diff] - val <= 3:
                    num_ways[-idx] += num_ways[-idx + diff]

        return num_ways[0]


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
