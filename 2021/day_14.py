"""
day_14.py

Day 14: Extended Polymerization

https://adventofcode.com/2021/day/14
"""

from collections import Counter
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rules: dict[str, str] = {}

        with DATA_PATH.joinpath("14.txt").open("r", encoding="utf-8") as file:
            self.state: str = file.readline().strip()

            file.readline()

            for line in file:
                self.rules[line.split(" -> ")[0]] = line.strip().split(" -> ")[1]

    def _process_k_steps(self, k: int) -> int:
        """Process k steps of polymerization.

        Args:
            k (int): The number of steps to process.

        Returns:
            int: The difference between the most common and least common element count.
        """

        state: Counter[str] = Counter(
            self.state[idx : idx + 2] for idx in range(len(self.state) - 1)
        )

        for _ in range(k):
            new_state: Counter[str] = Counter()

            for pair, count in state.items():
                new_state[pair[0] + self.rules[pair]] += count
                new_state[self.rules[pair] + pair[1]] += count

            state = new_state

        freq: Counter[str] = Counter()

        for pair, count in state.items():
            freq[pair[0]] += count
            freq[pair[1]] += count

        return (freq.most_common()[0][1] - freq.most_common()[-1][1]) // 2 + 1

    def part1(self) -> int:
        """part1"""

        return self._process_k_steps(k=10)

    def part2(self) -> int:
        """part2"""

        return self._process_k_steps(k=40)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
