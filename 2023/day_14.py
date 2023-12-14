"""
2023 Day 14
https://adventofcode.com/2023/day/14
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "14.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        platform: list[str] = []
        rocks_by_row: dict[int, int] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                platform.append(line)

        num_rows = len(platform)
        num_columns = len(platform[0])

        for idx in range(num_columns):
            column = [row[idx] for row in platform]

            slow = fast = 0

            while fast < num_rows and slow < num_rows:
                if column[slow] == "O":
                    if slow not in rocks_by_row:
                        rocks_by_row[slow] = 1
                    else:
                        rocks_by_row[slow] += 1

                    slow += 1
                elif column[slow] == "#":
                    slow += 1
                else:
                    if fast <= slow:
                        fast = slow + 1
                    elif column[fast] == ".":
                        fast += 1
                    elif column[fast] == "#":
                        slow = fast = fast + 1
                    else:  # fast meets 'O'
                        column[fast] = "."

                        if slow not in rocks_by_row:
                            rocks_by_row[slow] = 1
                        else:
                            rocks_by_row[slow] += 1

                        slow += 1

        for row, rocks in rocks_by_row.items():
            answer += (num_rows - row) * rocks

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        platform: list[list[str]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                platform.append(list(line))

        num_rows = len(platform)
        num_columns = len(platform[0])

        for _ in range(1_000_000_000):
            # north-ward
            for idx in range(num_columns):
                slow = fast = 0

                while fast < num_rows and slow < num_rows:
                    if platform[slow][idx] == "O":
                        slow += 1
                    elif platform[slow][idx] == "#":
                        slow += 1
                    else:
                        if fast <= slow:
                            fast = slow + 1
                        elif platform[fast][idx] == ".":
                            fast += 1
                        elif platform[fast][idx] == "#":
                            slow = fast = fast + 1
                        else:  # fast meets 'O'
                            platform[fast][idx] = "."
                            platform[slow][idx] = "O"

                            slow += 1
            # west-ward
            for idx in range(num_rows):
                slow = fast = 0

                while fast < num_columns and slow < num_columns:
                    if platform[idx][slow] == "O":
                        slow += 1
                    elif platform[idx][slow] == "#":
                        slow += 1
                    else:
                        if fast <= slow:
                            fast = slow + 1
                        elif platform[idx][fast] == ".":
                            fast += 1
                        elif platform[idx][fast] == "#":
                            slow = fast = fast + 1
                        else:  # fast meets 'O'
                            platform[idx][fast] = "."
                            platform[idx][slow] = "O"

                            slow += 1
            # south-ward
            for idx in range(num_columns):
                slow = fast = num_rows - 1

                while fast >= 0 and slow >= 0:
                    if platform[slow][idx] == "O":
                        slow -= 1
                    elif platform[slow][idx] == "#":
                        slow -= 1
                    else:
                        if fast >= slow:
                            fast = slow - 1
                        elif platform[fast][idx] == ".":
                            fast -= 1
                        elif platform[fast][idx] == "#":
                            slow = fast = fast - 1
                        else:  # fast meets 'O'
                            platform[fast][idx] = "."
                            platform[slow][idx] = "O"

                            slow -= 1
            # east-ward
            for idx in range(num_rows):
                slow = fast = num_columns - 1

                while fast >= 0 and slow >= 0:
                    if platform[idx][slow] == "O":
                        slow -= 1
                    elif platform[idx][slow] == "#":
                        slow -= 1
                    else:
                        if fast >= slow:
                            fast = slow - 1
                        elif platform[idx][fast] == ".":
                            fast -= 1
                        elif platform[idx][fast] == "#":
                            slow = fast = fast - 1
                        else:  # fast meets 'O'
                            platform[idx][fast] = "."
                            platform[idx][slow] = "O"

                            slow -= 1

        for idx, row in enumerate(platform):
            answer += row.count("O") * (num_rows - idx)

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
