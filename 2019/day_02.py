"""
day_02.py

Day 02: 1202 Program Alarm

https://adventofcode.com/2019/day/2
"""

from itertools import product
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("02.txt").open("r", encoding="utf-8") as file:
            self.program: list[int] = list(map(int, file.readline().strip().split(",")))

    def _get_output(self, noun: int, verb: int) -> int:
        """Run a program from initial state with customized 'noun' and 'verb'"""

        program: list[int] = self.program.copy()

        program[1] = noun
        program[2] = verb

        idx: int = 0

        while idx < len(program):
            opcode: int = program[idx]

            match opcode:
                case 99:
                    break
                case 1 | 2:
                    in_1_pos: int = program[idx + 1]
                    in_2_pos: int = program[idx + 2]
                    out_pos: int = program[idx + 3]

                    match opcode:
                        case 1:
                            program[out_pos] = program[in_1_pos] + program[in_2_pos]
                        case 2:
                            program[out_pos] = program[in_1_pos] * program[in_2_pos]
                case _:
                    raise ValueError(f"Unknown opcode {opcode} at position {idx}")

            idx += 4

        return program[0]

    def part1(self) -> int:
        """part1"""

        return self._get_output(noun=12, verb=2)

    def part2(self) -> int:
        """part2"""

        target: int = 19690720

        for noun, verb in product(range(100), range(100)):
            if self._get_output(noun=noun, verb=verb) == target:
                return noun * 100 + verb

        raise ValueError("No noun/verb pair produces the target output")


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
