"""
day_04.py

Day 4: Secure Container

https://adventofcode.com/2021/day/4
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("04.txt").open("r", encoding="utf-8") as file:
            start, end = file.readline().strip().split("-")

        self.start: str = start
        self.end: str = end

    def part1(self) -> int:
        """part1"""

        def qualify(number: int) -> bool:
            number_str = str(number)
            dup: bool = False

            for idx in range(1, len(number_str)):
                if number_str[idx] == number_str[idx - 1]:
                    dup = True

                if number_str[idx] < number_str[idx - 1]:
                    return False

            return dup

        return sum(
            1 for number in range(int(self.start), int(self.end) + 1) if qualify(number)
        )

    def part2(self) -> int:
        """part2"""

        def qualify(number: int) -> bool:
            number_str = str(number)

            min_dup_count: int = 6
            dup_count: int | None = None

            for idx in range(1, len(number_str)):
                if number_str[idx] < number_str[idx - 1]:
                    return False

                if number_str[idx] == number_str[idx - 1]:
                    if not dup_count:
                        dup_count = 2
                    else:
                        dup_count += 1
                elif dup_count:
                    min_dup_count = min(min_dup_count, dup_count)
                    dup_count = None

            if dup_count:
                min_dup_count = min(min_dup_count, dup_count)

            return min_dup_count == 2

        return sum(
            1 for number in range(int(self.start), int(self.end) + 1) if qualify(number)
        )


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
