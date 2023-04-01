"""
2020 Day 1
https://adventofcode.com/2020/day/1
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data/01.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0
        target = 2020
        nums: list[int] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                nums.append(int(line))

        nums.sort()

        head = 0
        tail = len(nums) - 1

        while head < tail:
            if nums[head] + nums[tail] == target:
                answer = nums[head] * nums[tail]
                break

            if nums[head] + nums[tail] > target:
                tail -= 1
                continue

            head += 1

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0
        target = 2020
        nums: list[int] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                nums.append(int(line))

        nums.sort()

        for idx, num in enumerate(nums):
            others = self._helper(nums[idx + 1 :], target - num)

            if others[0] != -1:
                answer = num * others[0] * others[1]
                break

        return answer

    def _helper(self, nums: list[int], target: int) -> tuple[int, int]:
        head = 0
        tail = len(nums) - 1

        while head < tail:
            if nums[head] + nums[tail] == target:
                return nums[head], nums[tail]

            if nums[head] + nums[tail] > target:
                tail -= 1
            else:
                head += 1

        return -1, -1

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
