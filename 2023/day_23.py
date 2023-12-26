"""
2023 Day 23
https://adventofcode.com/2023/day/23
"""

from copy import copy
from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "23.txt"

    def part_one(self) -> int:
        """part one answer"""

        matrix: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

        start = (0, 1)
        direct = (1, 0)

        answer = self._count_steps(start, direct, matrix)

        return answer

    def _count_steps(
        self, start: tuple[int, int], direct: tuple[int, int], matrix: list[str]
    ) -> int:
        steps = 0
        current = start

        outs = []

        while len(outs) < 2:
            if len(outs) == 1:
                current, direct = outs[0]

            temps_outs = []

            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if direction == (-direct[0], -direct[1]):
                    continue

                new_y, new_x = current[0] + direction[0], current[1] + direction[1]

                if new_y == len(matrix):
                    return steps

                if (
                    (direction[1] == 1 and matrix[new_y][new_x] not in ">.")
                    or (direction[1] == -1 and matrix[new_y][new_x] not in "<.")
                    or (direction[0] == 1 and matrix[new_y][new_x] not in "v.")
                    or (direction[0] == -1 and matrix[new_y][new_x] not in "^.")
                ):
                    continue

                temps_outs.append(((new_y, new_x), direction))

            outs = temps_outs
            steps += 1

        return steps + max(
            self._count_steps(new_coord, direc, matrix) for new_coord, direc in outs
        )

    def part_two(self) -> int:
        """part two answer"""

        matrix: list[list[str]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(list(line))

        start = (0, 1)
        direct = (1, 0)
        history: set[tuple[int, int]] = {start}

        global mapping
        mapping = {}

        answer = self._count_steps_2(start, direct, history, matrix)

        return answer

    def _count_steps_2(
        self,
        start: tuple[int, int],
        direct: tuple[int, int],
        history: set[tuple[int, int]],
        matrix: list[list[str]],
    ) -> int:
        steps = 0
        current = start

        outs = []

        while len(outs) < 2:
            if len(outs) == 1:
                current, direct = outs[0]
                history.add(current)

            temps_outs = []

            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if direction == (-direct[0], -direct[1]):
                    continue

                new_y, new_x = current[0] + direction[0], current[1] + direction[1]

                if new_y == len(matrix):
                    return steps

                if matrix[new_y][new_x] == "#" or (new_y, new_x) in history:
                    continue

                temps_outs.append(((new_y, new_x), direction))

            if not temps_outs:
                return -1

            outs = temps_outs
            steps += 1

        global mapping

        results: list[int] = []

        for new_coord, direc in outs:
            if (new_coord, direc) in mapping:
                res = mapping[(new_coord, direc)]
            else:
                his = copy(history)
                his.add(new_coord)
                res = self._count_steps_2(new_coord, direc, his, matrix)
                mapping[(new_coord, direc)] = res

            if res == -1:
                continue

            results.append(res)

        if not results:
            return -1

        return steps + max(results)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
