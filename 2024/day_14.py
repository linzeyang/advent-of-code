"""
day_14.py

Day 14: Restroom Redoubt

https://adventofcode.com/2024/day/14
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.robots: list[list[int]] = []

        with DATA_PATH.joinpath("14.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                parts = line.split(" ")

                part1 = parts[0][2:].split(",")
                part2 = parts[1][2:].split(",")

                self.robots.append(
                    [int(part1[0]), int(part1[1]), int(part2[0]), int(part2[1])]
                )

    def part1(self) -> int:
        """part1"""

        LEN_X, LEN_Y = 101, 103
        HALF_X, HALF_Y = LEN_X // 2, LEN_Y // 2

        num_q1 = num_q2 = num_q3 = num_q4 = 0

        for robot in self.robots:
            coord_x, coord_y = self._calc_1(robot)

            if 0 <= coord_x < HALF_X:
                if 0 <= coord_y < HALF_Y:
                    num_q1 += 1
                elif coord_y > HALF_Y:
                    num_q2 += 1
            elif coord_x > HALF_X:
                if 0 <= coord_y < HALF_Y:
                    num_q3 += 1
                elif coord_y > HALF_Y:
                    num_q4 += 1

        return num_q1 * num_q2 * num_q3 * num_q4

    def _calc_1(self, robot: list[int]) -> tuple[int, int]:
        """calculate 1"""

        LEN_X, LEN_Y = 101, 103

        return (robot[0] + 100 * robot[2]) % LEN_X, (robot[1] + 100 * robot[3]) % LEN_Y

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
