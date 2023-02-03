"""
2021 Day 03
https://adventofcode.com/2021/day/3
"""

from collections import defaultdict
from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "03.txt"

    def part_one(self) -> int:
        """part one answer"""

        num_of_lines = 0
        bit_one_by_column = defaultdict(int)

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                num_of_lines += 1

                for idx, char in enumerate(line):
                    if char == "1":
                        bit_one_by_column[idx] += 1

        gamma_rate_bits: list[str] = []
        epsilon_rate_bits: list[str] = []

        for idx, count in sorted(bit_one_by_column.items()):
            if count > num_of_lines // 2:
                gamma_rate_bits.append("1")
                epsilon_rate_bits.append("0")
            else:
                gamma_rate_bits.append("0")
                epsilon_rate_bits.append("1")

        return int("".join(gamma_rate_bits), base=2) * int(
            "".join(epsilon_rate_bits), base=2
        )

    def part_two(self) -> int:
        """part two answer"""

        num_of_lines = 0

        lines_with_zero_start: list[list[str]] = []
        lines_with_one_start: list[list[str]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                num_of_lines += 1

                if line.startswith("0"):
                    lines_with_zero_start.append(list(line))
                else:
                    lines_with_one_start.append(list(line))

        # print(lines_with_one_start, lines_with_zero_start)

        if len(lines_with_zero_start) > num_of_lines / 2:
            oxy_list = lines_with_zero_start
            co2_list = lines_with_one_start
        else:
            oxy_list = lines_with_one_start
            co2_list = lines_with_zero_start

        num_of_bits = len(oxy_list[0])

        for i in range(1, num_of_bits):
            zero_list = []
            one_list = []

            for line in oxy_list:
                if line[i] == "0":
                    zero_list.append(line)
                else:
                    one_list.append(line)

            if len(zero_list) > (len(zero_list) + len(one_list)) / 2:
                oxy_list = zero_list
            else:
                oxy_list = one_list

            if len(oxy_list) == 1:
                break

        for i in range(1, num_of_bits):
            zero_list = []
            one_list = []

            for line in co2_list:
                if line[i] == "0":
                    zero_list.append(line)
                else:
                    one_list.append(line)

            if len(zero_list) > (len(zero_list) + len(one_list)) / 2:
                co2_list = one_list
            else:
                co2_list = zero_list

            if len(co2_list) == 1:
                break

        return int("".join(oxy_list[0]), base=2) * int("".join(co2_list[0]), base=2)

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
