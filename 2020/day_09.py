"""
day_09.py

Day 9: Encoding Error

https://adventofcode.com/2020/day/9
"""

from collections import deque
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.numbers: list[int] = []

        with DATA_PATH.joinpath("09.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.numbers.append(int(line.strip()))

    def part1(self) -> int:
        """part1"""

        candidates = deque(self.numbers[:25])

        for idx in range(25, len(self.numbers)):
            target = self.numbers[idx]

            if not any(target - num in candidates for num in candidates):
                break

            candidates.popleft()
            candidates.append(target)

        return target

    def part2(self) -> int:
        """part2"""

        # 683 is the index of the first invalid number from part 1
        IDX = 683
        TARGET = self.numbers[IDX]

        left, right = 0, 1
        summ = self.numbers[left] + self.numbers[right]

        while summ != TARGET:
            if summ < TARGET:
                right += 1
                summ += self.numbers[right]
            else:
                summ -= self.numbers[left]
                left += 1

        section = self.numbers[left : right + 1]

        return min(section) + max(section)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
