"""
day_15.py

Day 15: Rambunctious Recitation

https://adventofcode.com/2020/day/15
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("15.txt").open("r", encoding="utf-8") as file:
            self.staring_numbers = [int(part) for part in file.readline().split(",")]

    def part1(self) -> int:
        """part1"""

        memory: dict[int, list[int]] = {}

        for idx, number in enumerate(self.staring_numbers):
            memory[number] = [idx + 1]

        last = self.staring_numbers[-1]
        round_number = len(self.staring_numbers) + 1

        while round_number <= 2020:
            if last in memory and len(memory[last]) == 1:
                last = 0
            elif last not in memory:
                last = 0
            else:
                last = memory[last][-1] - memory[last][-2]

            if last in memory:
                memory[last].append(round_number)
            else:
                memory[last] = [round_number]

            round_number += 1

        return last

    def part2(self) -> int:
        """part2"""

        memory: dict[int, list[int]] = {}

        for idx, number in enumerate(self.staring_numbers):
            memory[number] = [idx + 1]

        last = self.staring_numbers[-1]
        round_number = len(self.staring_numbers) + 1

        while round_number <= 30_000_000:
            if last in memory and len(memory[last]) == 1:
                last = 0
            elif last not in memory:
                last = 0
            else:
                last = memory[last][-1] - memory[last][-2]

            if last in memory:
                memory[last].append(round_number)

                if len(memory[last]) > 2:
                    memory[last].pop(0)
            else:
                memory[last] = [round_number]

            round_number += 1

        return last


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
