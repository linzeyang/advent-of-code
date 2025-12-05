"""
day_05.py

Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.ranges: list[tuple[int, ...]] = []
        self.ingredient_ids: list[int] = []

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    break

                self.ranges.append(tuple(map(int, line.split("-"))))

            for line in file:
                self.ingredient_ids.append(int(line.strip()))

        # Both parts can benefit from sorted ranges
        self.ranges.sort(key=lambda x: x[0])

    def part1(self) -> int:
        """Traverse all ingredient ids to check if they are in any range."""

        out: int = 0

        for ingredient_id in self.ingredient_ids:
            for start, end in self.ranges:
                if start <= ingredient_id <= end:
                    out += 1
                    break

        return out

    def part2(self) -> int:
        """Merge intervals to find the number of unique valid ingredient ids."""

        out: int = 0
        target: tuple[int, ...] = self.ranges[0]

        for idx in range(1, len(self.ranges)):
            start, end = self.ranges[idx]

            if start - target[1] <= 1:  # Merge overlapping or consecutive ranges
                target = target[0], max(target[1], end)
            else:
                out += target[1] - target[0] + 1
                target = start, end

        # Must add the last range
        out += target[1] - target[0] + 1

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
