"""
2022 Day 07
https://adventofcode.com/2022/day/7
"""

from pathlib import Path

from typing_extensions import Self


class FileSystemNode:
    def __init__(
        self, typp: str, name: str, size: int, parent: Self | None = None
    ) -> None:
        self.typp = typp
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def __str__(self) -> str:
        return (
            f"{self.__class__} {self.typp} {self.name}"
            f" {self.parent.name if self.parent else None}"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__} {self.typp} {self.name}"
            f" {self.parent.name if self.parent else None}"
        )

    def add_child(self, line: str) -> None:
        if line.startswith("dir"):
            node = FileSystemNode(
                typp="dir", name=line.split()[-1], size=0, parent=self
            )
        else:
            node = FileSystemNode(
                typp="file",
                name=line.split()[-1],
                size=int(line.split()[0]),
                parent=self,
            )

        self.children.append(node)

    def get_child(self, name: str) -> Self:
        for child in self.children:
            if child.name == name:
                return child

        return child

    def get_parent(self) -> Self | None:
        return self.parent

    def get_size(self) -> int:
        if self.typp == "file":
            return self.size

        if not self.children:
            return 0

        return sum(child.get_size() for child in self.children)


part1_answer = 0
sizes = []


def traverse(node) -> None:
    if (size := node.get_size()) <= 100000:
        global part1_answer
        part1_answer += size

    global sizes
    sizes.append(size)

    for child in node.children:
        if child.typp == "dir":
            traverse(child)


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "07.txt"

    def part_one(self) -> int:
        """part one answer"""

        root = FileSystemNode(typp="dir", name="/", size=0)
        current = None
        mode = None

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                if line == "$ cd /":
                    current = root
                    continue

                if line.startswith("$ ls"):
                    mode = "ls"
                    continue

                if line.startswith("$ cd"):
                    mode = "cd"
                    path = line.split()[-1]

                    if path == "..":
                        current = current.get_parent()
                    else:
                        current = current.get_child(path)
                    continue

                if mode == "ls":
                    current.add_child(line)

        traverse(root)

        global part1_answer

        return part1_answer

    def part_two(self) -> int:
        """part two answer"""

        global sizes

        return min(sorted(size for size in sizes if size >= max(sizes) - 40000000))

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
