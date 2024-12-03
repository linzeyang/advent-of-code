"""
day_04.py

Day 4: Passport Processing

https://adventofcode.com/2020/day/4
"""

from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

ALL_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.passports: list[dict[str, str]] = []

        with DATA_PATH.joinpath("04.txt").open("r", encoding="utf-8") as file:
            passport: dict[str, str] = {}

            for line in file:
                line = line.strip()

                if not line:
                    self.passports.append(passport)
                    passport = {}
                else:
                    for segment in line.split():
                        key, value = segment.split(":")
                        passport[key] = value

        if passport:
            self.passports.append(passport)

    def part1(self) -> int:
        """part1"""

        num_of_valid = 0

        for passport in self.passports:
            if (ALL_FIELDS - set(passport.keys())) in (set(), {"cid"}):
                num_of_valid += 1

        return num_of_valid

    def part2(self) -> int:
        """part2"""

        num_of_valid = 0

        for passport in self.passports:
            if (ALL_FIELDS - set(passport.keys())) not in (set(), {"cid"}):
                continue

            if self._validate_passport(passport=passport):
                num_of_valid += 1

        return num_of_valid

    def _validate_passport(self, passport: dict[str, str]) -> bool:  # noqa: C901
        """validate passsport for part 2"""

        byr = passport["byr"]

        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            return False

        iyr = passport["iyr"]

        if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
            return False

        eyr = passport["eyr"]

        if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
            return False

        hgt = passport["hgt"]

        if passport["hgt"][-2:] not in ("cm", "in"):
            return False

        hgt_int = int(hgt[:-2])

        if hgt.endswith("cm") and (hgt_int < 150 or hgt_int > 193):
            return False

        if hgt.endswith("in") and (hgt_int < 59 or hgt_int > 76):
            return False

        hcl = passport["hcl"]

        if len(hcl) != 7 or not hcl.startswith("#"):
            return False

        try:
            int(hcl[1:], base=16)
        except ValueError:
            return False

        if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            return False

        pid = passport["pid"]

        if len(pid) != 9 or not all(digit.isdigit() for digit in pid):
            return False

        return True


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
