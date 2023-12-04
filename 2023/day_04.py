"""
2023 Day 04
https://adventofcode.com/2023/day/4
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "04.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                content = line.split(": ")[1]
                wins, have = content.split(" | ")
                wins = {int(part) for part in wins.split()}
                have = {int(part) for part in have.split()}

                if not (inter := len(wins & have)):
                    continue

                answer += 2 ** (inter - 1)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        mapping: dict[int, int] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                header, content = line.split(": ")
                card_id = int(header.split()[1])

                if card_id not in mapping:
                    mapping[card_id] = 1
                else:
                    mapping[card_id] += 1

                wins, have = content.split(" | ")
                wins = {int(part) for part in wins.split()}
                have = {int(part) for part in have.split()}
                inter = len(wins & have)

                for idx in range(card_id + 1, card_id + 1 + inter):
                    if idx not in mapping:
                        mapping[idx] = mapping[card_id]
                    else:
                        mapping[idx] += mapping[card_id]

        return sum(mapping.values())

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
