"""
day_10.py

Day 10: Hoof It

https://adventofcode.com/2024/day/10
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.map: list[list[int]] = []
        self.starting_points: list[tuple[int, int]] = []

        with DATA_PATH.joinpath("10.txt").open("r", encoding="utf-8") as file:
            for line in file:
                row: list[int] = []
                idx = len(self.map)

                for jdx, number in enumerate(line.strip()):
                    if number == "0":
                        self.starting_points.append((idx, jdx))

                    row.append(int(number))

                self.map.append(row)

    def part1(self) -> int:
        """part1"""

        out = 0

        for idx, jdx in self.starting_points:
            destinations = self._get_destinations(idx, jdx, 0)

            out += len(destinations)

        return out

    def _get_destinations(
        self, idx: int, jdx: int, height: int
    ) -> set[tuple[int, int]]:
        """get destinations"""

        neighbors: tuple[tuple[int, int], ...] = (
            (idx - 1, jdx),
            (idx + 1, jdx),
            (idx, jdx - 1),
            (idx, jdx + 1),
        )

        potentials: set[tuple[int, int]] = set()

        for neighbor_idx, neighbor_jdx in neighbors:
            if (
                neighbor_idx < 0
                or neighbor_idx >= len(self.map)
                or neighbor_jdx < 0
                or neighbor_jdx >= len(self.map[0])
                or self.map[neighbor_idx][neighbor_jdx] != height + 1
            ):
                continue

            potentials.add((neighbor_idx, neighbor_jdx))

        if height == 8:
            return potentials

        results: set[tuple[int, int]] = set()

        for potential_idx, potential_jdx in potentials:
            results.update(
                self._get_destinations(
                    idx=potential_idx, jdx=potential_jdx, height=height + 1
                )
            )

        return results

    def part2(self) -> int:
        """part2"""

        out = 0

        for idx, jdx in self.starting_points:
            can_reach, num_of_paths = self._get_unique_paths(idx, jdx, 0)

            if can_reach:
                out += num_of_paths

        return out

    def _get_unique_paths(self, idx: int, jdx: int, height: int) -> tuple[bool, int]:
        """get unique paths"""

        neighbors: tuple[tuple[int, int], ...] = (
            (idx - 1, jdx),
            (idx + 1, jdx),
            (idx, jdx - 1),
            (idx, jdx + 1),
        )

        potentials: set[tuple[int, int]] = set()

        for neighbor_idx, neighbor_jdx in neighbors:
            if (
                neighbor_idx < 0
                or neighbor_idx >= len(self.map)
                or neighbor_jdx < 0
                or neighbor_jdx >= len(self.map[0])
                or self.map[neighbor_idx][neighbor_jdx] != height + 1
            ):
                continue

            potentials.add((neighbor_idx, neighbor_jdx))

        if height == 8:
            return (True, len(potentials)) if potentials else (False, 0)

        total_num_of_paths = 0

        for potential_idx, potential_jdx in potentials:
            can_reach, num_of_paths = self._get_unique_paths(
                idx=potential_idx, jdx=potential_jdx, height=height + 1
            )

            if can_reach:
                total_num_of_paths += num_of_paths

        return (True, total_num_of_paths) if total_num_of_paths else (False, 0)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
