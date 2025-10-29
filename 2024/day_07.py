"""
day_07.py

Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


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

        out: int = 0

        for test_value, numbers in self.equations:
            if self._validate_1(target=test_value, numbers=numbers):
                out += test_value

        return out

    def _validate_1(self, target: int, numbers: tuple[int, ...]) -> bool:
        """validate for part 1"""

        if len(numbers) == 2:
            return target == sum(numbers) or target == numbers[0] * numbers[1]

        last_number: int = numbers[-1]

        if target % last_number == 0:
            return self._validate_1(
                target=target // last_number, numbers=numbers[:-1]
            ) or self._validate_1(target=target - last_number, numbers=numbers[:-1])

        return self._validate_1(target=target - last_number, numbers=numbers[:-1])

    def part2(self) -> int:
        """part2"""

        out: int = 0

        for test_value, numbers in self.equations:
            if self._validate_2(target=test_value, numbers=numbers):
                out += test_value

        return out

    def _validate_2(self, target: int, numbers: tuple[int, ...]) -> bool:
        """validate for part 2 with concatenation operator"""

        if len(numbers) == 2:
            # Base case: try all three operations
            return (
                target == sum(numbers)  # addition
                or target == numbers[0] * numbers[1]  # multiplication
                or target == int(str(numbers[0]) + str(numbers[1]))  # concatenation
            )

        last_number: int = numbers[-1]
        last_number_str: str = str(last_number)
        target_str: str = str(target)

        # Try reverse concatenation: if target ends with last_number digits
        if target_str.endswith(last_number_str) and len(target_str) > len(
            last_number_str
        ):
            new_target_str: str = target_str[: -len(last_number_str)]

            if new_target_str:  # Make sure we don't get empty string
                new_target: int = int(new_target_str)

                if self._validate_2(target=new_target, numbers=numbers[:-1]):
                    return True

        # Try reverse multiplication: if target is divisible by last_number
        if target % last_number == 0:
            if self._validate_2(target=target // last_number, numbers=numbers[:-1]):
                return True

        # Try reverse addition: subtract last_number from target
        if target > last_number:  # Ensure we don't go negative
            return self._validate_2(target=target - last_number, numbers=numbers[:-1])

        return False


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
