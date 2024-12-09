"""
day_04.py

Day 4: Ceres Search

https://adventofcode.com/2024/day/4
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.matrix: list[str] = []

        with DATA_PATH.joinpath("04.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.matrix.append(line.strip())

        self.x_len = len(self.matrix[0])
        self.y_len = len(self.matrix)

    def part1(self) -> int:
        """part1"""

        out = 0

        for idx in range(self.y_len):
            for jdx in range(self.x_len):
                if self.matrix[idx][jdx] != "X":
                    continue

                out += self._find_xmas(idx, jdx)

        return out

    def _find_xmas(self, idx: int, jdx: int) -> int:
        """Find the number of XMAS"""

        coordinates: list[tuple[tuple[int, int], ...]] = [
            ((idx, jdx), (idx - 1, jdx), (idx - 2, jdx), (idx - 3, jdx)),  # bottom up
            (
                (idx, jdx),
                (idx - 1, jdx + 1),
                (idx - 2, jdx + 2),
                (idx - 3, jdx + 3),
            ),  # up right
            (
                (idx, jdx),
                (idx, jdx + 1),
                (idx, jdx + 2),
                (idx, jdx + 3),
            ),  # left to right
            (
                (idx, jdx),
                (idx + 1, jdx + 1),
                (idx + 2, jdx + 2),
                (idx + 3, jdx + 3),
            ),  # down right
            ((idx, jdx), (idx + 1, jdx), (idx + 2, jdx), (idx + 3, jdx)),  # upside down
            (
                (idx, jdx),
                (idx + 1, jdx - 1),
                (idx + 2, jdx - 2),
                (idx + 3, jdx - 3),
            ),  # down left
            (
                (idx, jdx),
                (idx, jdx - 1),
                (idx, jdx - 2),
                (idx, jdx - 3),
            ),  # right to left
            (
                (idx, jdx),
                (idx - 1, jdx - 1),
                (idx - 2, jdx - 2),
                (idx - 3, jdx - 3),
            ),  # up left
        ]

        return sum(1 for coordinate in coordinates if self._validate_1(coordinate))

    def _validate_1(self, coordinate: tuple[tuple[int, int], ...]) -> bool:
        """validate for part 1"""

        for coord_i, coord_j in coordinate:
            if not (0 <= coord_i < self.y_len) or not (0 <= coord_j < self.x_len):
                return False

        return (
            "".join(self.matrix[coord_i][coord_j] for coord_i, coord_j in coordinate)
            == "XMAS"
        )

    def part2(self) -> int:
        """part2"""

        out = 0

        for idx in range(1, self.y_len - 1):
            for jdx in range(1, self.x_len - 1):
                if self.matrix[idx][jdx] != "A":
                    continue

                out += self._find_x_mas(idx, jdx)

        return out

    def _find_x_mas(self, idx: int, jdx: int) -> int:
        """Find the number of X-MAS"""

        coordinates: list[tuple[tuple[int, int], ...]] = [
            (
                (idx - 1, jdx - 1),
                (idx, jdx),
                (idx + 1, jdx + 1),
            ),  # up left to down right
            (
                (idx - 1, jdx + 1),
                (idx, jdx),
                (idx + 1, jdx - 1),
            ),  # down left to up right
        ]

        return (
            1
            if self._validate_2(coordinates[0]) and self._validate_2(coordinates[1])
            else 0
        )

    def _validate_2(self, coordinate: tuple[tuple[int, int], ...]) -> bool:
        """validate for part 2"""

        return "".join(
            self.matrix[coord_i][coord_j] for coord_i, coord_j in coordinate
        ) in ("MAS", "SAM")


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
