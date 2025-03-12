"""
day_12.py

Day 12: Rain Risk

https://adventofcode.com/2020/day/12
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.instructions: list[str] = []

        with DATA_PATH.joinpath("12.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.instructions.append(line.strip())

    def part1(self) -> int:  # noqa: C901
        """part1"""

        pos_x = pos_y = direction = 0

        for instruction in self.instructions:
            action = instruction[0]
            value = int(instruction[1:])

            match action:
                case "N":
                    pos_y += value
                case "S":
                    pos_y -= value
                case "E":
                    pos_x += value
                case "W":
                    pos_x -= value
                case "L":
                    direction = (direction - value) % 360
                case "R":
                    direction = (direction + value) % 360
                case "F":
                    match direction:
                        case 0:
                            pos_x += value
                        case 90:
                            pos_y -= value
                        case 180:
                            pos_x -= value
                        case 270:
                            pos_y += value

        return abs(pos_x) + abs(pos_y)

    def part2(self) -> int:  # noqa: C901
        """part2"""

        pos_x = pos_y = 0

        waypoint_x, waypoint_y = 10, 1

        for instruction in self.instructions:
            action = instruction[0]
            value = int(instruction[1:])

            match action:
                case "N":
                    waypoint_y += value
                case "S":
                    waypoint_y -= value
                case "E":
                    waypoint_x += value
                case "W":
                    waypoint_x -= value
                case "L":
                    for _ in range(value // 90):
                        waypoint_x, waypoint_y = -waypoint_y, waypoint_x
                case "R":
                    for _ in range(value // 90):
                        waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                case "F":
                    pos_x += value * waypoint_x
                    pos_y += value * waypoint_y

        return abs(pos_x) + abs(pos_y)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
