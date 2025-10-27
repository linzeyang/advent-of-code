"""
2023 Day 03
https://adventofcode.com/2023/day/3
"""

from pathlib import Path

SYMBOLS = {"/", "@", "&", "+", "%", "#", "$", "=", "*", "-"}


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "03.txt"

    def part_one(self) -> int:
        """part one answer"""

        answer = 0

        matrix: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

        height = len(matrix)
        width = len(matrix[0])

        for idx in range(height):
            found_digit = False
            adjacent_to_symbol = False
            number = 0

            for jdx in range(width):
                if not matrix[idx][jdx].isdigit():
                    if found_digit:
                        if adjacent_to_symbol:
                            answer += number
                        adjacent_to_symbol = False
                        found_digit = False
                        number = 0
                    continue

                if not found_digit:
                    found_digit = True

                number = number * 10 + int(matrix[idx][jdx])

                if (
                    (
                        0 <= idx - 1 < height
                        and 0 <= jdx - 1 < width
                        and matrix[idx - 1][jdx - 1] in SYMBOLS
                    )
                    or (
                        0 <= idx - 1 < height
                        and 0 <= jdx < width
                        and matrix[idx - 1][jdx] in SYMBOLS
                    )
                    or (
                        0 <= idx - 1 < height
                        and 0 <= jdx + 1 < width
                        and matrix[idx - 1][jdx + 1] in SYMBOLS
                    )
                    or (
                        0 <= idx < height
                        and 0 <= jdx - 1 < width
                        and matrix[idx][jdx - 1] in SYMBOLS
                    )
                    or (
                        0 <= idx < height
                        and 0 <= jdx + 1 < width
                        and matrix[idx][jdx + 1] in SYMBOLS
                    )
                    or (
                        0 <= idx + 1 < height
                        and 0 <= jdx - 1 < width
                        and matrix[idx + 1][jdx - 1] in SYMBOLS
                    )
                    or (
                        0 <= idx + 1 < height
                        and 0 <= jdx < width
                        and matrix[idx + 1][jdx] in SYMBOLS
                    )
                    or (
                        0 <= idx + 1 < height
                        and 0 <= jdx + 1 < width
                        and matrix[idx + 1][jdx + 1] in SYMBOLS
                    )
                ):
                    adjacent_to_symbol = True

            if found_digit and adjacent_to_symbol:
                answer += number

        return answer

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        matrix: list[str] = []

        gears: dict[tuple[int, int], list[int]] = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)

        height = len(matrix)
        width = len(matrix[0])

        for idx in range(height):
            found_digit = False
            adjacent_to_symbol = False
            symbol_positions: set[tuple[int, int]] = set()
            number = 0

            for jdx in range(width):
                if not matrix[idx][jdx].isdigit():
                    if found_digit:
                        if adjacent_to_symbol:
                            for position in symbol_positions:
                                if position not in gears:
                                    gears[position] = [number]
                                else:
                                    gears[position].append(number)
                        adjacent_to_symbol = False
                        symbol_positions = set()
                        found_digit = False
                        number = 0
                    continue

                if not found_digit:
                    found_digit = True

                number = number * 10 + int(matrix[idx][jdx])

                if (
                    0 <= idx - 1 < height
                    and 0 <= jdx - 1 < width
                    and matrix[idx - 1][jdx - 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx - 1, jdx - 1))
                if (
                    0 <= idx - 1 < height
                    and 0 <= jdx < width
                    and matrix[idx - 1][jdx] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx - 1, jdx))
                if (
                    0 <= idx - 1 < height
                    and 0 <= jdx + 1 < width
                    and matrix[idx - 1][jdx + 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx - 1, jdx + 1))
                if (
                    0 <= idx < height
                    and 0 <= jdx - 1 < width
                    and matrix[idx][jdx - 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx, jdx - 1))
                if (
                    0 <= idx < height
                    and 0 <= jdx + 1 < width
                    and matrix[idx][jdx + 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx, jdx + 1))
                if (
                    0 <= idx + 1 < height
                    and 0 <= jdx - 1 < width
                    and matrix[idx + 1][jdx - 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx + 1, jdx - 1))
                if (
                    0 <= idx + 1 < height
                    and 0 <= jdx < width
                    and matrix[idx + 1][jdx] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx + 1, jdx))
                if (
                    0 <= idx + 1 < height
                    and 0 <= jdx + 1 < width
                    and matrix[idx + 1][jdx + 1] == "*"
                ):
                    adjacent_to_symbol = True
                    symbol_positions.add((idx + 1, jdx + 1))

            if found_digit and adjacent_to_symbol:
                for position in symbol_positions:
                    if position not in gears:
                        gears[position] = [number]
                    else:
                        gears[position].append(number)

        for numbers in gears.values():
            if len(numbers) == 2:
                answer += numbers[0] * numbers[1]

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
