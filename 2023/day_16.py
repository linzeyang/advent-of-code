"""
2023 Day 16
https://adventofcode.com/2023/day/16
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "16.txt"

    def part_one(self) -> int:
        """part one answer"""

        matrix: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

        answer = self._get_energized(matrix=matrix, starting=(0, 0, 0))

        return answer

    def part_two(self) -> int:
        """part two answer"""

        matrix: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

        results: list[int] = []

        for idx in range(len(matrix[0])):
            results.append(self._get_energized(matrix, (idx, 0, 1)))

        for idx in range(len(matrix[0])):
            results.append(self._get_energized(matrix, (idx, len(matrix) - 1, 3)))

        for idx in range(len(matrix)):
            results.append(self._get_energized(matrix, (0, idx, 0)))

        for idx in range(len(matrix)):
            results.append(self._get_energized(matrix, (len(matrix[0]) - 1, idx, 2)))

        answer = max(results)
        return answer

    def _get_energized(self, matrix: list[str], starting: tuple[int, int, int]) -> int:
        width = len(matrix[0])
        height = len(matrix)

        energized: set[tuple[int, int]] = set()
        status: list[tuple[int, int, int]] = [starting]
        history: set[tuple[int, int, int]] = set()

        while status:
            new_status: list[tuple[int, int, int]] = []

            for coordx, coordy, direct in status:
                if not (0 <= coordx < width and 0 <= coordy < height):
                    continue

                if (coordx, coordy, direct) in history:
                    continue

                history.add((coordx, coordy, direct))
                energized.add((coordx, coordy))

                if matrix[coordy][coordx] == ".":
                    if direct == 0:
                        coordx += 1
                    elif direct == 2:
                        coordx -= 1
                    elif direct == 1:
                        coordy += 1
                    else:
                        coordy -= 1

                    new_status.append((coordx, coordy, direct))
                elif matrix[coordy][coordx] == "|":
                    if direct == 0 or direct == 2:
                        new_status.append((coordx, coordy - 1, 3))
                        new_status.append((coordx, coordy + 1, 1))
                    elif direct == 1:
                        new_status.append((coordx, coordy + 1, direct))
                    else:
                        new_status.append((coordx, coordy - 1, direct))
                elif matrix[coordy][coordx] == "-":
                    if direct == 1 or direct == 3:
                        new_status.append((coordx - 1, coordy, 2))
                        new_status.append((coordx + 1, coordy, 0))
                    elif direct == 0:
                        new_status.append((coordx + 1, coordy, direct))
                    else:
                        new_status.append((coordx - 1, coordy, direct))
                elif matrix[coordy][coordx] == "/":
                    if direct == 0:
                        new_status.append((coordx, coordy - 1, 3))
                    elif direct == 1:
                        new_status.append((coordx - 1, coordy, 2))
                    elif direct == 2:
                        new_status.append((coordx, coordy + 1, 1))
                    else:
                        new_status.append((coordx + 1, coordy, 0))
                elif matrix[coordy][coordx] == "\\":
                    if direct == 0:
                        new_status.append((coordx, coordy + 1, 1))
                    elif direct == 1:
                        new_status.append((coordx + 1, coordy, 0))
                    elif direct == 2:
                        new_status.append((coordx, coordy - 1, 3))
                    else:
                        new_status.append((coordx - 1, coordy, 2))

            status = new_status

        return len(energized)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
