"""
day_16.py

Day 16: Ticket Translation

https://adventofcode.com/2020/day/16
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.raw_rules: list[str] = []
        self.my_ticket: str = ""
        self.other_tickets: list[str] = []

        with DATA_PATH.joinpath("16.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if "or" in line:
                    self.raw_rules.append(line)
                elif "ticket" in line:
                    continue
                elif not self.my_ticket:
                    self.my_ticket = line
                else:
                    self.other_tickets.append(line)

    def part1(self) -> int:
        """part1"""

        ranges: list[tuple[int, int]] = []

        for raw_rule in self.raw_rules:
            sub_ranges = raw_rule.split(": ")[1].split(" or ")

            for sub_range in sub_ranges:
                start, end = sub_range.split("-")
                ranges.append((int(start), int(end)))

        out = 0

        for ticket in self.other_tickets:
            for num in ticket.split(","):
                num = int(num)

                for start, end in ranges:
                    if start <= num <= end:
                        break
                else:
                    out += num

        return out

    def part2(self) -> int:  # noqa: C901
        """part2"""

        fields: list[str] = []
        ranges: list[tuple[int, int]] = []

        for raw_rule in self.raw_rules:
            field = raw_rule.split(": ")[0]
            fields.append(field)

            sub_ranges = raw_rule.split(": ")[1].split(" or ")

            for sub_range in sub_ranges:
                start, end = sub_range.split("-")
                ranges.append((int(start), int(end)))

        valid_tickets: list[str] = []

        for ticket in self.other_tickets:
            for num in ticket.split(","):
                num = int(num)

                for start, end in ranges:
                    if start <= num <= end:
                        break
                else:
                    break
            else:
                valid_tickets.append(ticket)

        position_candidates: dict[int, set[int]] = {}

        for ticket in valid_tickets:
            for position, num in enumerate(ticket.split(",")):
                num = int(num)

                field_idx_set: set[int] = set()

                for jdx, (start, end) in enumerate(ranges):
                    if start <= num <= end:
                        field_idx_set.add(jdx // 2)

                if position not in position_candidates:
                    position_candidates[position] = field_idx_set
                else:
                    position_candidates[position] &= field_idx_set

        identified_fields: list[tuple[int, int]] = []

        while len(identified_fields) < len(fields):
            positions_to_del: list[int] = []
            field_idx_candidates_to_del: list[int] = []

            for position, candidates in position_candidates.items():
                if len(candidates) > 1:
                    continue

                identified_field_idx = candidates.pop()
                identified_fields.append((position, identified_field_idx))

                positions_to_del.append(position)
                field_idx_candidates_to_del.append(identified_field_idx)

            for position in positions_to_del:
                del position_candidates[position]

            for field_idx_candidate in field_idx_candidates_to_del:
                for candidates in position_candidates.values():
                    if field_idx_candidate in candidates:
                        candidates.remove(field_idx_candidate)

        identified_fields.sort(key=lambda tup: tup[1])

        nums = [int(num) for num in self.my_ticket.split(",")]

        out = 1

        for idx, _ in identified_fields[:6]:
            out *= nums[idx]

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
