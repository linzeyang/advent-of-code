"""
day_11.py

Day 11: ???

https://adventofcode.com/2020/day/11
"""

from copy import deepcopy
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.map: list[list[str]] = []

        with DATA_PATH.joinpath("11.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.map.append(list(line.strip()))

        self.len_x = len(self.map)
        self.len_y = len(self.map[0])

        # first step: make all empty seats occupied
        for line in self.map:
            for jdx, kind in enumerate(line):
                if kind == "L":
                    line[jdx] = "#"

    def part1(self) -> int:
        """part1"""

        map1 = deepcopy(self.map)

        while True:
            to_flip: list[tuple[int, int]] = []

            for idx, line in enumerate(map1):
                for jdx, kind in enumerate(line):
                    _, num_occupied = self._check_adjacents(mapp=map1, idx=idx, jdx=jdx)

                    if kind == "L" and num_occupied == 0:
                        to_flip.append((idx, jdx))
                    elif kind == "#" and num_occupied >= 4:
                        to_flip.append((idx, jdx))

            if not to_flip:
                break

            for idx, jdx in to_flip:
                if map1[idx][jdx] == "L":
                    map1[idx][jdx] = "#"
                else:
                    map1[idx][jdx] = "L"

        out = 0

        for line in map1:
            out += line.count("#")

        return out

    def _check_adjacents(self, mapp: list, idx: int, jdx: int) -> tuple[int, int]:
        """check adjacents"""

        num_empty = num_occupied = 0

        for x, y in (
            (idx - 1, jdx - 1),
            (idx - 1, jdx),
            (idx - 1, jdx + 1),
            (idx, jdx - 1),
            (idx, jdx + 1),
            (idx + 1, jdx - 1),
            (idx + 1, jdx),
            (idx + 1, jdx + 1),
        ):
            if x < 0 or x >= self.len_x or y < 0 or y >= self.len_y:
                continue

            match mapp[x][y]:
                case "#":
                    num_occupied += 1
                case "L":
                    num_empty += 1

        return num_empty, num_occupied

    def part2(self) -> int:
        """part2"""

        map2 = deepcopy(self.map)

        while True:
            to_flip: list[tuple[int, int]] = []

            for idx, line in enumerate(map2):
                for jdx, kind in enumerate(line):
                    _, num_occupied = self._check_directions(
                        mapp=map2, idx=idx, jdx=jdx
                    )

                    if kind == "L" and num_occupied == 0:
                        to_flip.append((idx, jdx))
                    elif kind == "#" and num_occupied >= 5:
                        to_flip.append((idx, jdx))

            if not to_flip:
                break

            for idx, jdx in to_flip:
                if map2[idx][jdx] == "L":
                    map2[idx][jdx] = "#"
                else:
                    map2[idx][jdx] = "L"

        out = 0

        for line in map2:
            out += line.count("#")

        return out

    def _check_directions(self, mapp: list, idx: int, jdx: int) -> tuple[int, int]:
        """check directions"""

        num_empty = num_occupied = 0

        for delta_x, delta_y in (
            (-1, -1),
            (-1, 0),
            (-1, +1),
            (0, -1),
            (0, +1),
            (+1, -1),
            (+1, 0),
            (+1, +1),
        ):
            temp_x = idx + delta_x
            temp_y = jdx + delta_y

            while (0 <= temp_x < self.len_x) and (0 <= temp_y < self.len_y):
                match mapp[temp_x][temp_y]:
                    case "#":
                        num_occupied += 1
                        break
                    case "L":
                        num_empty += 1
                        break

                temp_x += delta_x
                temp_y += delta_y

        return num_empty, num_occupied


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
