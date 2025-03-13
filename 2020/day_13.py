"""
day_13.py

Day 13: Shuttle Search

https://adventofcode.com/2020/day/13
"""

from math import ceil
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("13.txt").open("r", encoding="utf-8") as file:
            self.ts = int(file.readline())

            second_line = file.readline().strip()

            self.raw_buses: list[int] = [
                int(bus) if bus != "x" else 0 for bus in second_line.split(",")
            ]
            self.buses: list[int] = [
                int(bus) for bus in second_line.split(",") if bus != "x"
            ]

    def part1(self) -> int:
        """part1"""

        best_bus, wait_time = -1, max(self.buses) + 1

        for bus in self.buses:
            time = ceil(self.ts / bus) * bus - self.ts

            if time < wait_time:
                best_bus, wait_time = bus, time

        return best_bus * wait_time

    def part2(self) -> int:
        """part2"""

        buses: list = []

        for idx, bus in enumerate(self.raw_buses):
            if not bus:
                continue

            buses.append((bus, idx))

        # [(37, 0), (41, 27), (433, 37), (23, 45), (17, 54), (19, 56), (29, 66),
        #  (593, 68), (13, 81)]

        factor = 1
        base = 593 * 41 * 23 * 13

        while factor:
            num = base * factor

            if (
                (num - 68) % 37
                or (num - 31) % 433
                or (num - 14) % 17
                or (num - 12) % 19
                or (num - 2) % 29
            ):
                factor += 1
            else:
                break

        return num - 68  # 600691418730595


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
