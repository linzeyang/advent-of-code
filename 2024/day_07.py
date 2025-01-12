"""
day_07.py

Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.equations: list[tuple[int, tuple[int, ...]]] = []

        with DATA_PATH.joinpath("07.txt").open("r", encoding="utf-8") as file:
            for line in file:
                test_value, numbers = line.strip().split(": ")
                self.equations.append(
                    (int(test_value), tuple(int(number) for number in numbers.split()))
                )

    def part1(self) -> int:
        """part1"""

        out = 0

        for test_value, numbers in self.equations:
            if self._validate_1(target=test_value, numbers=numbers):
                out += test_value

        return out

    def _validate_1(self, target: int, numbers: tuple[int, ...]) -> bool:
        """validate for part 1"""

        if len(numbers) == 2:
            return target == sum(numbers) or target == numbers[0] * numbers[1]

        last_number = numbers[-1]

        if target % last_number == 0:
            return self._validate_1(
                target=target // last_number, numbers=numbers[:-1]
            ) or self._validate_1(target=target - last_number, numbers=numbers[:-1])

        return self._validate_1(target=target - last_number, numbers=numbers[:-1])

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
