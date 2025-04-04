"""
day_25.py

Day 25: Combo Breaker

https://adventofcode.com/2020/day/25
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("25.txt").open("r", encoding="utf-8") as file:
            self.card_public_key = int(file.readline().strip())
            self.door_public_key = int(file.readline().strip())

    def part1(self) -> int:
        """part1"""

        SUBJECT_NUMBER = 7
        DIVISOR = 20201227

        value = 1
        card_loop = 0

        while value != self.card_public_key:
            value = (value * SUBJECT_NUMBER) % DIVISOR
            card_loop += 1

        print(f"Card loop is {card_loop}")

        value = 1

        for _ in range(card_loop):
            value = (value * self.door_public_key) % DIVISOR

        return value

    def part2(self) -> int:
        """Day 25 has no part 2"""

        return -1


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print("Day 25 has no part 2.")


if __name__ == "__main__":
    main()
