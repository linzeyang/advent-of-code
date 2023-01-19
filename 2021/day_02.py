"""
2021 Day 02
https://adventofcode.com/2021/day/2
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "02.txt"

    def part_one(self) -> int:
        """part one answer"""

        x_coord = y_coord = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                command, arg = line.split()

                if command == "forward":
                    x_coord += int(arg)
                elif command == "down":
                    y_coord += int(arg)
                else:
                    y_coord -= int(arg)

        return x_coord * y_coord

    def part_two(self) -> int:
        """part two answer"""

        x_coord = y_coord = aim = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                command, arg = line.split()

                if command == "forward":
                    x_coord += int(arg)
                    y_coord += aim * int(arg)
                elif command == "down":
                    aim += int(arg)
                else:
                    aim -= int(arg)

        return x_coord * y_coord

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
