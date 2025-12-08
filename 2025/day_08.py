"""
day_08.py

Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import heapq
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.points: list[tuple[int, ...]] = []

        # Read puzzle input: each line is an X,Y,Z coordinate for a junction box
        with DATA_PATH.joinpath("08.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.points.append(tuple(int(num) for num in line.strip().split(",")))

    def part1(self) -> int:
        """part1"""

        length: int = len(self.points)
        # Number of attempts to process:
        # exactly 1000 globally-shortest pairs (including no-ops)
        K = 1_000
        # Min-heap of edges: (squared_distance, i, j).
        # Use squared distance to avoid expensive sqrt.
        queue: list[tuple[int, int, int]] = []

        heapq.heapify(queue)

        for idx in range(length - 1):
            for jdx in range(idx + 1, length):
                sqr_distance: int = sum(
                    (self.points[idx][kdx] - self.points[jdx][kdx]) ** 2
                    for kdx in range(3)
                )
                heapq.heappush(queue, (sqr_distance, idx, jdx))

        # circuits: list of lists storing node indices in each circuit (component)
        circuits: list[list[int]] = []
        # mapping: node index -> circuits list index
        mapping: dict[int, int] = {}

        # Process exactly K shortest edges in ascending order
        for _ in range(K):
            _, idx, jdx = heapq.heappop(queue)

            # Both endpoints unseen: create a new circuit with the two nodes
            if idx not in mapping and jdx not in mapping:
                circuits.append([idx, jdx])
                mapping[idx] = len(circuits) - 1
                mapping[jdx] = len(circuits) - 1
            # Attach idx to jdx's circuit
            elif idx not in mapping:
                circuits[mapping[jdx]].append(idx)
                mapping[idx] = mapping[jdx]
            # Attach jdx to idx's circuit
            elif jdx not in mapping:
                circuits[mapping[idx]].append(jdx)
                mapping[jdx] = mapping[idx]
            # IMPORTANT: Both seen and in different circuits: merge circuits (union)
            elif mapping[idx] != mapping[jdx]:
                circuits[mapping[idx]].extend(circuits[mapping[jdx]])

                original_mapping_jdx: int = mapping[jdx]

                # Update mapping for all nodes moved into idx's circuit
                for item in circuits[mapping[jdx]]:
                    mapping[item] = mapping[idx]

                # Mark the absorbed circuit as empty (retained to keep indices stable)
                circuits[original_mapping_jdx] = []

        # Compute sizes for all circuits (empty lists contribute size 0)
        top_3: list[int] = sorted((len(circuit) for circuit in circuits), reverse=True)[
            :3
        ]

        return top_3[0] * top_3[1] * top_3[2]

    def part2(self) -> int:
        """part2"""

        length: int = len(self.points)
        # Build the same global edge heap: (squared_distance, i, j),
        # ascending by distance
        queue: list[tuple[int, int, int]] = []

        heapq.heapify(queue)

        for idx in range(length - 1):
            for jdx in range(idx + 1, length):
                sqr_distance: int = sum(
                    (self.points[idx][kdx] - self.points[jdx][kdx]) ** 2
                    for kdx in range(3)
                )
                heapq.heappush(queue, (sqr_distance, idx, jdx))

        # Part 2 uses effective merges only: skip edges within the same circuit
        circuits: list[list[int]] = []
        mapping: dict[int, int] = {}
        # Track the number of current circuits; starting from n singletons,
        # each effective union reduces by 1
        num_real_circuits: int = 1_000

        while queue:
            _, idx, jdx = heapq.heappop(queue)

            # Both unseen: create a new circuit with the two nodes
            # (reduces circuit count by 1)
            if idx not in mapping and jdx not in mapping:
                circuits.append([idx, jdx])
                mapping[idx] = len(circuits) - 1
                mapping[jdx] = len(circuits) - 1

                num_real_circuits -= 1
            # Attach idx into jdx's circuit (reduces circuit count by 1)
            elif idx not in mapping:
                circuits[mapping[jdx]].append(idx)
                mapping[idx] = mapping[jdx]

                num_real_circuits -= 1
            # Attach jdx into idx's circuit (reduces circuit count by 1)
            elif jdx not in mapping:
                circuits[mapping[idx]].append(jdx)
                mapping[jdx] = mapping[idx]

                num_real_circuits -= 1
            # Merge two different circuits (effective union, reduces circuit count by 1)
            elif mapping[idx] != mapping[jdx]:
                circuits[mapping[idx]].extend(circuits[mapping[jdx]])

                original_mapping_jdx = mapping[jdx]
                for item in circuits[mapping[jdx]]:
                    mapping[item] = mapping[idx]
                circuits[original_mapping_jdx] = []

                num_real_circuits -= 1

            # When all nodes are in a single circuit,
            # return product of X coordinates of the last effective connection
            if num_real_circuits == 1:
                return self.points[idx][0] * self.points[jdx][0]


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
