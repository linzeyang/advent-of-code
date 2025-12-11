"""
day_11.py

Day 11: Reactor

https://adventofcode.com/2025/day/11
"""

from functools import lru_cache
from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.connections: dict[str, tuple[str, ...]] = {}

        with DATA_PATH.joinpath("11.txt").open("r", encoding="utf-8") as file:
            for line in file:
                # Parse "aaa: bbb ccc" -> in_="aaa", out="bbb ccc"
                in_, out = line.strip().split(": ")
                self.connections[in_] = tuple(out.split(" "))

    def part1(self) -> int:
        """part1"""

        return self._count_paths(source="you", destination="out")

    def part2(self) -> int:
        """
        We need to find paths from 'svr' to 'out' that pass through BOTH 'dac' and 'fft'
        Since the graph is a DAG (directed acyclic graph), the order must be either:
         1. svr -> ... -> dac -> ... -> fft -> ... -> out
         2. svr -> ... -> fft -> ... -> dac -> ... -> out
        """

        SVR = "svr"
        DAC = "dac"
        FFT = "fft"
        OUT = "out"

        svr_dac: int = self._count_paths(source=SVR, destination=DAC)
        dac_fft: int = self._count_paths(source=DAC, destination=FFT)
        fft_out: int = self._count_paths(source=FFT, destination=OUT)

        svr_fft: int = self._count_paths(source=SVR, destination=FFT)
        fft_dac: int = self._count_paths(source=FFT, destination=DAC)
        dac_out: int = self._count_paths(source=DAC, destination=OUT)

        return svr_dac * dac_fft * fft_out + svr_fft * fft_dac * dac_out

    def _count_paths(self, source: str, destination: str) -> int:
        """
        Count all paths from source to destination using DFS with memoization.
        Generic method that is used in both part1 and part2.

        Args:
            source (str): The starting node.
            destination (str): The ending node.

        Returns:
            int: The number of paths from source to destination.
        """

        @lru_cache(maxsize=600)  # total number of nodes < 600
        def dfs(current: str) -> int:
            if current == "out":
                return 0

            if destination in self.connections[current]:
                return 1

            out: int = 0

            for key in self.connections[current]:
                out += dfs(key)

            return out

        return dfs(source)


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
