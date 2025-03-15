"""
day_14.py

Day 14: Docking Data

https://adventofcode.com/2020/day/14
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.lines: list[str] = []

        with DATA_PATH.joinpath("14.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.lines.append(line.strip())

    def part1(self) -> int:
        """part1"""

        memory: dict[int, int] = {}

        mask: list[tuple[int, str]] = []

        for line in self.lines:
            if line.startswith("mask"):
                mask = self._convert_mask(line)
            else:
                addr, value = self._convert_value(mask, line)

                memory[addr] = value

        return sum(memory.values())

    def _convert_mask(self, line: str) -> list[tuple[int, str]]:
        raw_mask = line.split(" = ")[1]

        out: list[tuple[int, str]] = []

        for idx, char in enumerate(raw_mask):
            if char == "X":
                continue

            out.append((idx, char))

        return out

    def _convert_value(self, mask: list[tuple[int, str]], line: str) -> tuple[int, int]:
        raw_addr, raw_value = line.split("] = ")

        addr = int(raw_addr[4:])

        value_bin_list = list(f"{int(raw_value):0>36b}")

        for idx, char in mask:
            value_bin_list[idx] = char

        return addr, int("".join(value_bin_list), base=2)

    def part2(self) -> int:
        """part2"""

        memory: dict[int, int] = {}

        mask: list[tuple[int, str]] = []

        for line in self.lines:
            if line.startswith("mask"):
                mask = self._convert_mask_2(line)
            else:
                addrs, value = self._convert_value_2(mask, line)

                for addr in addrs:
                    memory[addr] = value

        return sum(memory.values())

    def _convert_mask_2(self, line: str) -> list[tuple[int, str]]:
        raw_mask = line.split(" = ")[1]

        return [(idx, char) for idx, char in enumerate(raw_mask)]

    def _convert_value_2(
        self, mask: list[tuple[int, str]], line: str
    ) -> tuple[list[int], int]:
        raw_addr, raw_value = line.split("] = ")

        addr_bin_list = list(f"{int(raw_addr[4:]):0>36b}")

        x_idxs: list[int] = []

        for idx, char in mask:
            if char != "0":
                addr_bin_list[idx] = char

                if char == "X":
                    x_idxs.append(idx)

        num_of_x = len(x_idxs)

        addrs: list[int] = []

        for i in range(2**num_of_x):
            i_bin_list = list(f"{i:0>{num_of_x}b}")

            for idx, char in zip(x_idxs, i_bin_list, strict=True):
                addr_bin_list[idx] = char

            addrs.append(int("".join(addr_bin_list), base=2))

        return addrs, int(raw_value)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
