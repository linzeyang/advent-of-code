"""
2023 Day 01
https://adventofcode.com/2023/day/1
"""

from pathlib import Path

MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "01.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    break

                digits = [int(char) for char in line if char.isdigit()]

                if len(digits) == 1:
                    answer += digits[0] * 11
                else:
                    answer += digits[0] * 10 + digits[-1]

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    break

                first_digit = last_digit = 0

                idx = 0

                while idx < len(line):
                    if line[idx].isdigit():
                        first_digit = int(line[idx])
                        break

                    if line[idx] not in "otsfne":
                        idx += 1
                        continue

                    if line[idx : idx + 3] in {"one", "two", "six"}:
                        first_digit = int(MAPPING[line[idx : idx + 3]])
                        break

                    if line[idx : idx + 4] in {"four", "five", "nine"}:
                        first_digit = int(MAPPING[line[idx : idx + 4]])
                        break

                    if line[idx : idx + 5] in {"three", "seven", "eight"}:
                        first_digit = int(MAPPING[line[idx : idx + 5]])
                        break

                    idx += 1

                idx = len(line) - 1

                while idx >= 0:
                    if line[idx].isdigit():
                        last_digit = int(line[idx])
                        break

                    if line[idx] not in "eoxrnt":
                        idx -= 1
                        continue

                    if line[idx - 2 : idx + 1] in {"one", "two", "six"}:
                        last_digit = int(MAPPING[line[idx - 2 : idx + 1]])
                        break

                    if line[idx - 3 : idx + 1] in {"four", "five", "nine"}:
                        last_digit = int(MAPPING[line[idx - 3 : idx + 1]])
                        break

                    if line[idx - 4 : idx + 1] in {"three", "seven", "eight"}:
                        last_digit = int(MAPPING[line[idx - 4 : idx + 1]])
                        break

                    idx -= 1

                answer += first_digit * 10 + last_digit

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
