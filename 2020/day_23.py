"""
day_23.py

Day 23: Crab Cups

https://adventofcode.com/2020/day/23
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("23.txt").open("r", encoding="utf-8") as file:
            self.raw_input = file.readline().strip()

        self.initial_state: list[int] = [int(c) for c in self.raw_input]

    def part1(self) -> str:
        """part1"""

        state: list[int] = self.initial_state[:]

        current_idx = 0
        current_value = state[current_idx]

        for _ in range(100):
            next_a = state[(current_idx + 1) % 9]
            next_b = state[(current_idx + 2) % 9]
            next_c = state[(current_idx + 3) % 9]

            for val in (next_a, next_b, next_c):
                state.remove(val)

            destination = current_value - 1

            if destination < 1:
                destination = 9

            while destination in (next_a, next_b, next_c):
                destination -= 1

                if destination < 1:
                    destination = 9

            destination_idx = state.index(destination)

            state.insert(destination_idx + 1, next_a)
            state.insert(destination_idx + 2, next_b)
            state.insert(destination_idx + 3, next_c)

            current_idx = (state.index(current_value) + 1) % 9
            current_value = state[current_idx]

        out: list[str] = []

        for offset in range(1, 9):
            out.append(str(state[(state.index(1) + offset) % 9]))

        return "".join(out)

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
