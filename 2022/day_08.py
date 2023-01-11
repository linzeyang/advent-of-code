"""
2022 Day 08
https://adventofcode.com/2022/day/8
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "08.txt"

    def __init__(self) -> None:
        self.matrix: list[list[int]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            for line in file:
                self.matrix.append([int(char) for char in line.strip()])

        self.x_coord = len(self.matrix[0])
        self.y_coord = len(self.matrix)

    def part_one(self) -> int:
        """part one answer"""

        answer = 2 * (self.x_coord + self.y_coord) - 4

        for i in range(1, self.x_coord - 1):
            for j in range(1, self.y_coord - 1):
                left = self.matrix[i][:j]
                right = self.matrix[i][j + 1 :]
                up = [self.matrix[k][j] for k in range(i)]
                down = [self.matrix[k][j] for k in range(i + 1, self.x_coord)]

                if (
                    (val := self.matrix[i][j]) > max(left)
                    or val > max(right)
                    or val > max(up)
                    or val > max(down)
                ):
                    answer += 1

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        for i in range(1, self.x_coord - 1):
            for j in range(1, self.y_coord - 1):
                left = self.matrix[i][j - 1 :: -1]
                right = self.matrix[i][j + 1 :]
                up = [self.matrix[k][j] for k in range(i - 1, -1, -1)]
                down = [self.matrix[k][j] for k in range(i + 1, self.x_coord)]

                val = self.matrix[i][j]
                score = 1

                for sec in (left, right, up, down):
                    sub = 0
                    for elem in sec:
                        sub += 1
                        if elem >= val:
                            break
                    score *= sub

                if score > answer:
                    answer = score

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
