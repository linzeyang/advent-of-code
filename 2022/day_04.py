"""
2022 Day 04
https://adventofcode.com/2022/day/4
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
                zones = line.split(",")
                zone1_low, zone1_high = (int(num) for num in zones[0].split("-"))
                zone2_low, zone2_high = (int(num) for num in zones[1].split("-"))

                if (zone1_low <= zone2_low and zone1_high >= zone2_high) or (
                    zone1_low >= zone2_low and zone1_high <= zone2_high
                ):
                    answer += 1

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                zones = line.split(",")
                zone1_low, zone1_high = (int(num) for num in zones[0].split("-"))
                zone2_low, zone2_high = (int(num) for num in zones[1].split("-"))

                if not zone1_high < zone2_low and not zone2_high < zone1_low:
                    answer += 1

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
