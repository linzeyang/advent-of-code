"""
day_01.py

Day 01: Secret Entrance

https://adventofcode.com/2025/day/01
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.sequence: list[tuple[str, int]] = []

        with DATA_PATH.joinpath("01.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.sequence.append((line[0], int(line[1:])))

    def part1(self) -> int:
        """part1"""

        current: int = 50
        out: int = 0

        for direction, amount in self.sequence:
            match direction:
                case "R":
                    current = (current + amount) % 100
                case "L":
                    current = (current - amount) % 100

            if not current:
                out += 1

        return out

    def part2(self) -> int:
        """part2"""

        current: int = 50
        out: int = 0

        for direction, amount in self.sequence:
            # Each full rotation (100 clicks) passes 0 exactly once
            div, mod = divmod(amount, 100)
            out += div

            match direction:
                case "R":
                    # Moving right (increasing numbers):
                    # Passes 0 if we cross the 99 -> 0 boundary
                    if current + mod >= 100:
                        out += 1

                    current = (current + mod) % 100
                case "L":
                    # Moving left (decreasing numbers):
                    # Passes 0 if we reach 0 or cross the 0 -> 99 boundary
                    # Note: If we start at 0, we immediately leave it.
                    # So only count if current > 0 AND we move enough to reach/pass 0.
                    if current > 0 and mod >= current:
                        out += 1

                    current = (current - mod) % 100

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
