"""
day_09.py

Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.points: list[tuple[int, ...]] = []

        with DATA_PATH.joinpath("09.txt").open("r", encoding="utf-8") as file:
            for line in file:
                self.points.append(tuple(map(int, line.split(","))))

        # Build the loop edges: consecutive red tiles are joined by a straight
        # green line either on the same row (horizontal) or column (vertical).
        self.horizontal_edges: list[tuple[int, int, int]] = []
        self.vertical_edges: list[tuple[int, int, int]] = []

        n: int = len(self.points)

        for i in range(n):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % n]

            if x1 == x2 and y1 == y2:
                continue

            if y1 == y2:
                a, b = (x1, x2) if x1 <= x2 else (x2, x1)
                self.horizontal_edges.append((y1, a, b))
            else:
                a, b = (y1, y2) if y1 <= y2 else (y2, y1)
                self.vertical_edges.append((x1, a, b))

    def part1(self) -> int:
        """part1"""

        out: int = 2
        length: int = len(self.points)

        # brute force: total number of points < 500
        for idx in range(length - 1):
            for jdx in range(idx + 1, length):
                out = max(
                    out,
                    (abs(self.points[idx][0] - self.points[jdx][0]) + 1)
                    * (abs(self.points[idx][1] - self.points[jdx][1]) + 1),
                )

        return out

    def part2(self) -> int:
        """
        part2

        A rectangle is valid when its four borders lie entirely on red/green
        tiles. For each row/column we precompute the merged spans of tiles that
        are red or green (either on the loop edge or inside it), then accept a
        candidate only if all four borders fall within a single span. Because
        the loop is a simple (non self-intersecting) polygon, a fully covered
        border guarantees the interior is covered too, so no separate point-in-
        polygon test is required.
        """

        horizontal_edges: list[tuple[int, int, int]] = self.horizontal_edges
        vertical_edges: list[tuple[int, int, int]] = self.vertical_edges
        n: int = len(self.points)

        def merge_intervals(
            intervals: list[tuple[int, int]],
        ) -> list[tuple[int, int]]:
            if not intervals:
                return []

            intervals.sort(key=lambda t: t[0])

            out: list[tuple[int, int]] = []
            start, end = intervals[0]

            for a, b in intervals[1:]:
                if a <= end:
                    if b > end:
                        end = b
                else:
                    out.append((start, end))
                    start, end = a, b

            out.append((start, end))

            return out

        x_cache: dict[int, list[tuple[int, int]]] = {}
        y_cache: dict[int, list[tuple[int, int]]] = {}

        def x_intervals(y: int) -> list[tuple[int, int]]:
            cached: list[tuple[int, int]] | None = x_cache.get(y)

            if cached is not None:
                return cached

            xs: list[int] = []

            for xv, ya, yb in vertical_edges:
                if ya <= y < yb:
                    xs.append(xv)

            xs.sort()

            intervals: list[tuple[int, int]] = []

            for i in range(0, len(xs), 2):
                if i + 1 < len(xs):
                    intervals.append((xs[i], xs[i + 1]))

            for yh, xa, xb in horizontal_edges:
                if yh == y:
                    intervals.append((xa, xb))

            merged: list[tuple[int, int]] = merge_intervals(intervals)
            x_cache[y] = merged

            return merged

        def y_intervals(x: int) -> list[tuple[int, int]]:
            cached: list[tuple[int, int]] | None = y_cache.get(x)

            if cached is not None:
                return cached

            ys: list[int] = []

            for yh, xa, xb in horizontal_edges:
                if xa <= x < xb:
                    ys.append(yh)

            ys.sort()

            intervals: list[tuple[int, int]] = []

            for i in range(0, len(ys), 2):
                if i + 1 < len(ys):
                    intervals.append((ys[i], ys[i + 1]))

            for xv, ya, yb in vertical_edges:
                if xv == x:
                    intervals.append((ya, yb))

            merged: list[tuple[int, int]] = merge_intervals(intervals)
            y_cache[x] = merged

            return merged

        def interval_covers(
            target: tuple[int, int], intervals: list[tuple[int, int]]
        ) -> bool:
            a, b = target

            for start, end in intervals:
                if start <= a and b <= end:
                    return True

            return False

        out: int = 0

        for i in range(n - 1):
            x1, y1 = self.points[i]

            for j in range(i + 1, n):
                x2, y2 = self.points[j]
                xmin, xmax = (x1, x2) if x1 <= x2 else (x2, x1)
                ymin, ymax = (y1, y2) if y1 <= y2 else (y2, y1)
                area = (xmax - xmin + 1) * (ymax - ymin + 1)

                if area <= out:
                    continue
                if not interval_covers((xmin, xmax), x_intervals(ymin)):
                    continue
                if not interval_covers((xmin, xmax), x_intervals(ymax)):
                    continue
                if not interval_covers((ymin, ymax), y_intervals(xmin)):
                    continue
                if not interval_covers((ymin, ymax), y_intervals(xmax)):
                    continue

                out = area

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
