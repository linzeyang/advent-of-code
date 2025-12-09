"""
day_06.py

Day 6: Lanternfish

https://adventofcode.com/2021/day/6
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.state: dict = dict.fromkeys(range(9), 0)

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            line: str = file.readline().strip()

            for num in line.split(","):
                self.state[int(num)] += 1

    def part1(self) -> int:
        """part1"""

        N = 80

        self._iterate(N)

        return sum(self.state.values())

    def part2(self) -> int:
        """part2"""

        # continue from day 80
        N: int = 256 - 80

        self._iterate(N)

        return sum(self.state.values())

    def _iterate(self, n: int) -> None:
        """iterate n days, modifies state in place."""

        for _ in range(n):
            (
                self.state[0],
                self.state[1],
                self.state[2],
                self.state[3],
                self.state[4],
                self.state[5],
                self.state[6],
                self.state[7],
                self.state[8],
            ) = (
                self.state[1],
                self.state[2],
                self.state[3],
                self.state[4],
                self.state[5],
                self.state[6],
                self.state[0] + self.state[7],
                self.state[8],
                self.state[0],
            )


if __name__ == "__main__":
    solution = Solution()
    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")
