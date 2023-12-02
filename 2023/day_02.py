"""
2023 Day 02
https://adventofcode.com/2023/day/2
"""

from pathlib import Path

MAPPING = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "02.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                header, content = line.split(": ")

                valid = True

                for draw in content.split("; "):
                    for count_color in draw.split(", "):
                        count, color = count_color.split(" ")

                        if MAPPING[color] < int(count):
                            valid = False
                            break

                    if not valid:
                        break

                if valid:
                    answer += int(header.split(" ")[1])

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                mapping = {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                }

                _, content = line.split(": ")

                for draw in content.split("; "):
                    for count_color in draw.split(", "):
                        count, color = count_color.split(" ")

                        if mapping[color] < int(count):
                            mapping[color] = int(count)

                answer += mapping["red"] * mapping["green"] * mapping["blue"]

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
