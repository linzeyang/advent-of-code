"""
day_08.py

Day 8: Handheld Halting

https://adventofcode.com/2020/day/8
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.instructions: list[tuple[str, ...]] = []

        with DATA_PATH.joinpath("08.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                self.instructions.append(tuple(line.split()))

    def part1(self) -> int:
        """part1"""

        accumulator = idx = 0

        executed_idx: set[int] = set()

        while idx not in executed_idx:
            executed_idx.add(idx)

            instruction, argument = self.instructions[idx]

            match instruction:
                case "acc":
                    accumulator += int(argument)
                    idx += 1
                case "jmp":
                    idx += int(argument)
                case "nop":
                    idx += 1

        return accumulator

    def part2(self) -> int:
        """part2"""

        alt_instructions = self.instructions[:]
        alt_idx = 0
        last_alt_idx = -1
        last_alt_instruction = ("", "")

        while alt_idx < len(alt_instructions):
            alt_instruction = alt_instructions[alt_idx]

            if alt_instruction == "acc":
                continue

            if last_alt_idx >= 0:
                alt_instructions[last_alt_idx] = last_alt_instruction

            last_alt_idx = alt_idx
            last_alt_instruction = alt_instruction

            if alt_instruction[0] == "nop":
                alt_instructions[alt_idx] = ("jmp", alt_instruction[1])
            else:
                alt_instructions[alt_idx] = ("nop", alt_instruction[1])

            valid, accu = self._do_traverse(instructions=alt_instructions)

            if valid:
                break

            alt_idx += 1

        return accu

    def _do_traverse(self, instructions) -> tuple[bool, int]:
        accumulator = idx = 0

        executed_idx: set[int] = set()

        while idx < len(instructions):
            if idx in executed_idx:
                return False, accumulator

            executed_idx.add(idx)

            instruction, argument = instructions[idx]

            match instruction:
                case "acc":
                    accumulator += int(argument)
                    idx += 1
                case "jmp":
                    idx += int(argument)
                case "nop":
                    idx += 1

        return True, accumulator


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
