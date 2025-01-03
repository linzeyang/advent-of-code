"""
day_13.py

Day 13: Claw Contraption

https://adventofcode.com/2024/day/13


An additional library is used in the solutions:

```bash
pip install sympy==1.13.1
```
"""

from pathlib import Path

from sympy import Eq, solve, symbols

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.parameters_list: list[list[int]] = []

        parameters: list[int] = []

        with DATA_PATH.joinpath("13.txt").open("r", encoding="utf-8") as file:
            for line in file:
                if line == "\n":
                    self.parameters_list.append(parameters)
                    parameters = []
                else:
                    parts = line.strip().split(", ")

                    if "+" in parts[0]:
                        parameters.append(int(parts[0].split("+")[-1]))
                        parameters.append(int(parts[1].split("+")[-1]))
                    else:
                        parameters.append(int(parts[0].split("=")[-1]))
                        parameters.append(int(parts[1].split("=")[-1]))

        if parameters:
            self.parameters_list.append(parameters)

    def part1(self) -> int:
        """part1"""

        out = 0

        for parameters in self.parameters_list:
            sol_x, sol_y = self._solve_1(parameters)

            if sol_x == -1 or sol_y == -1:
                continue

            out += sol_x * 3 + sol_y

        return out

    def _solve_1(self, parameters: list[int]) -> tuple[int, int]:
        """solve 1"""

        x, y = symbols("x y")

        eq1 = Eq(parameters[0] * x + parameters[2] * y, parameters[4])
        eq2 = Eq(parameters[1] * x + parameters[3] * y, parameters[5])

        solution = solve((eq1, eq2), (x, y))

        sol_x, sol_y = solution[x], solution[y]

        if sol_x % 1 != 0 or sol_y % 1 != 0 or sol_x > 100 or sol_y > 100:
            return -1, -1

        return sol_x, sol_y

    def part2(self) -> int:
        """part2"""

        out = 0

        for parameters in self.parameters_list:
            sol_x, sol_y = self._solve_2(parameters)

            if sol_x == -1 or sol_y == -1:
                continue

            out += sol_x * 3 + sol_y

        return out

    def _solve_2(self, parameters: list[int]) -> tuple[int, int]:
        """solve 2"""

        x, y = symbols("x y")

        eq1 = Eq(parameters[0] * x + parameters[2] * y, parameters[4] + 1e13)
        eq2 = Eq(parameters[1] * x + parameters[3] * y, parameters[5] + 1e13)

        solution = solve((eq1, eq2), (x, y))

        sol_x, sol_y = solution[x], solution[y]

        if sol_x % 1 != 0 or sol_y % 1 != 0:
            return -1, -1

        return sol_x, sol_y


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
