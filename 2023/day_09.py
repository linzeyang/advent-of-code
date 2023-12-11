"""
2023 Day 09
https://adventofcode.com/2023/day/9
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "09.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                nums = [int(part) for part in line.split(" ")]
                summ = nums[-1]
                all_zero = all(num == 0 for num in nums)

                while not all_zero:
                    nums = [nums[idx] - nums[idx - 1] for idx in range(1, len(nums))]
                    summ += nums[-1]
                    all_zero = all(num == 0 for num in nums)

                answer += summ

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                nums = [int(part) for part in line.split(" ")]
                summ = nums[0]
                sign = -1
                all_zero = all(num == 0 for num in nums)

                while not all_zero:
                    nums = [nums[idx] - nums[idx - 1] for idx in range(1, len(nums))]
                    summ += nums[0] * sign
                    sign *= -1
                    all_zero = all(num == 0 for num in nums)

                answer += summ

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
