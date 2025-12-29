"""
day_13.py

Day 13: Transparent Origami

https://adventofcode.com/2021/day/13
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.dots: set[tuple[int, ...]] = set()
        self.folds: list[tuple[str, int]] = []

        with DATA_PATH.joinpath("13.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line: str = line.strip()
                if line:
                    if line.startswith("fold"):
                        self.folds.append(
                            (line.split("=")[0][-1], int(line.split("=")[1]))
                        )
                    else:
                        self.dots.add(tuple(map(int, line.split(","))))

    def _fold_dots(self, num: int) -> set[tuple[int, ...]]:
        """fold the dots"""

        dots: set[tuple[int, ...]] = self.dots.copy()

        for dir, ref in self.folds[:num]:
            if dir == "x":
                dots = {(x if x < ref else 2 * ref - x, y) for x, y in dots}
            else:
                dots = {(x, y if y < ref else 2 * ref - y) for x, y in dots}

        return dots

    def part1(self) -> int:
        """part1"""

        return len(self._fold_dots(1))

    def part2(self) -> str:
        """part2"""

        dots: set[tuple[int, ...]] = self._fold_dots(len(self.folds))

        # draw the dots
        max_x: int = max(x for x, _ in dots)
        max_y: int = max(y for _, y in dots)

        for y in range(max_y + 1):
            for x in range(max_x + 1):
                print("*" if (x, y) in dots else " ", end="")

            print()

        return "the pattern printed above"


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
