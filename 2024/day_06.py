"""
day_06.py

Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Direction(Enum):
    """Guard movement directions"""

    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def turn_right(self) -> Direction:
        """Get the direction after turning right"""

        directions: list[Direction] = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT,
        ]
        current_idx: int = directions.index(self)
        return directions[(current_idx + 1) % 4]


@dataclass(frozen=True)
class Position:
    """Position in the grid"""

    row: int
    col: int

    def move(self, direction: Direction) -> Position:
        """Get the position after moving in the given direction"""

        dr, dc = direction.value
        return Position(self.row + dr, self.col + dc)


class Grid:
    """Represents the lab grid with obstacles"""

    def __init__(self, obstacles: set[Position], rows: int, cols: int) -> None:
        self.obstacles = obstacles
        self.rows = rows
        self.cols = cols

    def is_obstacle(self, pos: Position) -> bool:
        """Check if there's an obstacle at the given position"""

        return pos in self.obstacles

    def is_in_bounds(self, pos: Position) -> bool:
        """Check if the position is within grid bounds"""

        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols


class Solution:
    def __init__(self) -> None:
        """Initialize the solution with grid data"""

        self.grid: Grid
        self.start_pos: Position
        self._parse_input()

    def _parse_input(self) -> None:
        """Parse the input file to create grid and find starting position"""

        obstacles: set[Position] = set()
        start_pos: Position = Position(0, 0)  # placeholder

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            lines: list[str] = [line.strip() for line in file]

        rows: int = len(lines)
        cols: int = len(lines[0]) if lines else 0

        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line):
                if char == "#":
                    obstacles.add(Position(row_idx, col_idx))
                elif char == "^":
                    start_pos = Position(row_idx, col_idx)

        self.grid: Grid = Grid(obstacles, rows, cols)
        self.start_pos: Position = start_pos

    def part1(self) -> int:
        """Simulate guard movement and count visited positions"""

        visited: set[Position] = set()
        current_pos: Position = self.start_pos
        direction: Direction = Direction.UP

        while self.grid.is_in_bounds(current_pos):
            visited.add(current_pos)

            # Try to move forward
            next_pos = current_pos.move(direction)

            if not self.grid.is_in_bounds(next_pos):
                break

            if self.grid.is_obstacle(next_pos):
                # Turn right if obstacle ahead
                direction = direction.turn_right()
            else:
                # Move forward
                current_pos = next_pos

        return len(visited)

    def part2(self) -> int:
        """Find positions where placing an obstacle creates a loop"""

        original_path = self._get_original_path()

        # Only test positions on the original path (excluding start)
        return sum(
            1
            for pos in original_path
            if pos != self.start_pos and self._creates_loop(pos)
        )

    def _get_original_path(self) -> set[Position]:
        """Get the original path by simulating guard movement step by step"""

        visited = set()
        current_pos = self.start_pos
        direction = Direction.UP

        while self.grid.is_in_bounds(current_pos):
            visited.add(current_pos)

            # Try to move forward
            next_pos = current_pos.move(direction)

            if not self.grid.is_in_bounds(next_pos):
                break

            if self.grid.is_obstacle(next_pos):
                # Turn right if obstacle ahead
                direction = direction.turn_right()
            else:
                # Move forward
                current_pos = next_pos

        return visited

    def _creates_loop(self, obstacle_pos: Position) -> bool:
        """Check if placing an obstacle at the given position creates a loop"""

        # Create a temporary grid with the additional obstacle
        temp_obstacles: set[Position] = self.grid.obstacles | {obstacle_pos}
        temp_grid = Grid(temp_obstacles, self.grid.rows, self.grid.cols)

        current_pos = self.start_pos
        direction = Direction.UP

        # Track visited states (position + direction) to detect loops
        visited_states = set()

        while temp_grid.is_in_bounds(current_pos):
            state = (current_pos, direction)
            if state in visited_states:
                # Found a loop!
                return True

            visited_states.add(state)

            # Try to move forward
            next_pos = current_pos.move(direction)

            if not temp_grid.is_in_bounds(next_pos):
                break

            if temp_grid.is_obstacle(next_pos):
                # Turn right if obstacle ahead
                direction = direction.turn_right()
            else:
                # Move forward
                current_pos = next_pos

        return False


def main() -> None:
    """Run the solution and print results"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
