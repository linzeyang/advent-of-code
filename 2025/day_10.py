"""
day_10.py

Day 10: Factory

https://adventofcode.com/2025/day/10
"""

from itertools import combinations
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.entries: list = []

        with DATA_PATH.joinpath("10.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.entries.append(self._process_entry(line=line.strip()))

    def _process_entry(
        self, line: str
    ) -> tuple[int, list[int], list[list[str]], list[int]]:
        splits: list[str] = line.split(" ")

        light_diagram: str = splits[0][1:-1]
        light: int = int(light_diagram.replace(".", "0").replace("#", "1"), 2)

        buttons: list[int] = []
        button_bits: list[list[str]] = []

        for raw_button in splits[1:-1]:
            bits: list[str] = ["0"] * len(light_diagram)

            for num in raw_button[1:-1].split(","):
                bits[int(num)] = "1"

            button_bits.append(bits)
            buttons.append(int("".join(bits), 2))

        joltage_req: list[int] = list(map(int, splits[-1][1:-1].split(",")))

        return light, buttons, button_bits, joltage_req

    def part1(self) -> int:
        """
        # Because:
        # 1. XOR is commutative
        # 2. XORing a number with itself yields 0
        # 3. XORing 0 with any number yields the number itself
        # Therefore, using each button any number of times reduces to
        # using each button at most once.
        # That is, the goal is to find the minimum number of operations
        # using each button in 'buttons' at most once to XOR-accumulate 'status'
        # until it equals 'light'
        """

        out: int = 0

        for light, buttons, _, _ in self.entries:
            breaked: bool = False

            # Try every combination of buttons, starting from 1 button
            # and up to all buttons
            for k in range(1, len(buttons) + 1):
                for comb in combinations(buttons, k):
                    status: int = 0

                    for num in comb:
                        status ^= num

                    if status == light:
                        out += k
                        breaked = True
                        break

                if breaked:
                    break

        return out

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
