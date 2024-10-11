"""
2023 Day 06
https://adventofcode.com/2023/day/6
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "06.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 1

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            bs = [int(part) for part in file.readline().split(":")[1].strip().split()]
            cs = [int(part) for part in file.readline().split(":")[1].strip().split()]

        for b, c in zip(bs, cs):
            answer *= self.solve(b, c)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            b = int("".join(file.readline().split(":")[1].strip().split()))
            c = int("".join(file.readline().split(":")[1].strip().split()))

        answer = self.solve(b, c)

        return answer

    def solve(self, b: int, c: int) -> int:
        x1 = 0.5 * (b - (b**2 - 4 * c) ** 0.5)
        x2 = 0.5 * (b + (b**2 - 4 * c) ** 0.5)

        if x1 == int(x1):
            x1 += 1
        else:
            x1 = int(x1) + 1

        if x2 == int(x2):
            x2 -= 1
        else:
            x2 = int(x2)

        return x2 - x1 + 1

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
