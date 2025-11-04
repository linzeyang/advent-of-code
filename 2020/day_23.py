"""
day_23.py

Day 23: Crab Cups

https://adventofcode.com/2020/day/23
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("23.txt").open("r", encoding="utf-8") as file:
            self.raw_input: str = file.readline().strip()

        self.initial_state: tuple[int] = tuple(int(c) for c in self.raw_input)

    def part1(self) -> str:
        """part1

        Simulates the Crab Cups game for 100 moves with the initial 9 cups.

        Algorithm:
        1. Start with current cup (first cup in input)
        2. For each move (100 total):
           - Pick up 3 cups immediately clockwise of current cup
           - Find destination cup (current label-1, wrapping 1→9, skipping picked cups)
           - Place picked cups immediately clockwise of destination cup
           - Move current cup to next clockwise position
        3. After 100 moves, return cup labels clockwise from cup 1 (excluding cup 1)

        Uses list operations since only 9 cups make O(n) operations acceptable.
        """

        state: list[int] = list(self.initial_state)

        current_idx: int = 0
        current_value: int = state[current_idx]

        for _ in range(100):
            next_a: int = state[(current_idx + 1) % 9]
            next_b: int = state[(current_idx + 2) % 9]
            next_c: int = state[(current_idx + 3) % 9]

            for val in (next_a, next_b, next_c):
                state.remove(val)

            destination: int = current_value - 1

            if destination < 1:
                destination = 9

            while destination in (next_a, next_b, next_c):
                destination -= 1

                if destination < 1:
                    destination = 9

            destination_idx: int = state.index(destination)

            state.insert(destination_idx + 1, next_a)
            state.insert(destination_idx + 2, next_b)
            state.insert(destination_idx + 3, next_c)

            current_idx = (state.index(current_value) + 1) % 9
            current_value = state[current_idx]

        return "".join(
            str(state[(state.index(1) + offset) % 9]) for offset in range(1, 9)
        )

    def part2(self) -> int:
        """
        part2

        Optimized solution using a dictionary-based linked list to handle 1 million cups
        and 10 million moves efficiently.
        Uses cup -> next_cup mapping for O(1) operations.
        """

        LENGTH = 1_000_000
        MOVES = 10_000_000

        # Use a dictionary to represent the linked list: cup -> next_cup
        cups: dict[int, int] = {}

        # Build the initial linked list from the input
        initial_cups: list[int] = list(self.initial_state)

        # Link the initial cups
        for i in range(len(initial_cups) - 1):
            cups[initial_cups[i]] = initial_cups[i + 1]

        # Link the last initial cup to the first extended cup (10)
        cups[initial_cups[-1]] = 10

        # Link the extended cups (10 to 1,000,000)
        for i in range(10, LENGTH):
            cups[i] = i + 1

        # Link the last cup back to the first cup to complete the circle
        cups[LENGTH] = initial_cups[0]

        # Start with the first cup from input
        current: int = initial_cups[0]

        for _ in range(MOVES):
            # Pick up the next 3 cups
            picked_up_1: int = cups[current]
            picked_up_2: int = cups[picked_up_1]
            picked_up_3: int = cups[picked_up_2]

            # Remove the picked up cups from the circle
            cups[current] = cups[picked_up_3]

            # Find destination cup
            destination: int = current - 1

            if destination < 1:
                destination = LENGTH

            # Skip the picked up cups
            while destination in (picked_up_1, picked_up_2, picked_up_3):
                destination -= 1

                if destination < 1:
                    destination = LENGTH

            # Insert the picked up cups after the destination
            cups[picked_up_3] = cups[destination]
            cups[destination] = picked_up_1

            # Move to the next current cup
            current = cups[current]

        # Find the two cups after cup 1
        cup_after_1: int = cups[1]
        cup_after_2: int = cups[cup_after_1]

        return cup_after_1 * cup_after_2


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
