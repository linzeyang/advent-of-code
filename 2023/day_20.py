"""
2023 Day 20
https://adventofcode.com/2023/day/20
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "20.txt"

    def part_one(self) -> int:
        """part one answer"""

        module_mapping: dict[str, dict] = {}
        initials: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                if line.startswith("broadcaster"):
                    initials = line.split(" -> ")[1].split(", ")
                    continue

                parts = line.split(" -> ")

                if line.startswith("%"):
                    module_mapping[parts[0][1:]] = {
                        "type": "%",
                        "status": 0,
                        "targets": parts[1].split(", "),
                    }
                else:
                    module_mapping[parts[0][1:]] = {
                        "type": "&",
                        "sources": [],
                        "status": [],
                        "targets": parts[1].split(", "),
                    }

        for module_name, module_dict in module_mapping.items():
            for module in module_dict["targets"]:
                if module not in module_mapping:
                    continue
                if module_mapping[module]["type"] == "&":
                    module_mapping[module]["sources"].append(module_name)
                    module_mapping[module]["status"].append(0)

        num_low = num_high = 0

        for _ in range(1000):
            delta_low, delta_high = self._process(module_mapping, initials)
            num_low += delta_low
            num_high += delta_high

        answer = num_low * num_high

        return answer

    def _process(
        self, module_mapping: dict[str, dict], modules: list[str]
    ) -> tuple[int, int]:
        num_low, num_high = 1 + len(modules), 0

        intermediates = [(module, 0, "") for module in modules]

        while intermediates:
            temp_intermediates: list[tuple[str, int, str]] = []

            for module, status, source in intermediates:
                if module_mapping[module]["type"] == "%":
                    if status:
                        continue

                    status = int(not module_mapping[module]["status"])

                    module_mapping[module]["status"] = status
                else:
                    status_idx = module_mapping[module]["sources"].index(source)

                    module_mapping[module]["status"][status_idx] = status

                    status = int(not all(module_mapping[module]["status"]))

                if status:
                    num_high += len(module_mapping[module]["targets"])
                else:
                    num_low += len(module_mapping[module]["targets"])

                for target in module_mapping[module]["targets"]:
                    if target not in module_mapping:
                        continue
                    temp_intermediates.append((target, status, module))

            intermediates = temp_intermediates

        return num_low, num_high

    def part_two(self) -> int:
        """part two answer"""

        module_mapping: dict[str, dict] = {}
        initials: list[str] = []

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                if line.startswith("broadcaster"):
                    initials = line.split(" -> ")[1].split(", ")
                    continue

                parts = line.split(" -> ")

                if line.startswith("%"):
                    module_mapping[parts[0][1:]] = {
                        "type": "%",
                        "status": 0,
                        "targets": parts[1].split(", "),
                    }
                else:
                    module_mapping[parts[0][1:]] = {
                        "type": "&",
                        "sources": [],
                        "status": [],
                        "targets": parts[1].split(", "),
                    }

        for module_name, module_dict in module_mapping.items():
            for module in module_dict["targets"]:
                if module not in module_mapping:
                    continue
                if module_mapping[module]["type"] == "&":
                    module_mapping[module]["sources"].append(module_name)
                    module_mapping[module]["status"].append(0)

        answer = 0
        result = False

        while not result:
            answer += 1
            result = self._process_2(module_mapping, initials)

        return answer

    def _process_2(self, module_mapping: dict[str, dict], modules: list[str]) -> bool:
        intermediates = [(module, 0, "") for module in modules]

        while intermediates:
            temp_intermediates = []

            for module, status, source in intermediates:
                if module_mapping[module]["type"] == "%":
                    if status:
                        continue

                    status = int(not module_mapping[module]["status"])

                    module_mapping[module]["status"] = status
                else:
                    status_idx = module_mapping[module]["sources"].index(source)

                    module_mapping[module]["status"][status_idx] = status

                    status = int(not all(module_mapping[module]["status"]))

                for target in module_mapping[module]["targets"]:
                    if target not in module_mapping:
                        if not status:
                            return True

                        continue
                    temp_intermediates.append((target, status, module))

            intermediates = temp_intermediates

        return False

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
