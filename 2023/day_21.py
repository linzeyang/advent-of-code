"""
2023 Day 21
https://adventofcode.com/2023/day/21
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "21.txt"

    def part_one(self) -> int:
        """part one answer"""

        matrix: list[str] = []
        currents: list[tuple[int, int]] = []
        history_grids: set[tuple[int, int]] = set()
        even_grids = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

                if "S" in line:
                    starting_point = (len(matrix) - 1, line.index("S"))
                    currents.append(starting_point)
                    history_grids.add(starting_point)
                    even_grids += 1

        for step in range(1, 65):
            temp: list[tuple[int, int]] = []

            for y, x in currents:
                for delta_y, delta_x in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y + delta_y, x + delta_x

                    if (
                        new_y < 0
                        or new_y >= len(matrix)
                        or new_x < 0
                        or new_x > len(matrix[0])
                    ):
                        continue

                    if matrix[new_y][new_x] == "#" or (new_y, new_x) in history_grids:
                        continue

                    history_grids.add((new_y, new_x))
                    temp.append((new_y, new_x))

                    if step & 1 == 0:
                        even_grids += 1

            currents = temp

        answer = even_grids

        return answer

    def part_two(self) -> int:
        """part two answer"""

        matrix: list[str] = []
        currents: list[tuple[int, int]] = []
        history_grids: set[tuple[int, int]] = set()
        even_grids = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

                if "S" in line:
                    starting_point = (len(matrix) - 1, line.index("S"))
                    currents.append(starting_point)
                    history_grids.add(starting_point)
                    even_grids += 1

        for step in range(1, 26501366):
            temp: list[tuple[int, int]] = []

            for y, x in currents:
                for delta_y, delta_x in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y + delta_y, x + delta_x

                    if (
                        matrix[new_y % len(matrix)][new_x % len(matrix[0])] == "#"
                        or (new_y, new_x) in history_grids
                    ):
                        continue

                    history_grids.add((new_y, new_x))
                    temp.append((new_y, new_x))

                    if step & 1 == 0:
                        even_grids += 1

            currents = temp

        answer = even_grids

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
