# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "z3-solver>=4.15.4.0",
# ]
# ///
# reference: https://packaging.python.org/en/latest/specifications/inline-script-metadata/
# usage: uv run day_10.py

"""
day_10.py

Day 10: Factory

https://adventofcode.com/2025/day/10
"""

from itertools import combinations
from pathlib import Path

import z3

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.entries: list[tuple[int, list[int], list[list[str]], list[int]]] = []

        with DATA_PATH.joinpath("10.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.entries.append(self._process_entry(line=line.strip()))

    def _process_entry(
        self, line: str
    ) -> tuple[int, list[int], list[list[str]], list[int]]:
        """
        Process a single entry from the input file.

        Args:
            line (str): A single line from the input file.

        Returns:
            tuple[int, list[int], list[list[str]], list[int]]: A tuple containing:
                - light (int): The light status represented as an integer
                - buttons (list[int]): A list of button statuses represented as integers
                - button_bits (list[list[str]]): A list of button statuses represented
                    as binary strings
                - joltage_req (list[int]): A list of joltage requirements
        """

        splits: list[str] = line.split(" ")

        light_diagram: str = splits[0][1:-1]
        light: int = int(light_diagram.replace(".", "0").replace("#", "1"), base=2)

        buttons: list[int] = []
        button_bits: list[list[str]] = []

        for raw_button in splits[1:-1]:
            bits: list[str] = ["0"] * len(light_diagram)

            for num in raw_button[1:-1].split(","):
                bits[int(num)] = "1"

            button_bits.append(bits)
            buttons.append(int("".join(bits), base=2))

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
            # Try every combination of buttons, starting from 1 button
            # and up to all buttons
            for k in range(1, len(buttons) + 1):
                for comb in combinations(buttons, k):
                    status: int = 0

                    for num in comb:
                        status ^= num

                    if status == light:
                        out += k
                        break
                else:  # No valid combination found for this k, jump to next k
                    continue

                break  # Valid combination found for this k, move to next entry

        return out

    def part2(self) -> int:
        """
        Z3 Solver (https://pypi.org/project/z3-solver/) for Integer Linear Programming
        We want to minimize sum(x_i)
        Subject to: A x = b (over Integers)
        x_i >= 0
        """

        out: int = 0

        for _, _, button_bits, joltage_req in self.entries:
            opt = z3.Optimize()

            # Define integer variables
            vars: list = [z3.Int(name=f"x_{jdx}") for jdx in range(len(button_bits))]

            # Non-negative constraint
            for var in vars:
                opt.add(var >= 0)

            # Add linear equation constraints
            for idx, joltage in enumerate(joltage_req):
                # Construct the sum expression for this row
                # A[r] * x = b[r]
                row_expr = 0

                for jdx, col in enumerate(button_bits):
                    if col[idx] == "1":
                        row_expr += vars[jdx]

                opt.add(row_expr == joltage)

            # Objective: Minimize sum of presses
            opt.minimize(z3.Sum(vars))

            if opt.check() == z3.sat:
                model = opt.model()
                out += model.eval(z3.Sum(vars)).as_long()
            else:
                print("No solution found!")

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
