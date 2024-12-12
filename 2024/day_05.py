"""
day_05.py

Day 5: Print Queue

https://adventofcode.com/2024/day/5
"""

from collections import defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rules: dict[str, list[str]] = defaultdict(list)
        self.updates: list[list[str]] = []

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            for line in file:
                if "|" in line:
                    left, right = line.strip().split("|")

                    self.rules[right].append(left)
                elif "," in line:
                    self.updates.append(line.strip().split(","))

    def part1(self) -> int:
        """part1"""

        out = 0

        for pages in self.updates:
            if self._validate(pages):
                out += int(pages[len(pages) // 2])

        return out

    def _validate(self, pages: list[str]) -> bool:
        """validate the order of pages"""

        examined: set[str] = set()
        not_examined: set[str] = set(pages)

        for page in pages:
            if page in self.rules:
                for rule in self.rules[page]:
                    if rule in not_examined:
                        return False

            examined.add(page)
            not_examined.remove(page)

        return True

    def part2(self) -> int:
        """part2"""

        out = 0

        for pages in self.updates:
            if self._validate(pages):
                continue

            pages = self._reorder(pages)

            while not self._validate(pages):
                pages = self._reorder(pages)

            out += int(pages[len(pages) // 2])

        return out

    def _reorder(self, pages: list[str]) -> list[str]:
        """reorder"""

        left: list[str] = []
        right: set[str] = set(pages)

        for page in pages:
            if page not in self.rules:
                continue

            for rule in self.rules[page]:
                if rule in right:
                    left.append(rule)
                    right.remove(rule)

            if page in right:
                left.append(page)
                right.remove(page)

        return left + list(right)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
