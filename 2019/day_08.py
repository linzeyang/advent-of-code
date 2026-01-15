"""
day_08.py

Day 8: Space Image Format

https://adventofcode.com/2019/day/8
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"

WIDTH = 25
HEIGHT = 6


class Solution:
    """Solution for Advent of Code 2019 Day 8."""

    def __init__(self) -> None:
        """Load image layers."""

        with (DATA_PATH / "08.txt").open("r", encoding="utf-8") as file:
            raw: str = file.readline().strip()

        layer_size: int = WIDTH * HEIGHT
        self.layers: list[str] = [
            raw[i * layer_size : (i + 1) * layer_size]
            for i in range(len(raw) // layer_size)
        ]

    def part1(self) -> int:
        """Solve part 1."""

        layer_with_fewest_zeros: str = min(
            self.layers, key=lambda layer: layer.count("0")
        )

        return layer_with_fewest_zeros.count("1") * layer_with_fewest_zeros.count("2")

    def part2(self) -> str:
        """Solve part 2: decode the image and return it as ASCII art."""

        pixels: list[str] = ["2"] * WIDTH * HEIGHT

        for layer in self.layers:
            for idx, pixel in enumerate(layer):
                if pixels[idx] == "2" and pixel != "2":
                    pixels[idx] = pixel

        lines: list[str] = []

        for row in range(HEIGHT):
            start: int = row * WIDTH
            end: int = start + WIDTH
            lines.append(
                "".join("#" if pixel == "1" else " " for pixel in pixels[start:end])
            )

        return "\n".join(lines)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is\n{solution.part2()}")


if __name__ == "__main__":
    main()
