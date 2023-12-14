"""
2023 Day 13
https://adventofcode.com/2023/day/13
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "13.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            pattern: list[str] = []
            refs: list[int] = []

            while line := file.readline():
                if line == "\n":
                    line_no, is_horizontal = self._find_mirror(
                        pattern=pattern, refs=refs
                    )
                    answer += line_no * 100 if is_horizontal else line_no

                    pattern = []
                    refs = []

                    continue

                line = line.strip()

                if pattern and line == pattern[-1]:
                    refs.append(len(pattern) - 1)

                pattern.append(line)

        return answer

    def _find_mirror(self, pattern: list[str], refs: list[int]) -> tuple[int, bool]:
        if not refs:
            return self._find_vertical_mirror(pattern), False

        for ref in refs:
            rang = min(ref, len(pattern) - ref - 2)

            for idx in range(rang):
                if pattern[ref - idx - 1] != pattern[ref + idx + 2]:
                    break
            else:
                return ref + 1, True

        return self._find_vertical_mirror(pattern), False

    def _find_vertical_mirror(self, pattern: list[str]) -> int:
        columns: list[str] = []
        refs: list[int] = []

        for idx in range(len(pattern[0])):
            column = "".join(line[idx] for line in pattern)

            if columns and column == columns[-1]:
                refs.append(len(columns) - 1)

            columns.append(column)

        for ref in refs:
            rang = min(ref, len(columns) - ref - 2)

            for idx in range(rang):
                if columns[ref - idx - 1] != columns[ref + idx + 2]:
                    break
            else:
                return ref + 1

        return 0

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            pattern: list[str] = []
            refs: list[tuple[int, int]] = []

            while line := file.readline():
                if line == "\n":
                    line_no, is_horizontal = self._find_mirror_2(
                        pattern=pattern, refs=refs
                    )
                    answer += line_no * 100 if is_horizontal else line_no

                    pattern = []
                    refs = []

                    continue

                line = line.strip()

                if pattern:
                    if line == pattern[-1]:
                        refs.append((len(pattern) - 1, 0))
                    elif self._line_similar(line, pattern[-1]):
                        refs.append((len(pattern) - 1, 1))

                pattern.append(line)

        return answer

    @staticmethod
    def _line_similar(line1: str, line2: str) -> bool:
        diff = 0

        for idx, char in enumerate(line1):
            if char != line2[idx]:
                diff += 1

            if diff > 1:
                return False

        return True

    def _find_mirror_2(
        self, pattern: list[str], refs: list[tuple[int, int]]
    ) -> tuple[int, bool]:
        if not refs:
            return self._find_vertical_mirror_2(pattern), False

        for ref, diffs in refs:
            rang = min(ref, len(pattern) - ref - 2)

            for idx in range(rang):
                if pattern[ref - idx - 1] == pattern[ref + idx + 2]:
                    continue
                elif self._line_similar(pattern[ref - idx - 1], pattern[ref + idx + 2]):
                    diffs += 1
                    if diffs > 1:
                        break
                else:
                    break
            else:
                if diffs == 1:
                    return ref + 1, True

        return self._find_vertical_mirror_2(pattern), False

    def _find_vertical_mirror_2(self, pattern: list[str]) -> int:
        columns: list[str] = []
        refs: list[tuple[int, int]] = []

        for idx in range(len(pattern[0])):
            column = "".join(line[idx] for line in pattern)

            if columns:
                if column == columns[-1]:
                    refs.append((len(columns) - 1, 0))
                elif self._line_similar(column, columns[-1]):
                    refs.append((len(columns) - 1, 1))

            columns.append(column)

        for ref, diffs in refs:
            rang = min(ref, len(columns) - ref - 2)

            for idx in range(rang):
                if columns[ref - idx - 1] == columns[ref + idx + 2]:
                    continue
                elif self._line_similar(columns[ref - idx - 1], columns[ref + idx + 2]):
                    diffs += 1
                    if diffs > 1:
                        break
                else:
                    break
            else:
                if diffs == 1:
                    return ref + 1

        return 0

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
