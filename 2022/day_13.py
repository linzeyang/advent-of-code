"""
2022 Day 13
https://adventofcode.com/2022/day/13
"""

import ast
from functools import cmp_to_key
from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "13.txt"

    def __init__(self) -> None:
        self.storage: list[list[list]] = []
        self.flattened_storage: list[list] = []

    def _compare_two_items(self, item_a: int | list, item_b: int | list) -> int:
        if isinstance(item_a, int) and isinstance(item_b, int):
            return -1 if item_a < item_b else 0 if item_a == item_b else 1

        if isinstance(item_a, list) and isinstance(item_b, list):
            length_a, length_b = len(item_a), len(item_b)

            for idx in range(min(length_a, length_b)):
                if (temp := self._compare_two_items(item_a[idx], item_b[idx])) in {
                    -1,
                    1,
                }:
                    return temp

            if length_a < length_b:
                return -1
            if length_a > length_b:
                return 1
            return 0

        if isinstance(item_a, int):
            item_a = [item_a]
        elif isinstance(item_b, int):
            item_b = [item_b]

        return self._compare_two_items(item_a, item_b)

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        temp: list[list] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line.strip():
                    temp.append(ast.literal_eval(line.strip()))
                else:
                    self.storage.append(temp)
                    temp = []

        if temp:
            self.storage.append(temp)

        for idx, (list_a, list_b) in enumerate(self.storage):
            if self._compare_two_items(list_a, list_b) == -1:
                answer += idx + 1

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 1

        for lis in self.storage:
            self.flattened_storage.extend(lis)

        self.flattened_storage.append([[2]])
        self.flattened_storage.append([[6]])

        self.flattened_storage.sort(key=cmp_to_key(self._compare_two_items))

        for idx, lis in enumerate(self.flattened_storage):
            if lis in ([[2]], [[6]]):
                answer *= idx + 1

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
