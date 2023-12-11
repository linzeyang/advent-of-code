"""
2023 Day 08
https://adventofcode.com/2023/day/8
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "08.txt"

    def part_one(self) -> int:
        """part one answer"""

        mapping: dict[str, tuple[str, str]] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            instructions = file.readline().strip()

            file.readline()

            while line := file.readline().strip():
                in_node, out_nodes = line.split(" = ")
                out_nodes = tuple(out_nodes.strip("()").split(", "))
                mapping[in_node] = out_nodes

        node = "AAA"
        answer = 0

        while True:
            nexts = mapping[node]
            instruct = instructions[answer % len(instructions)]

            if instruct == "L":
                node = nexts[0]
            else:
                node = nexts[1]

            answer += 1

            if node == "ZZZ":
                break

        return answer

    def part_two(self) -> int:
        """part two answer"""

        mapping: dict[str, tuple[str, str]] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            instructions = file.readline().strip()

            file.readline()

            while line := file.readline().strip():
                in_node, out_nodes = line.split(" = ")
                out_nodes = tuple(out_nodes.strip("()").split(", "))
                mapping[in_node] = out_nodes

        nodes = [node for node in mapping if node[-1] == "A"]
        answer = 0

        while True:
            instruct = instructions[answer % len(instructions)]

            if instruct == "L":
                idx = 0
            else:
                idx = 1

            nodes = [mapping[node][idx] for node in nodes]
            answer += 1

            if all(node[-1] == "Z" for node in nodes):
                break

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
