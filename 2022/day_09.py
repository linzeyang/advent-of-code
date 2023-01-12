"""
2022 Day 09
https://adventofcode.com/2022/day/9
"""

from pathlib import Path


class BaseKnot:
    def __init__(self, parent=None) -> None:
        self.x = 0
        self.y = 0
        self.parent = parent

    def distance(self) -> int:
        return max(abs(self.x - self.parent.x), abs(self.y - self.parent.y))

    def move(self, direct: str) -> None:
        if direct == "R":
            self.move_x(1)
        elif direct == "L":
            self.move_x(-1)
        elif direct == "U":
            self.move_y(1)
        else:
            self.move_y(-1)

    def move_x(self, direction: int) -> None:
        self.x += direction

    def move_y(self, direction: int) -> None:
        self.y += direction

    def adjust(self) -> None:
        if self.distance() < 2:
            return

        if abs(self.x - self.parent.x) > 1 and abs(self.y - self.parent.y) > 1:
            if self.parent.x - self.x > 1:
                self.x = self.parent.x - 1
            elif self.x - self.parent.x > 1:
                self.x = self.parent.x + 1
            if self.parent.y - self.y > 1:
                self.y = self.parent.y - 1
            elif self.y - self.parent.y > 1:
                self.y = self.parent.y + 1
        else:
            if self.parent.x - self.x > 1:
                self.y = self.parent.y
                self.x = self.parent.x - 1
            elif self.x - self.parent.x > 1:
                self.y = self.parent.y
                self.x = self.parent.x + 1
            elif self.parent.y - self.y > 1:
                self.x = self.parent.x
                self.y = self.parent.y - 1
            elif self.y - self.parent.y > 1:
                self.x = self.parent.x
                self.y = self.parent.y + 1

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "09.txt"

    def part_one(self) -> int:
        """part one answer"""

        self.head = BaseKnot()
        self.tail = BaseKnot(parent=self.head)
        self.tailed: set[tuple[int, int]] = {(0, 0)}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                direct, steps = line.split()

                for _ in range(int(steps)):
                    self.head.move(direct)
                    self.tail.adjust()

                    self.tailed.add(self.tail.position)

        return len(self.tailed)

    def part_two(self) -> int:
        """part two answer"""

        self.head = BaseKnot()

        prev = self.head

        self.knots: list[BaseKnot] = []

        for _ in range(9):
            knot = BaseKnot(parent=prev)
            self.knots.append(knot)
            prev = knot

        self.tailed: set[tuple[int, int]] = {(0, 0)}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                direct, steps = line.split()

                for _ in range(int(steps)):
                    self.head.move(direct)

                    for knot in self.knots:
                        knot.adjust()

                    self.tailed.add(knot.position)

        return len(self.tailed)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
