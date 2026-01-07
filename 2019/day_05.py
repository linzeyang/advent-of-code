"""
day_05.py

Day 5: Sunny with a Chance of Asteroids

https://adventofcode.com/2019/day/5
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("05.txt").open("r", encoding="utf-8") as file:
            self.program: list[int] = list(map(int, file.readline().strip().split(",")))

    def _get_output(self, _input: int) -> int:
        """Run a program from initial state with customized '_input'"""

        out: int = 0

        program: list[int] = self.program.copy()

        idx: int = 0

        while idx < len(program):
            header: str = f"{program[idx]:0>4}"
            position_mode: str = header[:2]
            opcode: int = int(header[2:])

            p1_mode: str = position_mode[-1]
            p2_mode: str = position_mode[-2]

            match opcode:
                case 99:  # Halt
                    break
                case 1 | 2 | 7 | 8:
                    p1: int = (
                        program[program[idx + 1]]
                        if p1_mode == "0"
                        else program[idx + 1]
                    )

                    p2: int = (
                        program[program[idx + 2]]
                        if p2_mode == "0"
                        else program[idx + 2]
                    )

                    out_pos: int = program[idx + 3]

                    match opcode:
                        case 1:  # Add
                            program[out_pos] = p1 + p2
                        case 2:  # Multiply
                            program[out_pos] = p1 * p2
                        case 7:  # Less than
                            program[out_pos] = int(p1 < p2)
                        case 8:  # Equals
                            program[out_pos] = int(p1 == p2)

                    idx += 4
                case 3:  # Input
                    out_pos: int = program[idx + 1]

                    program[out_pos] = _input

                    idx += 2
                case 4:  # Output
                    p1: int = (
                        program[program[idx + 1]]
                        if p1_mode == "0"
                        else program[idx + 1]
                    )

                    out = p1

                    idx += 2
                case 5 | 6:
                    p1: int = (
                        program[program[idx + 1]]
                        if p1_mode == "0"
                        else program[idx + 1]
                    )

                    p2: int = (
                        program[program[idx + 2]]
                        if p2_mode == "0"
                        else program[idx + 2]
                    )

                    match opcode:
                        case 5:  # Jump-if-true
                            if p1:
                                idx = p2
                            else:
                                idx += 3
                        case 6:  # Jump-if-false
                            if not p1:
                                idx = p2
                            else:
                                idx += 3
                case _:
                    raise ValueError(f"Unknown opcode {opcode} at position {idx}")

        return out

    def part1(self) -> int:
        """part1"""

        return self._get_output(_input=1)

    def part2(self) -> int:
        """part2"""

        return self._get_output(_input=5)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
