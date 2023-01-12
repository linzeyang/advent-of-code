"""
2022 Day 10
https://adventofcode.com/2022/day/10
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "10.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0
        x = 1
        accumulated_cycles = 0

        check_point_cycles = [20, 60, 100, 140, 180, 220]

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                if line.startswith("addx"):
                    increment = int(line.split()[-1])

                    if (
                        expected_cycles := accumulated_cycles + 2
                    ) in check_point_cycles:
                        answer += x * expected_cycles
                    elif expected_cycles in [cycle + 1 for cycle in check_point_cycles]:
                        answer += x * (expected_cycles - 1)

                    x += increment
                    accumulated_cycles += 2
                else:
                    if (
                        expected_cycles := accumulated_cycles + 1
                    ) in check_point_cycles:
                        answer += x * expected_cycles
                    accumulated_cycles += 1

        return answer

    def part_two(self) -> str:
        """part two answer"""

        x = 1
        accumulated_cycles = 0
        on_screen: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                if line.startswith("addx"):
                    if x - 1 <= accumulated_cycles % 40 <= x + 1:
                        on_screen.append("#")
                    else:
                        on_screen.append(".")

                    if x - 2 <= accumulated_cycles % 40 <= x:
                        on_screen.append("#")
                    else:
                        on_screen.append(".")

                    x += int(line.split()[-1])
                    accumulated_cycles += 2
                else:
                    if x - 1 <= accumulated_cycles % 40 <= x + 1:
                        on_screen.append("#")
                    else:
                        on_screen.append(".")

                    accumulated_cycles += 1

        temp = []

        i = 0
        while seg := on_screen[i : i + 40]:
            temp.append("".join(seg))
            i += 40

        return "\n".join(temp)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ \n{self.part_two()}\n ]]")


if __name__ == "__main__":
    Solution().print_answers()
