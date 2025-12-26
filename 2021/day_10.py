"""
day_10.py

Day 10: Syntax Scoring

https://adventofcode.com/2021/day/10
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"

OPENNING: dict[str, str] = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CLOSING: dict[str, str] = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rows: list[str] = []

        with DATA_PATH.joinpath("10.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.rows.append(line.strip())

    def part1(self) -> int:
        """part1"""

        SCORES: dict[str, int] = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }

        out: int = 0

        def process_row(row: str) -> str:
            stack: list[str] = []

            for char in row:
                if char in OPENNING:
                    stack.append(char)
                elif stack and stack[-1] == CLOSING[char]:
                    stack.pop()
                else:
                    return char

            return ""

        for row in self.rows:
            out += SCORES.get(process_row(row), 0)

        return out

    def part2(self) -> int:
        """part2"""

        SCORES: dict[str, int] = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }

        line_scores: list[int] = []

        def process_row(row: str) -> int:
            stack: list[str] = []

            for char in row:
                if char in OPENNING:
                    stack.append(char)
                elif stack and stack[-1] == CLOSING[char]:
                    stack.pop()
                else:
                    return 0

            out: int = 0

            for char in stack[::-1]:
                out = out * 5 + SCORES[OPENNING[char]]

            return out

        for row in self.rows:
            if (line_score := process_row(row)) > 0:
                line_scores.append(line_score)

        line_scores.sort()

        return line_scores[len(line_scores) // 2]


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
