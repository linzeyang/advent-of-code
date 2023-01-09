"""
2022 Day 03
https://adventofcode.com/2022/day/3
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "03.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                half = len(line) // 2
                common = set(line[:half]).intersection(set(line[half:]))

                if (char := common.pop()).isupper():
                    value = ord(char) - ord("A") + 27
                else:
                    value = ord(char) - ord("a") + 1

                answer += value

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            temp = []

            while line := file.readline().strip():
                if len(temp) < 3:
                    temp.append(line)
                    continue

                common = (
                    set(temp[0]).intersection(set(temp[1])).intersection(set(temp[2]))
                )

                if (char := common.pop()).isupper():
                    value = ord(char) - ord("A") + 27
                else:
                    value = ord(char) - ord("a") + 1

                answer += value
                temp = [line]

            common = set(temp[0]).intersection(set(temp[1])).intersection(set(temp[2]))

            if (char := common.pop()).isupper():
                value = ord(char) - ord("A") + 27
            else:
                value = ord(char) - ord("a") + 1

            answer += value

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
