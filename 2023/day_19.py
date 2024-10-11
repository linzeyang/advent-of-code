"""
2023 Day 19
https://adventofcode.com/2023/day/19
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "19.sample.txt"

    def part_one(self) -> int:
        """part one answer"""

        rules: dict = {}
        parts = 0
        answer = 0

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    if parts:
                        break
                    else:
                        continue

                line = line.strip()

                if not line.startswith("{"):
                    rule_name, instructs = self._process_rule(line)
                    rules[rule_name] = instructs

                else:
                    parts += 1
                    answer += self._process_part(line, rules)

        return answer

    def _process_rule(self, raw_rule: str) -> tuple[str, list]:
        name, other = raw_rule.split("{")

        instructs = []

        for seg in other[:-1].split(","):
            if ":" in seg:
                instructs.append(tuple(seg.split(":")))
            else:
                instructs.append(seg)

        return name, instructs

    def _process_part(self, raw_part: str, rules: dict[str, list]) -> int:
        part_dict: dict[str, int] = {}

        for seg in raw_part.strip("{}").split(","):
            label, amount = seg.split("=")
            part_dict[label] = int(amount)

        rule = "in"

        while True:
            rule = self._process_part_rule(part_dict, rules[rule])

            if rule == "A":
                return sum(part_dict.values())

            if rule == "R":
                return 0

    def _process_part_rule(self, part_dict: dict[str, int], rule: list) -> str:
        for rul in rule:
            if isinstance(rul, str):
                return rul

            if "<" in rul[0]:
                label, target = rul[0].split("<")

                if part_dict[label] < int(target):
                    return rul[1]
            else:
                label, target = rul[0].split(">")

                if part_dict[label] > int(target):
                    return rul[1]

    def part_two(self) -> int:
        """part two answer"""

        answer = 0
        rules: dict = {}

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                rule_name, rule = self._process_rule(line)
                rules[rule_name] = rule

        pres = []

        for rul in rules["in"]:
            answer += self._calculate(pres, rul, rules)
            if isinstance(rul, tuple):
                pres.append(self._opposite(rul[0]))

        return answer

    def _calculate(self, pres: list, rule, rules: dict) -> int:
        if rule == "R":
            return 0

        if rule == "A":
            return self._calc_conditions(pres)

        if rule[1] == "R":
            return 0

        if rule[1] == "A":
            return self._calc_conditions(pres + [rule[0]])

        ...

    def _opposite(self, pre: str) -> str: ...

    def _calc_conditions(self, pres: list) -> int: ...

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
