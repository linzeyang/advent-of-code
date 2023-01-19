"""
2021 Day 01
https://adventofcode.com/2021/day/1
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "01.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0
        previous = -1

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                depth = int(line)

                if previous != -1 and depth > previous:
                    answer += 1

                previous = depth

        return answer

    def part_two(self) -> int:
        """part two answer"""

        window_of_three: list[int] = []
        answer = 0
        previous = -1

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                depth = int(line)

                if len(window_of_three) >= 3:
                    window_of_three.pop(0)

                window_of_three.append(depth)

                if len(window_of_three) < 3:
                    continue

                sub = sum(window_of_three)

                if previous != -1 and sub > previous:
                    answer += 1

                previous = sub

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
