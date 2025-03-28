"""
day_19.py

Day 19: Monster Messages

https://adventofcode.com/2020/day/19
"""

import re
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.raw_rules: dict[str, str] = {}
        self.messages: list[str] = []

        with DATA_PATH.joinpath("19.txt").open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if ":" in line:
                    self.raw_rules[line.split(": ")[0]] = line.split(": ")[1]
                elif line:
                    self.messages.append(line)

    def part1(self) -> int:
        """part1"""

        rule_0 = self._construct_rule("0")

        pattern = re.compile(f"^{rule_0}$")

        return sum(1 for message in self.messages if pattern.fullmatch(message))

    def _construct_rule(self, rule_id: str) -> str:
        """Construct a rule from its rule id, eg. "12" -> "(a|b)" """

        rule_content = self.raw_rules[rule_id]

        if rule_content == '"a"':
            return "a"

        if rule_content == '"b"':
            return "b"

        if "|" in rule_content:
            left, right = rule_content.split(" | ")

            if " " in left:
                left = self._construct_rule(left.split()[0]) + self._construct_rule(
                    left.split()[1]
                )
            else:
                left = self._construct_rule(left)

            if " " in right:
                right = self._construct_rule(right.split()[0]) + self._construct_rule(
                    right.split()[1]
                )
            else:
                right = self._construct_rule(right)

            return "(" + left + "|" + right + ")"

        if " " in rule_content:
            return self._construct_rule(rule_content.split()[0]) + self._construct_rule(
                rule_content.split()[1]
            )

        return self._construct_rule(rule_content)

    def part2(self) -> int:
        """part2"""

        rule_42 = self._construct_rule("42")
        rule_31 = self._construct_rule("31")

        rule_8 = rule_42 + "+"
        rule_11 = (
            "("
            + rule_42
            + rule_31
            + "|"
            + rule_42 * 2
            + rule_31 * 2
            + "|"
            + rule_42 * 3
            + rule_31 * 3
            + "|"
            + rule_42 * 4
            + rule_31 * 4
            + "|"
            + rule_42 * 5
            + rule_31 * 5
            + ")"
        )

        rule_0 = rule_8 + rule_11

        pattern = re.compile(f"^{rule_0}$")

        return sum(1 for message in self.messages if pattern.fullmatch(message))


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
