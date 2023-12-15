"""
2023 Day 15
https://adventofcode.com/2023/day/15
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "15.txt"

    def part_one(self) -> int:
        """part one answer"""

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            instructions = file.readline().strip().split(",")

        answer = 0

        for instruct in instructions:
            answer += self._hash(sequence=instruct)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            instructions = file.readline().strip().split(",")

        answer = 0

        box_lens_mapping: dict[int, dict[str, int]] = {}

        for instruct in instructions:
            if instruct[-1].isdigit():
                label, num = instruct.split("=")
                num = int(num)

                box_no = self._hash(sequence=label)

                if box_no not in box_lens_mapping:
                    box_lens_mapping[box_no] = {label: num}
                else:
                    box_lens_mapping[box_no][label] = num
            else:
                label = instruct[:-1]

                box_no = self._hash(sequence=label)

                if (
                    box_no not in box_lens_mapping
                    or label not in box_lens_mapping[box_no]
                ):
                    continue

                del box_lens_mapping[box_no][label]

        for box_no, lenss in box_lens_mapping.items():
            for idx, num in enumerate(lenss.values()):
                answer += (box_no + 1) * (idx + 1) * num

        return answer

    @staticmethod
    def _hash(sequence: str) -> int:
        number = 0

        for char in sequence:
            number = (number + ord(char)) * 17 % 256

        return number

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
