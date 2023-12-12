"""
2023 Day 10
https://adventofcode.com/2023/day/10
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "10.txt"

    def part_one(self) -> int:
        """part one answer"""
        
        matrix: list[str] = []
        
        s_x = s_y = -1

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                matrix.append(line)
                if "S" in line:
                    s_y = len(matrix) - 1
                    s_x = line.index("S")
                    
        left_x, left_y, left_dir = s_x, s_y - 1, 1
        right_x, right_y, right_dir = s_x - 1, s_y, 2

        answer = 1
        
        while left_x != right_x or left_y != right_y:
            left_x, left_y, left_dir = self._get_next(left_x, left_y, left_dir, matrix)
            right_x, right_y, right_dir = self._get_next(right_x, right_y, right_dir, matrix)
            
            answer += 1

        return answer
    
    def _get_next(self, cord_x: int, cord_y: int, dir: int, matrix: list[str]) -> tuple[int, int, int]:
        point = matrix[cord_y][cord_x]
        
        if point == "-":
            if dir == 2:
                return cord_x - 1, cord_y, 2
            else:
                return cord_x + 1, cord_y, 0
        elif point == "|":
            if dir == 1:
                return cord_x, cord_y - 1, 1
            else:
                return cord_x, cord_y + 1, 3
        elif point == "L":
            if dir == 2:
                return cord_x, cord_y - 1, 1
            else:
                return cord_x + 1, cord_y, 0
        elif point == "J":
            if dir == 3:
                return cord_x - 1, cord_y, 2
            else:
                return cord_x, cord_y - 1, 1
        elif point == "7":
            if dir == 0:
                return cord_x, cord_y + 1, 3
            else:
                return cord_x - 1, cord_y, 2
        else:
            if dir == 2:
                return cord_x, cord_y + 1, 3
            else:
                return cord_x + 1, cord_y, 0

    def part_two(self) -> int:
        """part two answer"""

        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                ...

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
