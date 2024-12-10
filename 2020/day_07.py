"""
day_07.py

Day 7: Handy Haversacks

https://adventofcode.com/2020/day/7
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.mapping: dict[str, dict[str, int]] = {}

        with DATA_PATH.joinpath("07.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self._construct_mapping(line=line)

    def _construct_mapping(self, line: str) -> None:
        """construct bag -> bag -> count mapping"""

        bag, contents = line.split(" bags contain ")

        self.mapping[bag] = {}

        if "no other bags" in contents:
            return

        contents = contents[:-1]  # remove the peroid (".") at the end of the line

        for content in contents.split(", "):
            parts = content.split(" ")
            content_bag_count = parts[0]
            content_bag = " ".join(parts[1:-1])

            self.mapping[bag][content_bag] = int(content_bag_count)

    def _construct_reverse_mapping(self) -> None:
        """construct reverse mapping (bag -> bags)"""

        self.reverse_mapping: dict[str, list[str]] = {}

        for bag, content_mapping in self.mapping.items():
            for content_bag in content_mapping.keys():
                if content_bag not in self.reverse_mapping:
                    self.reverse_mapping[content_bag] = []

                self.reverse_mapping[content_bag].append(bag)

    def part1(self) -> int:
        """part1"""

        self._construct_reverse_mapping()

        unique_colors = self._get_unique_colors(
            parent_bags=self.reverse_mapping["shiny gold"]
        )

        return len(unique_colors)

    def _get_unique_colors(self, parent_bags: list[str]) -> set:
        """count unique colors"""

        if not parent_bags:
            return set()

        unique_colors = set()

        for bag in parent_bags:
            unique_colors.add(bag)
            unique_colors.update(
                self._get_unique_colors(parent_bags=self.reverse_mapping.get(bag, []))
            )

        return unique_colors

    def part2(self) -> int:
        """part2"""

        return self._count_bags(bag="shiny gold") - 1  # deduct shiny gold bag itself

    def _count_bags(self, bag: str) -> int:
        """count bags"""

        if not (content_mapping := self.mapping[bag]):
            return 1

        return 1 + sum(
            [
                self._count_bags(bag=content_bag) * count
                for content_bag, count in content_mapping.items()
            ]
        )


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
