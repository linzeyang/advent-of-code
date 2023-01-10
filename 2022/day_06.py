"""
2022 Day 06
https://adventofcode.com/2022/day/6
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "06.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            line = file.readline().strip()

            for i in range(len(line) - 3):
                if len(set(line[i : i + 4])) == 4:
                    answer = i + 4
                    break

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            line = file.readline().strip()

            for i in range(len(line) - 13):
                if len(set(line[i : i + 14])) == 14:
                    answer = i + 14
                    break

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
