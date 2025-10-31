"""
day_17.py

Day 17: Chronospatial Computer

https://adventofcode.com/2024/day/17
"""

import time
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.registers: list[int] = [0, 0, 0]
        self.programs: list[str] = []

        with DATA_PATH.joinpath("17.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line: str = line.strip()

                if line.startswith("Register A"):
                    self.registers[0] = int(line.split(" ")[2])
                elif line.startswith("Register B"):
                    self.registers[1] = int(line.split(" ")[2])
                elif line.startswith("Register C"):
                    self.registers[2] = int(line.split(" ")[2])
                elif line.startswith("Program"):
                    self.programs = line.split(" ")[1].split(",")

    def part1(self) -> str:  # noqa: C901
        """part1"""

        out: list[str] = []
        pos: int = 0

        while pos < len(self.programs):
            instruct: str = self.programs[pos]
            operand: str = self.programs[pos + 1]
            operand_literal: int = int(operand)

            if "0" <= operand <= "3":
                operand_combo = int(operand)
            elif operand == "4":
                operand_combo = self.registers[0]
            elif operand == "5":
                operand_combo = self.registers[1]
            elif operand == "6":
                operand_combo = self.registers[2]

            match instruct:
                case "0":
                    self._do_adv(number=operand_combo)
                case "1":
                    self._do_bxl(number=operand_literal)
                case "2":
                    self._do_bst(number=operand_combo)
                case "3":
                    pos = self._do_jnz(pos=pos, number=operand_literal)
                case "4":
                    self._do_bxc()
                case "5":
                    out.append(str(self._do_out(number=operand_combo)))
                case "6":
                    self._do_bdv(number=operand_combo)
                case "7":
                    self._do_cdv(number=operand_combo)

            pos += 2 if instruct != "3" else 0

        return ",".join(out)

    def _do_adv(self, number: int) -> None:
        self.registers[0] = int(self.registers[0] / (2**number))

    def _do_bxl(self, number: int) -> None:
        self.registers[1] ^= number

    def _do_bxc(self) -> None:
        self.registers[1] ^= self.registers[2]

    def _do_out(self, number: int) -> int:
        return number % 8

    def _do_bst(self, number: int) -> None:
        self.registers[1] = number % 8

    def _do_jnz(self, pos: int, number: int) -> int:
        return pos + 2 if not self.registers[0] else number

    def _do_bdv(self, number: int) -> None:
        self.registers[1] = int(self.registers[0] / (2**number))

    def _do_cdv(self, number: int) -> None:
        self.registers[2] = int(self.registers[0] / (2**number))

    def part2(self) -> int:
        """part2 - Reverse engineering approach"""

        start_time: float = time.perf_counter()

        # Target output should be the program itself
        target_output: list[int] = [int(x) for x in self.programs]

        print(f"Looking for A value that makes program output: {target_output}")
        print("Analyzing program structure...")

        # Let's analyze what the program does:
        # 2,4: bst 4 -> B = A % 8
        # 1,1: bxl 1 -> B = B ^ 1
        # 7,5: cdv 5 -> C = A // (2^B)
        # 1,4: bxl 4 -> B = B ^ 4
        # 0,3: adv 3 -> A = A // 8
        # 4,5: bxc   -> B = B ^ C
        # 5,5: out 5 -> output B % 8
        # 5,5: out 5 -> output B % 8 (duplicate)
        # 3,0: jnz 0 -> if A != 0, jump to start

        print("-----------------")
        print("Program analysis:")
        print("- Takes A % 8, XORs with 1, then 4")
        print("- Uses result to shift A right by that amount into C")
        print("- XORs B with C, outputs B % 8")
        print("- Divides A by 8 and repeats")
        print("-----------------")

        # Use reverse engineering: build A from right to left
        # Since A gets divided by 8 each iteration, we can build it by
        # trying each possible 3-bit value (0-7) for each position

        def find_a_recursive(
            target_remaining: list[int], current_a: int = 0
        ) -> int | None:
            if not target_remaining:
                return current_a

            # We need to find what 3-bit value to add to current_a
            # to produce the next output value
            target_digit: int = target_remaining[-1]  # Work backwards

            for candidate_bits in range(8):  # Try all 3-bit values (0-7)
                test_a: int = (current_a << 3) | candidate_bits

                # Simulate one iteration of the program with this A
                output_digit: int = self._simulate_one_iteration(test_a)

                if output_digit == target_digit:
                    # This candidate works, recurse for remaining digits
                    result: int | None = find_a_recursive(target_remaining[:-1], test_a)

                    if result is not None:
                        return result

            return

        result: int | None = find_a_recursive(target_output)

        elapsed: float = time.perf_counter() - start_time

        if result is not None:
            print(f"Found solution A={result} in {elapsed:.4f} seconds")
            return result

        print(f"No solution found with reverse engineering in {elapsed:.4f}s")
        return -1

    def _simulate_one_iteration(self, a_value: int) -> int:
        """Simulate one iteration of the program to get the output digit"""

        # Based on program analysis:
        # 2,4: B = A % 8
        # 1,1: B = B ^ 1
        # 7,5: C = A // (2^B)
        # 1,4: B = B ^ 4
        # 0,3: A = A // 8  (this happens at end, doesn't affect output)
        # 4,5: B = B ^ C
        # 5,5: output B % 8

        b = a_value % 8
        b = b ^ 1
        c = a_value >> b  # A // (2^B) is same as A >> B
        b = b ^ 4
        b = b ^ c

        return b % 8


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
