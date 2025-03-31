"""
day_21.py

Day 21: Allergen Assessment

https://adventofcode.com/2020/day/21
"""

from collections import defaultdict
from functools import reduce
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.lines: list[str] = []
        self.distinct_allergens: set[str] = set()
        self.allergents_appearances: dict[str, list[int]] = defaultdict(list)

        with DATA_PATH.joinpath("21.txt").open("r", encoding="utf-8") as file:
            for line in file:
                left, right = line.strip().split(" (contains ")

                for allergent in right[:-1].split(", "):
                    self.distinct_allergens.add(allergent)
                    self.allergents_appearances[allergent].append(len(self.lines))

                self.lines.append(left)

        self.allergents_candidates_mapping: dict[str, set[str]] = {}

    def part1(self) -> int:
        """part1"""

        ingredients_with_allergens: set[str] = set()

        for allergent in self.distinct_allergens:
            candidates = reduce(
                lambda x, y: x & y,
                [
                    set(self.lines[line_idx].split(" "))
                    for line_idx in self.allergents_appearances[allergent]
                ],
            )

            ingredients_with_allergens |= candidates

            self.allergents_candidates_mapping[allergent] = candidates

        out = 0

        for line in self.lines:
            out += len(set(line.split(" ")) - ingredients_with_allergens)

        return out

    def part2(self) -> str:
        """part2"""

        confirmed_allergents: dict[str, str] = {}

        while len(confirmed_allergents) < len(self.distinct_allergens):
            allergents_to_del = []
            ingredients_to_del = []

            for allergent, candidates in self.allergents_candidates_mapping.items():
                if len(candidates) == 1:
                    allergents_to_del.append(allergent)

                    ingredient = candidates.pop()
                    ingredients_to_del.append(ingredient)

                    confirmed_allergents[allergent] = ingredient

            for allergent in allergents_to_del:
                del self.allergents_candidates_mapping[allergent]

            for ingredients in self.allergents_candidates_mapping.values():
                ingredients -= set(ingredients_to_del)

        return ",".join(
            item[1] for item in sorted(confirmed_allergents.items(), key=lambda x: x[0])
        )


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
