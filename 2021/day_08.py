"""
day_08.py

Day 8: Seven Segment Search

https://adventofcode.com/2025/day/8
"""

from collections import defaultdict
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.rows: list[tuple[str, ...]] = []

        with DATA_PATH.joinpath("08.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.rows.append(tuple(line.strip().split(" | ")))

    def part1(self) -> int:
        """part1"""

        out: int = 0

        for row in self.rows:
            _, output = row

            for segment in output.split(" "):
                if len(segment) in (2, 3, 4, 7):
                    out += 1

        return out

    def part2(self) -> int:
        """part2"""

        out: int = 0

        for row in self.rows:
            out += self._decipher(row)

        return out

    def _decipher(self, row: tuple[str, ...]) -> int:
        """decipher"""

        mapping: defaultdict[int, list[str]] = defaultdict(list)

        for segment in row[0].split(" "):
            mapping[len(segment)].append(segment)

        # one has length 2
        one: frozenset[str] = frozenset(mapping[2][0])
        # four has length 4
        four: frozenset[str] = frozenset(mapping[4][0])

        mapping2: dict[frozenset[str], int] = {
            one: 1,
            four: 4,
            frozenset(mapping[3][0]): 7,  # seven has length 3
            frozenset(mapping[7][0]): 8,  # eight has length 7
        }

        for segment in mapping[6]:
            # six and one have 1 segment in common
            if len(set(segment) & one) < 2:
                mapping2[frozenset(segment)] = 6
            # zero and four have 3 segments in common
            elif len(set(segment) & four) == 3:
                mapping2[frozenset(segment)] = 0
            # nine and four have 4 segments in common
            elif len(set(segment) & four) == 4:
                mapping2[frozenset(segment)] = 9

        for segment in mapping[5]:
            # two and four have 2 segments in common
            if len(set(segment) & four) == 2:
                mapping2[frozenset(segment)] = 2
            # three and one have 2 segments in common
            elif len(set(segment) & one) == 2:
                mapping2[frozenset(segment)] = 3
            # five and one have 1 segment in common
            else:
                mapping2[frozenset(segment)] = 5

        out: int = 0

        for segment in row[1].split(" "):
            out = out * 10 + mapping2[frozenset(segment)]

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
