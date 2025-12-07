"""
day_07.py

Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """Initialize the solution by reading and parsing the input data."""

        self.width: int = 0  # Width of the manifold grid
        self.start_point: int = 0  # Starting position of the tachyon beam (S)

        # Store splitters as sets of column indices for each row that contains them
        self.splitters: list[set[int]] = []

        with DATA_PATH.joinpath("07.txt").open("r", encoding="utf-8") as file:
            # Read first line to get grid dimensions and starting position
            first_line: str = file.readline().strip()
            self.width = len(first_line)
            self.start_point = first_line.index("S")

            # Process remaining lines to find splitter positions
            # Pass the whole line if it doesn't contain any splitter
            for line in file:
                if "^" in line:
                    # Store column indices where splitters are located in this row
                    self.splitters.append(
                        {idx for idx, char in enumerate(line) if char == "^"}
                    )

    def part1(self) -> int:
        """Solve Part 1: Count total number of beam splits.

        Simulates classical beam propagation where each beam continues downward
        and splits into left/right beams when hitting a splitter.
        """

        out: int = 0  # Counter for total splits

        # Track current beam positions (column indices) in the current row
        current: set[int] = {self.start_point}

        # Process each row containing splitters
        for splitter_row in self.splitters:
            # Create new set to track beam positions for the next row
            new_current: set[int] = set()

            # Process each beam position
            for idx in current:
                if idx in splitter_row:
                    # This beam hits a splitter - it splits into two new beams
                    # Add left beam (if within bounds)
                    if idx - 1 >= 0:
                        new_current.add(idx - 1)
                    # Add right beam (if within bounds)
                    if idx + 1 < self.width:
                        new_current.add(idx + 1)
                    # Count this as one split event
                    out += 1
                else:
                    # This beam doesn't hit a splitter - it continues straight down
                    new_current.add(idx)

            # Move to the next row with updated beam positions
            current = new_current

        return out

    def part2(self) -> int:
        """Solve Part 2: Count total number of timelines.

        Uses the many-worlds interpretation where each splitter creates separate
        timelines. Tracks the number of paths leading to each position using
        dynamic programming.
        """

        # Track current beam positions (same as Part 1)
        current: set[int] = {self.start_point}

        # Track number of paths leading to each column position
        # paths[i] = number of different timelines that reach column i
        paths: list[int] = [0] * self.width
        paths[self.start_point] = 1  # Start with one path at the starting position

        # Process each row containing splitters
        for splitter_row in self.splitters:
            # Track new beam positions for the next row
            new_current: set[int] = set()

            # Track new path counts for each position
            new_paths: list[int] = [0] * self.width

            # Process each current beam position
            for idx in current:
                if idx in splitter_row:
                    # This beam hits a splitter - it creates two timelines
                    # Left path: add current path count to left neighbor
                    if idx - 1 >= 0:
                        new_current.add(idx - 1)
                        new_paths[idx - 1] += paths[idx]

                    # Right path: add current path count to right neighbor
                    if idx + 1 < self.width:
                        new_current.add(idx + 1)
                        new_paths[idx + 1] += paths[idx]
                else:
                    # This beam continues straight - preserve its path count
                    new_current.add(idx)
                    new_paths[idx] += paths[idx]

            # Update for next iteration
            current = new_current
            paths = new_paths

        # Return total number of timelines (sum of all possible end positions)
        return sum(paths)


def main() -> None:
    """Main execution function."""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
