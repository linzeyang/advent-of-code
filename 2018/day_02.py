"""
day_02.py

Day 2: Inventory Management System

https://adventofcode.com/2018/day/2
"""

from collections import Counter
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("02.txt").open("r", encoding="utf-8") as file:
            self.ids: list[str] = [line.strip() for line in file]

    def part1(self) -> int:
        """part1"""

        num_of_two_appearances: int = 0
        num_of_three_appearances: int = 0

        for _id in self.ids:
            counter: Counter[str] = Counter(_id)

            if 2 in counter.values():
                num_of_two_appearances += 1
            if 3 in counter.values():
                num_of_three_appearances += 1

        return num_of_two_appearances * num_of_three_appearances

    def part2(self) -> str:
        """part2"""

        for idx in range(len(self.ids) - 1):
            _id: str = self.ids[idx]

            for jdx in range(idx + 1, len(self.ids)):
                _jd: str = self.ids[jdx]

                num_of_diffs: int = 0

                for kdx in range(len(_id)):
                    if _id[kdx] != _jd[kdx]:
                        num_of_diffs += 1

                        if num_of_diffs > 1:
                            break
                else:
                    return "".join(
                        char
                        for char, char2 in zip(_id, _jd, strict=True)
                        if char == char2
                    )

        return ""


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
