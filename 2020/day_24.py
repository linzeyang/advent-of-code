"""
day_24.py

Day 24: Lobby Layout

https://adventofcode.com/2020/day/24
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.instructions: list[str] = []

        with DATA_PATH.joinpath("24.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.instructions.append(line.strip())

    def part1(self) -> int:
        """part1"""

        turned_tiles: set[tuple[int, int]] = set()

        for instruction in self.instructions:
            # 1. interpret instruction to get the directions
            directions = self._interpret(instruction)

            # 2. get the coordinate of the tile
            coordinate = self._get_coordinate(directions)

            # 3. add or remove the tile from the set
            if coordinate in turned_tiles:
                turned_tiles.remove(coordinate)
            else:
                turned_tiles.add(coordinate)

        return len(turned_tiles)

    @staticmethod
    def _interpret(instruction: str) -> list[str]:
        """interpret instruction to get the directions"""

        out: list[str] = []

        idx = 0

        while idx < len(instruction):
            if instruction[idx] == "n" or instruction[idx] == "s":
                out.append(instruction[idx : idx + 2])
                idx += 2
            else:
                out.append(instruction[idx])
                idx += 1

        return out

    @staticmethod
    def _get_coordinate(directions: list[str]) -> tuple[int, int]:
        """get the coordinate of the tile"""

        x = y = 0

        for direction in directions:
            match direction:
                case "e":
                    x += 2
                case "w":
                    x -= 2
                case "ne":
                    x += 1
                    y += 1
                case "nw":
                    x -= 1
                    y += 1
                case "se":
                    x += 1
                    y -= 1
                case "sw":
                    x -= 1
                    y -= 1

        return x, y

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
