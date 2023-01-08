"""
2022 Day 02
https://adventofcode.com/2022/day/2
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "02.txt"
    MAPPING = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    COMPETE = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("B", "X"): 0,
        ("C", "Z"): 3,
        ("C", "X"): 6,
        ("C", "Y"): 0,
    }
    MAPPING2 = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    COMPETE2 = {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("B", "X"): 1,
        ("C", "Z"): 1,
        ("C", "X"): 2,
        ("C", "Y"): 3,
    }

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                opponent, mine = line.split()
                answer += (
                    self.MAPPING[mine] + self.COMPETE[(opponent, mine)]  # type: ignore
                )

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                opponent, mine = line.split()
                answer += (
                    self.MAPPING2[mine]
                    + self.COMPETE2[(opponent, mine)]  # type: ignore
                )

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
