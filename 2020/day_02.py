"""
2020 Day 02
https://adventofcode.com/2020/day/2
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "02.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                instruct, sequence = line.split(": ")
                lowhigh, target = instruct.split(" ")
                low, high = lowhigh.split("-")
                low, high = int(low), int(high)

                if low <= sequence.count(target) <= high:
                    answer += 1

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                instruct, sequence = line.split(": ")
                idxs, target = instruct.split(" ")
                idx_a, idx_b = idxs.split("-")
                idx_a, idx_b = int(idx_a), int(idx_b)

                count = (sequence[idx_a - 1] == target) + (
                    sequence[idx_b - 1] == target
                )

                if count == 1:
                    answer += 1

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
