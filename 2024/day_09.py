"""
day_09.py

Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.disk_map: str = ""

        with DATA_PATH.joinpath("09.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.disk_map = line.strip()

    def part1(self) -> int:  # noqa: C901
        """part1"""

        # 1. decompress the dense disk map to a list
        self.disk_part_1: list = []

        file_id: int = 0

        for idx, char in enumerate(self.disk_map):
            if idx & 1 == 0:  # file
                if char == "0":
                    continue

                self.disk_part_1.extend([file_id] * int(char))

                file_id += 1
            elif char != "0":  # free space
                self.disk_part_1.extend(["."] * int(char))

        # 2. move file blocks ahead (exchange file and free space blocks)
        left = self.disk_part_1.index(".")

        for r_idx in range(len(self.disk_part_1) - 1, -1, -1):
            if self.disk_part_1[r_idx] != ".":
                break

        right = r_idx

        while left < right:
            if self.disk_part_1[left] != ".":
                left += 1
                continue

            if self.disk_part_1[right] == ".":
                right -= 1
                continue

            self.disk_part_1[left], self.disk_part_1[right] = (
                self.disk_part_1[right],
                self.disk_part_1[left],
            )
            left += 1
            right -= 1

        # 3. calculate the checksum
        checksum: int = 0

        for idx in range(len(self.disk_part_1)):
            if self.disk_part_1[idx] == ".":
                break

            checksum += self.disk_part_1[idx] * idx

        return checksum

    def part2(self) -> int:  # noqa: C901
        """part2"""

        # 1. decompress the dense disk map to a list
        self.disk_part_2: list = []

        # [file_id, start_idx, length]
        file_blocks: list[list[int]] = []

        # [start_idx, length]
        free_space_blocks: list[list[int]] = []

        file_id: int = 0

        for idx, char in enumerate(self.disk_map):
            if idx & 1 == 0:  # file
                if char == "0":
                    continue

                file_blocks.append([file_id, len(self.disk_part_2), int(char)])

                self.disk_part_2.extend([file_id] * int(char))

                file_id += 1
            elif char != "0":  # free space
                free_space_blocks.append([len(self.disk_part_2), int(char)])

                self.disk_part_2.extend(["."] * int(char))

        # 2. move file blocks ahead (exchange file and free space blocks)
        for right_idx in range(len(file_blocks) - 1, -1, -1):
            file_id, file_block_start_idx, file_block_length = file_blocks[right_idx]

            for left_idx in range(len(free_space_blocks)):
                free_space_start_idx, free_space_length = free_space_blocks[left_idx]

                if free_space_start_idx > file_block_start_idx:
                    break

                if free_space_length < file_block_length:
                    continue

                self.disk_part_2[
                    free_space_start_idx : free_space_start_idx + file_block_length
                ] = [int(file_id)] * file_block_length

                self.disk_part_2[
                    file_block_start_idx : file_block_start_idx + file_block_length
                ] = ["."] * file_block_length

                free_space_blocks[left_idx] = [
                    free_space_start_idx + file_block_length,
                    free_space_length - file_block_length,
                ]

                break

        # 3. calculate the checksum
        checksum: int = 0

        for idx in range(len(self.disk_part_2)):
            if self.disk_part_2[idx] == ".":
                continue

            checksum += self.disk_part_2[idx] * idx

        return checksum


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
