"""
2023 Day 22
https://adventofcode.com/2023/day/22
"""

from dataclasses import dataclass
from pathlib import Path

from typing_extensions import Self


@dataclass
class Brick:
    start: tuple[int, ...]
    end: tuple[int, ...]

    def __hash__(self) -> int:
        return hash((self.start, self.end))

    def __eq__(self, __value: Self) -> bool:
        return self.start == __value.start and self.end == __value.end


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "22.txt"

    def part_one(self) -> int:
        """part one answer"""

        bricks: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                part1, part2 = line.split("~")

                bricks.append(
                    (
                        tuple(int(num) for num in part1.split(",")),
                        tuple(int(num) for num in part2.split(",")),
                    )
                )

        bricks.sort(key=lambda tup: tup[0][2])

        dependency_mapping: dict[Brick, set[Brick]] = {}
        z_mapping: dict[int, set[Brick]] = {1: set()}
        all_bricks: set[Brick] = set()

        for raw_brick in bricks:
            z_range = raw_brick[1][2] - raw_brick[0][2] + 1

            if raw_brick[0][2] == 1:
                brick = Brick(start=raw_brick[0], end=raw_brick[1])

                for idx in range(z_range):
                    if 1 + idx not in z_mapping:
                        z_mapping[1 + idx] = {brick}
                    else:
                        z_mapping[1 + idx].add(brick)

                dependency_mapping[brick] = set()
                all_bricks.add(brick)
                continue

            deps: set[Brick] = set()

            for idx in range(raw_brick[0][2] - 1, 0, -1):
                if idx not in z_mapping or not z_mapping[idx]:
                    continue

                for existing_brick in z_mapping[idx]:
                    if self._intersect(existing_brick, raw_brick):
                        deps.add(existing_brick)

                if deps:
                    break

            new_z = idx + 1 if deps else 1

            brick = Brick(
                start=(raw_brick[0][0], raw_brick[0][1], new_z),
                end=(raw_brick[1][0], raw_brick[1][1], new_z + z_range - 1),
            )

            all_bricks.add(brick)

            for z in range(new_z, new_z + z_range):
                if z not in z_mapping:
                    z_mapping[z] = {brick}
                else:
                    z_mapping[z].add(brick)

            dependency_mapping[brick] = deps

        dependenci: set[Brick] = set()

        for brick, dependencies in dependency_mapping.items():
            if len(dependencies) == 1:
                dep = next(iter(dependencies))
                dependenci.add(dep)

        answer = len(all_bricks - dependenci)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        bricks: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                part1, part2 = line.split("~")

                bricks.append(
                    (
                        tuple(int(num) for num in part1.split(",")),
                        tuple(int(num) for num in part2.split(",")),
                    )
                )

        bricks.sort(key=lambda tup: tup[0][2])

        dependency_mapping: dict[Brick, set[Brick]] = {}
        dependee_mapping: dict[Brick, set[Brick]] = {}
        result_mapping: dict[Brick, int] = {}
        z_mapping: dict[int, set[Brick]] = {1: set()}

        for raw_brick in bricks:
            z_range = raw_brick[1][2] - raw_brick[0][2] + 1

            if raw_brick[0][2] == 1:
                brick = Brick(start=raw_brick[0], end=raw_brick[1])

                for idx in range(z_range):
                    if 1 + idx not in z_mapping:
                        z_mapping[1 + idx] = {brick}
                    else:
                        z_mapping[1 + idx].add(brick)

                dependency_mapping[brick] = set()
                continue

            deps: set[Brick] = set()

            for idx in range(raw_brick[0][2] - 1, 0, -1):
                if idx not in z_mapping or not z_mapping[idx]:
                    continue

                for existing_brick in z_mapping[idx]:
                    if self._intersect(existing_brick, raw_brick):
                        deps.add(existing_brick)

                if deps:
                    break

            new_z = idx + 1 if deps else 1

            brick = Brick(
                start=(raw_brick[0][0], raw_brick[0][1], new_z),
                end=(raw_brick[1][0], raw_brick[1][1], new_z + z_range - 1),
            )

            for z in range(new_z, new_z + z_range):
                if z not in z_mapping:
                    z_mapping[z] = {brick}
                else:
                    z_mapping[z].add(brick)

            dependency_mapping[brick] = deps

            for dep in deps:
                if dep not in dependee_mapping:
                    dependee_mapping[dep] = {brick}
                else:
                    dependee_mapping[dep].add(brick)

        for z in sorted(z_mapping.keys()):
            for brick in z_mapping[z]:
                if brick in result_mapping or brick not in dependee_mapping:
                    continue

                would_falls = {brick}
                uppers = dependee_mapping[brick]

                while uppers:
                    temp_uppers: set[Brick] = set()

                    for up in uppers:
                        if up not in dependency_mapping:
                            continue

                        if dependency_mapping[up].issubset(would_falls):
                            would_falls.add(up)

                            if up in dependee_mapping:
                                temp_uppers |= dependee_mapping[up]

                    uppers = temp_uppers

                if len(would_falls) > 1:
                    result_mapping[brick] = len(would_falls) - 1

        answer = sum(result_mapping.values())

        return answer

    def _intersect(self, brick: Brick, raw_brick: tuple) -> bool:
        if (
            raw_brick[1][0] < brick.start[0]
            or raw_brick[0][0] > brick.end[0]
            or raw_brick[1][1] < brick.start[1]
            or raw_brick[0][1] > brick.end[1]
        ):
            return False

        return True

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
