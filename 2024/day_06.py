"""
day_06.py

Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6
"""

from itertools import cycle
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.sparse_matrix: list[list[int]] = []

        self.starting_point: tuple = ()

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.sparse_matrix.append(
                    [idx for idx, char in enumerate(line.strip()) if char == "#"]
                )

                if "^" in line:
                    self.starting_point = (len(self.sparse_matrix) - 1, line.index("^"))

        self.i_len = len(self.sparse_matrix)
        self.j_len = len(line)

    def part1(self) -> int:  # noqa: C901
        """part1"""

        direction_cycle = cycle(("U", "R", "D", "L"))

        direction = next(direction_cycle)  # UP

        visited: set[tuple[int, int]] = {self.starting_point}

        current_point: tuple[int, int] = self.starting_point

        while True:
            current_i, current_j = current_point

            match direction:
                case "U":
                    for idx in range(current_i - 1, -1, -1):
                        if current_j in self.sparse_matrix[idx]:
                            current_point = (idx + 1, current_j)

                            for iidx in range(current_i, idx, -1):
                                visited.add((iidx, current_j))

                            break
                    else:
                        for iidx in range(current_i, -1, -1):
                            visited.add((iidx, current_j))
                        break
                case "R":
                    for jdx in range(current_j + 1, self.j_len):
                        if jdx in self.sparse_matrix[current_i]:
                            current_point = (current_i, jdx - 1)

                            for jjdx in range(current_j, jdx):
                                visited.add((current_i, jjdx))

                            break
                    else:
                        for jjdx in range(current_j, self.j_len):
                            visited.add((current_i, jjdx))

                        break
                case "D":
                    for idx in range(current_i + 1, self.i_len):
                        if current_j in self.sparse_matrix[idx]:
                            current_point = (idx - 1, current_j)

                            for iidx in range(current_i, idx - 1):
                                visited.add((iidx, current_j))

                            break
                    else:
                        for iidx in range(current_i, self.i_len):
                            visited.add((iidx, current_j))
                        break
                case "L":
                    for jdx in range(current_j - 1, -1, -1):
                        if jdx in self.sparse_matrix[current_i]:
                            current_point = (current_i, jdx + 1)

                            for jjdx in range(current_j, jdx, -1):
                                visited.add((current_i, jjdx))

                            break
                    else:
                        for jjdx in range(current_j, -1, -1):
                            visited.add((current_i, jjdx))
                        break

            direction = next(direction_cycle)

        return len(visited)

    def part2(self) -> int:
        """part2"""

        return -1


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
