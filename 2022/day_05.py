"""
2022 Day 05
https://adventofcode.com/2022/day/5
"""

from pathlib import Path


def perform_task_1(
    stacks, number_of_crates: int, from_stack: int, to_stack: int
) -> None:
    stacks[to_stack].extend(stacks[from_stack][-1 : -number_of_crates - 1 : -1])
    stacks[from_stack] = stacks[from_stack][:-number_of_crates]


def perform_task_2(
    stacks, number_of_crates: int, from_stack: int, to_stack: int
) -> None:
    stacks[to_stack].extend(stacks[from_stack][-number_of_crates:])
    stacks[from_stack] = stacks[from_stack][:-number_of_crates]


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "05.txt"

    def part_one(self) -> str:
        """part one answer"""

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            crates_part: list[str] = []

            while (line := file.readline()) != "\n":
                crates_part.append(line)

            number_of_stacks = len(crates_part[-1].split())
            stacks = {n + 1: [] for n in range(number_of_stacks)}

            for line in crates_part[-2::-1]:
                for i in range(number_of_stacks):
                    if (char := line[1 + 4 * i]) != " ":
                        stacks[i + 1].append(char)

            while line := file.readline().strip():
                tokens = line.split()
                perform_task_1(
                    stacks,
                    number_of_crates=int(tokens[1]),
                    from_stack=int(tokens[3]),
                    to_stack=int(tokens[5]),
                )

        return "".join(stack[-1] for stack in stacks.values())

    def part_two(self) -> str:
        """part two answer"""

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            crates_part: list[str] = []

            while (line := file.readline()) != "\n":
                crates_part.append(line)

            number_of_stacks = len(crates_part[-1].split())
            stacks = {n + 1: [] for n in range(number_of_stacks)}

            for line in crates_part[-2::-1]:
                for i in range(number_of_stacks):
                    if (char := line[1 + 4 * i]) != " ":
                        stacks[i + 1].append(char)

            while line := file.readline().strip():
                tokens = line.split()
                perform_task_2(
                    stacks,
                    number_of_crates=int(tokens[1]),
                    from_stack=int(tokens[3]),
                    to_stack=int(tokens[5]),
                )

        return "".join(stack[-1] for stack in stacks.values())

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
