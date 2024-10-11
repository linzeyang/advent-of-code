"""
2023 Day 05
https://adventofcode.com/2023/day/5
"""

from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "05.txt"

    def part_one(self) -> int:
        """part one answer"""

        seeds: list[int] = []

        seed_to_soil: list[tuple[int, int, int]] = []
        soil_to_fertilizer: list[tuple[int, int, int]] = []
        fertilizer_to_water: list[tuple[int, int, int]] = []
        water_to_light: list[tuple[int, int, int]] = []
        light_to_temperature: list[tuple[int, int, int]] = []
        temperature_to_humidity: list[tuple[int, int, int]] = []
        humidity_to_location: list[tuple[int, int, int]] = []

        current = None

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    continue

                line = line.strip()

                if line.startswith("seeds: "):
                    seeds = [int(part) for part in line[7:].split()]
                    continue

                if line[0].isalpha():
                    if line.startswith("seed-"):
                        current = seed_to_soil
                    elif line.startswith("soil-"):
                        current = soil_to_fertilizer
                    elif line.startswith("fertilizer-"):
                        current = fertilizer_to_water
                    elif line.startswith("water-"):
                        current = water_to_light
                    elif line.startswith("light-"):
                        current = light_to_temperature
                    elif line.startswith("temperature-"):
                        current = temperature_to_humidity
                    else:
                        current = humidity_to_location

                    continue

                current.append(tuple(int(part) for part in line.split()))

        soils = [self._find_dest(number, seed_to_soil) for number in seeds]
        fertilizers = [self._find_dest(number, soil_to_fertilizer) for number in soils]
        waters = [
            self._find_dest(number, fertilizer_to_water) for number in fertilizers
        ]
        lights = [self._find_dest(number, water_to_light) for number in waters]
        temperatures = [
            self._find_dest(number, light_to_temperature) for number in lights
        ]
        humidities = [
            self._find_dest(number, temperature_to_humidity) for number in temperatures
        ]
        locations = [
            self._find_dest(number, humidity_to_location) for number in humidities
        ]

        return min(locations)

    def _find_dest(self, number: int, mapping: list[tuple[int, int, int]]) -> int:
        for dest_start, source_start, rang in mapping:
            if source_start <= number < source_start + rang:
                return dest_start + number - source_start

        return number

    def part_two(self) -> int:
        """part two answer"""

        seeds: list[int] = []

        seed_to_soil: list[tuple[int, int, int]] = []
        soil_to_fertilizer: list[tuple[int, int, int]] = []
        fertilizer_to_water: list[tuple[int, int, int]] = []
        water_to_light: list[tuple[int, int, int]] = []
        light_to_temperature: list[tuple[int, int, int]] = []
        temperature_to_humidity: list[tuple[int, int, int]] = []
        humidity_to_location: list[tuple[int, int, int]] = []

        current = None

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline():
                if line == "\n":
                    continue

                line = line.strip()

                if line.startswith("seeds: "):
                    seeds = [int(part) for part in line[7:].split()]
                    continue

                if line[0].isalpha():
                    if line.startswith("seed-"):
                        current = seed_to_soil
                    elif line.startswith("soil-"):
                        current = soil_to_fertilizer
                    elif line.startswith("fertilizer-"):
                        current = fertilizer_to_water
                    elif line.startswith("water-"):
                        current = water_to_light
                    elif line.startswith("light-"):
                        current = light_to_temperature
                    elif line.startswith("temperature-"):
                        current = temperature_to_humidity
                    else:
                        current = humidity_to_location

                    continue

                current.append(tuple(int(part) for part in line.split()))

        seed_ranges = [(seeds[idx], seeds[idx + 1]) for idx in range(0, len(seeds), 2)]

        soil_ranges: list[tuple[int, int]] = []
        for rang in seed_ranges:
            soil_ranges.extend(self._find_dest_ranges(rang, seed_to_soil))

        fertilizer_ranges: list[tuple[int, int]] = []
        for rang in soil_ranges:
            fertilizer_ranges.extend(self._find_dest_ranges(rang, soil_to_fertilizer))

        water_ranges: list[tuple[int, int]] = []
        for rang in fertilizer_ranges:
            water_ranges.extend(self._find_dest_ranges(rang, fertilizer_to_water))

        light_ranges: list[tuple[int, int]] = []
        for rang in water_ranges:
            light_ranges.extend(self._find_dest_ranges(rang, water_to_light))

        temperature_ranges: list[tuple[int, int]] = []
        for rang in light_ranges:
            temperature_ranges.extend(
                self._find_dest_ranges(rang, light_to_temperature)
            )

        humidity_ranges: list[tuple[int, int]] = []
        for rang in temperature_ranges:
            humidity_ranges.extend(
                self._find_dest_ranges(rang, temperature_to_humidity)
            )

        location_ranges: list[tuple[int, int]] = []
        for rang in humidity_ranges:
            location_ranges = self._find_dest_ranges(rang, humidity_to_location)

        location_ranges.sort(key=lambda tup: tup[0])

        return location_ranges[0][0]

    def _find_dest_ranges(
        self, rang: tuple[int, int], mapping: list[tuple[int, int, int]]
    ) -> list[tuple[int, int]]: ...  # TODO

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
