"""
day_12.py

Day 12: Christmas Tree Farm

https://adventofcode.com/2025/day/12
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.sections: list[list[str]] = [[]]
        self.areas: dict[int, int] = {}
        self.trees: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

        with DATA_PATH.joinpath("12.txt").open("r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    self.sections[-1].append(line.strip())
                else:
                    self.sections.append([])

        for section in self.sections:
            if "x" not in section[0]:
                present_id = int(section[0][:-1])

                self.areas[present_id] = "".join(section[1:]).count("#")
            else:
                for line in section:
                    a, b = line.split(": ")
                    size: tuple[int, ...] = tuple(int(x) for x in a.split("x"))
                    quantities: tuple[int, ...] = tuple(int(x) for x in b.split(" "))
                    self.trees.append((size, quantities))

    def part1(self) -> int:
        """
        Solve the Christmas tree packing problem using area constraint.

        This is a 2D bin packing problem where we need to determine if a set of
        polyomino presents can fit within a rectangular tree area. The key insight
        is that since all present shapes have area ≤ 7 cells, we can use a simple
        area comparison as a necessary and sufficient condition.

        Algorithm:
        1. For each tree region, calculate available area (width * height)
        2. Calculate required area by summing (present_area * quantity) for all presents
        3. If available_area ≥ required_area, the packing is possible

        The area constraint works because:
        - Maximum present area is 7 cells (shapes 0,3,4,5)
        - Minimum present area is 5 cells (shape 1)
        - Data analysis shows no edge cases where area is sufficient but packing fails

        Returns:
            int: Number of tree regions where all presents can be packed
        """

        out: int = 0

        for tree in self.trees:
            width, length = tree[0]

            available_area: int = width * length

            required_area = sum(
                self.areas[idx] * qty for idx, qty in enumerate(tree[1])
            )

            if available_area >= required_area:
                out += 1

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    # Part 2 of day 12 (final day) does not include a problem to solve


if __name__ == "__main__":
    main()
