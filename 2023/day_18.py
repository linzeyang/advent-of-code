"""
2023 Day 18
https://adventofcode.com/2023/day/18
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "18.txt"

    def part_one(self) -> int:
        """part one answer"""

        line_mapping: dict[int, list[int]] = {0: [0]}

        current = (0, 0)

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                direct, steps, _ = line.split(" ")

                if direct == "R":
                    line_mapping[current[1]].extend(
                        current[0] + idx for idx in range(1, int(steps) + 1)
                    )
                    current = (current[0] + int(steps), current[1])
                elif direct == "L":
                    line_mapping[current[1]].extend(
                        current[0] - idx for idx in range(1, int(steps) + 1)
                    )
                    current = (current[0] - int(steps), current[1])
                elif direct == "U":
                    for idx in range(1, int(steps) + 1):
                        if current[1] + idx not in line_mapping:
                            line_mapping[current[1] + idx] = [current[0]]
                        else:
                            line_mapping[current[1] + idx].append(current[0])
                    current = (current[0], current[1] + int(steps))
                else:
                    for idx in range(1, int(steps) + 1):
                        if current[1] - idx not in line_mapping:
                            line_mapping[current[1] - idx] = [current[0]]
                        else:
                            line_mapping[current[1] - idx].append(current[0])
                    current = (current[0], current[1] - int(steps))

        line_mapping[0].pop()
        matrix: list[list[int]] = []

        for line_no in sorted(line_mapping.keys()):
            line = [0] * 382

            for coord in line_mapping[line_no]:
                line[coord + 17] = 1

            matrix.append(line)

        points = [(208, 1)]

        while points:
            temp = []
            for point in points:
                if matrix[point[1] - 1][point[0]] == 0:
                    matrix[point[1] - 1][point[0]] = 1
                    temp.append((point[0], point[1] - 1))
                if matrix[point[1] + 1][point[0]] == 0:
                    matrix[point[1] + 1][point[0]] = 1
                    temp.append((point[0], point[1] + 1))
                if matrix[point[1]][point[0] - 1] == 0:
                    matrix[point[1]][point[0] - 1] = 1
                    temp.append((point[0] - 1, point[1]))
                if matrix[point[1]][point[0] + 1] == 0:
                    matrix[point[1]][point[0] + 1] = 1
                    temp.append((point[0] + 1, point[1]))
            points = temp

        answer = 0

        for line in matrix:
            answer += line.count(1)

        return answer

    def part_two(self) -> int:
        """part two answer"""

        current = (0, 0)
        edges: list[tuple[tuple[int, int], tuple[int, int]]] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                _, _, instruct = line.split(" ")

                steps = int(instruct[2:7], base=16)
                direct = int(instruct[7])

                if direct == 0:
                    direct = "R"
                elif direct == 1:
                    direct = "D"
                elif direct == 2:
                    direct = "L"
                else:
                    direct = "U"

                if direct == "R":
                    dest = (current[0] + int(steps), current[1])
                elif direct == "L":
                    dest = (current[0] - int(steps), current[1])
                elif direct == "U":
                    dest = (current[0], current[1] + int(steps))
                else:
                    dest = (current[0], current[1] - int(steps))

                edges.append((current, dest))

                current = dest

        answer = 0

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
