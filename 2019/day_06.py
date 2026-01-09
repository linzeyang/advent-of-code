"""
day_06.py

Day 6: Universal Orbit Map

https://adventofcode.com/2019/day/6
"""

from pathlib import Path

DATA_PATH: Path = Path(__file__).parent / "data"


class Node:
    def __init__(self, tag: str) -> None:
        self.tag = tag
        self.children: list["Node"] = []

    def __repr__(self) -> str:
        return f"Node: {self.tag}"

    def append_child(self, node: "Node") -> None:
        self.children.append(node)


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self._mapping: dict[str, Node] = {}

        with DATA_PATH.joinpath("06.txt").open("r", encoding="utf-8") as file:
            for line in file:
                left, right = line.strip().split(")")

                if right not in self._mapping:
                    child: Node = Node(tag=right)
                    self._mapping[right] = child
                else:
                    child: Node = self._mapping[right]

                if left not in self._mapping:
                    parent: Node = Node(tag=left)
                    self._mapping[left] = parent
                else:
                    parent: Node = self._mapping[left]

                parent.append_child(node=child)

    def part1(self) -> int:
        """part1"""

        if "COM" not in self._mapping:
            raise ValueError("'COM' not found!")

        out: int = 0
        level: int = 0
        level_nodes: list[Node] = [self._mapping["COM"]]

        while level_nodes:
            out += level * len(level_nodes)
            level += 1

            next_level_nodes: list[Node] = []

            for node in level_nodes:
                if node.children:
                    next_level_nodes.extend(node.children)

            level_nodes = next_level_nodes

        return out

    def part2(self) -> int:
        """part2"""

        def track(node: Node, prev: list[str]):
            if node.tag in ("YOU", "SAN"):
                return prev + [node.tag]

            if not node.children:
                return

            temp: list = []

            for child in node.children:
                res = track(child, prev + [node.tag])

                if res:
                    temp.append(res)

            if len(temp) == 1:
                return temp[0]

            return temp

        left, right = track(node=self._mapping["COM"], prev=[])

        out: int = 0

        for idx in range(min(len(left), len(right))):
            if left[idx] == right[idx]:
                continue

            out = len(left) - idx + len(right) - idx - 2
            break

        return out


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
