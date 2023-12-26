"""
2023 Day 24
https://adventofcode.com/2023/day/24
"""

# from decimal import Decimal
from itertools import combinations
from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "24.txt"

    def part_one(self) -> int:
        """part one answer"""

        points_velocity = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                coords, velo = line.split(" @ ")

                coords = tuple(int(part) for part in coords.split(", "))
                velo = tuple(int(part) for part in velo.split(", "))

                points_velocity.append((coords, velo))

        answer = 0

        for point1, point2 in combinations(points_velocity, 2):
            will_inter, inter = self._get_inter(point1, point2)

            if will_inter and 2e14 <= inter[0] <= 4e14 and 2e14 <= inter[1] <= 4e14:
                answer += 1

        return answer

    def _get_inter(self, point1, point2) -> tuple[bool, tuple]:
        coords1, velo1 = point1
        coords2, velo2 = point2

        x1, y1, _ = coords1
        x2, y2, _ = coords2

        a1 = velo1[1] / velo1[0]
        a2 = velo2[1] / velo2[0]

        c1 = y1 - a1 * x1
        c2 = y2 - a2 * x2

        if a1 == a2:
            return False, ()

        x = (c2 - c1) / (a1 - a2)
        y = a1 * x + c1

        if (
            (velo1[0] < 0 and x > x1)
            or (velo1[0] > 0 and x < x1)
            or (velo2[0] < 0 and x > x2)
            or (velo2[0] > 0 and x < x2)
        ):
            return False, ()

        return True, (x, y)

    def part_two(self) -> int:
        """part two answer"""

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                line.count("")

        answer = 0

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
