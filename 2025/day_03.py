"""
day_03.py

Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.banks: list[tuple[int, ...]] = []

        with DATA_PATH.joinpath("03.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.banks.append(tuple(int(char) for char in line.strip()))

    def part1(self) -> int:
        """part1"""

        out: int = 0

        for bank in self.banks:
            # Precompute the max value to the right of each index (suffix max)
            # largest_seen[i] will store the max value in bank[len(bank)-1-i:]
            largest_seen: list[int] = []

            for battery in bank[::-1]:
                if not largest_seen:
                    largest_seen.append(battery)
                else:
                    largest_seen.append(max(battery, largest_seen[-1]))

            candidate: int = 0

            # Iterate through each possible first digit
            for idx in range(len(bank) - 1):
                # bank[idx] is the tens digit;
                # largest_seen[-idx - 2] corresponds to max(bank[idx+1:])
                # which is the ones digit
                candidate = max(candidate, bank[idx] * 10 + largest_seen[-idx - 2])

            out += candidate

        return out

    def part2(self) -> int:
        """part2"""

        out: int = 0

        for bank in self.banks:
            # Map each digit (0-9) to a list of its indices for O(1) lookup
            digits_mapping: dict[int, list[int]] = {}

            for idx, digit in enumerate(bank):
                if digit not in digits_mapping:
                    digits_mapping[digit] = []

                digits_mapping[digit].append(idx)

            joltage: int = 0
            lower_bound: int = 0
            upper_bound: int = len(bank)

            # Greedily construct the 12-digit number from left to right
            for position in range(1, 13):
                # Update upper bound to ensure enough digits remain
                # for subsequent positions
                upper_bound = len(bank) - 12 + position

                # Try digits from 9 down to 1 to maximize the current position
                for candidate in range(9, 0, -1):
                    if candidate not in digits_mapping:
                        continue

                    breaked = False

                    # Find the first valid occurrence of the candidate digit
                    for jdx in digits_mapping[candidate]:
                        if lower_bound <= jdx < upper_bound:
                            lower_bound = jdx + 1
                            joltage = joltage * 10 + candidate
                            breaked = True
                            break

                    if breaked:
                        break

            out += joltage

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
