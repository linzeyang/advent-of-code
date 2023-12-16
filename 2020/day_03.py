"""
2020 Day 03
https://adventofcode.com/2020/day/3
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "03.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            line = file.readline().strip()

            width = len(line)
            idx = 3

            while line := file.readline().strip():
                idx %= width
                if line[idx] == "#":
                    answer += 1
                idx += 3

        return answer

    def part_two(self) -> int:
        """part two answer"""

        bases = [1, 3, 5, 7, 1]
        idxs = [1, 3, 5, 7, 1]
        answers = [0, 0, 0, 0, 0]

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            line = file.readline().strip()

            width = len(line)

            row_no = 1

            while line := file.readline().strip():
                row_no += 1

                for jdx in range(4):
                    idx = idxs[jdx] % width

                    if line[idx] == "#":
                        answers[jdx] += 1

                    idxs[jdx] = idx + bases[jdx]

                if row_no % 2:
                    kdx = idxs[4] % width

                    if line[kdx] == "#":
                        answers[4] += 1

                    idxs[4] = kdx + bases[4]

        answer = answers[0] * answers[1] * answers[2] * answers[3] * answers[4]

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
