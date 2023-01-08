"""
2022 Day 01
https://adventofcode.com/2022/day/1
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "01.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = sub_total = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    if sub_total > answer:
                        answer = sub_total
                    sub_total = 0
                else:
                    sub_total += int(line)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        top_3: list[int] = []
        sub_total = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    if len(top_3) < 3:
                        top_3.append(sub_total)
                    elif sub_total > min(top_3):
                        top_3.remove(min(top_3))
                        top_3.append(sub_total)
                    sub_total = 0
                else:
                    sub_total += int(line)

        return sum(top_3)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
