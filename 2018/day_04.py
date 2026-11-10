"""
day_04.py

Day 4: Repose Record

https://adventofcode.com/2018/day/4
"""

from collections import Counter
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("04.txt").open("r", encoding="utf-8") as file:
            records: list[str] = [line.strip() for line in file]

        records.sort()

        self.guards: dict[int, list[list[int]]] = {}

        guard_id: int = -1

        for record in records:
            if "Guard" in record:
                guard_id = int(record.split("Guard #")[-1].split(" begins")[0])

                if guard_id not in self.guards:
                    self.guards[guard_id] = []
            else:
                minute: int = int(record.split("] ")[0].split(":")[-1])

                if "asleep" in record:
                    self.guards[guard_id].append([minute, -1])
                else:
                    self.guards[guard_id][-1][-1] = minute

    def part1(self) -> int:
        """part1"""

        max_id: int = -1
        max_total_minutes: int = -1

        for guard_id, slots in self.guards.items():
            total_minutes: int = sum(end - start for start, end in slots)

            if total_minutes > max_total_minutes:
                max_id = guard_id
                max_total_minutes = total_minutes

        minute_count: Counter[int] = Counter()

        for start, end in self.guards[max_id]:
            for minute in range(start, end):
                minute_count[minute] += 1

        minute_at_max_frequency: int = minute_count.most_common(1)[0][0]

        return max_id * minute_at_max_frequency

    def part2(self) -> int:
        """part2"""

        max_id: int = -1
        max_frequency: int = -1
        minute_at_max_frequency: int = -1

        for guard_id, slots in self.guards.items():
            minute_count: Counter[int] = Counter()

            for start, end in slots:
                for minute in range(start, end):
                    minute_count[minute] += 1

            if not minute_count:
                continue

            max_minute, max_minute_count = minute_count.most_common(1)[0]

            if max_minute_count > max_frequency:
                max_id = guard_id
                max_frequency = max_minute_count
                minute_at_max_frequency = max_minute

        return max_id * minute_at_max_frequency


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
