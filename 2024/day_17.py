"""
day_17.py

Day 17: Chronospatial Computer

https://adventofcode.com/2024/day/17
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.registers: list[int] = [0, 0, 0]
        self.programs: list[str] = []

        with DATA_PATH.joinpath("17.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

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

        pos = 0

        while pos < len(self.programs):
            instruct = self.programs[pos]

            operand = self.programs[pos + 1]

            operand_literal = int(operand)

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
        return  pos + 2 if not self.registers[0] else number

    def _do_bdv(self, number: int) -> None:
        self.registers[1] = int(self.registers[0] / (2**number))

    def _do_cdv(self, number: int) -> None:
        self.registers[2] = int(self.registers[0] / (2**number))

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
