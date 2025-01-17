"""
day_11.py

Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11
"""

from pathlib import Path
from typing import Self

DATA_PATH = Path(__file__).parent / "data"


class LinkedListNode:
    value: str
    _next: Self | None

    def __init__(self, value: str, _next: Self | None) -> None:
        self.value = self._process_value(value)
        self._next = _next

    def _process_value(self, value: str) -> str:
        """process value"""

        if not value.startswith("0"):
            return value

        if int(value) == 0:
            return "0"

        return value.lstrip("0")


class Solution:
    def __init__(self) -> None:
        """initiation"""

        with DATA_PATH.joinpath("11.txt").open("r", encoding="utf-8") as file:
            self.initials = file.read().strip().split()

    def _traverse(self, head: LinkedListNode) -> None:
        """traverse"""

        current = head

        while current:
            print(current.value, end=" ")
            current = current._next

        print("\n")

    def _get_length(self, head: LinkedListNode) -> int:
        """get length"""

        length = 0

        current = head

        while current:
            length += 1
            current = current._next

        return length

    def part1(self) -> int:
        """part1"""

        length = 0

        for value in self.initials:
            head = LinkedListNode(value, None)

            for _ in range(25):
                head = self._blink(head=head)

            length += self._get_length(head=head)

        return length

    def _blink(self, head: LinkedListNode) -> LinkedListNode:
        """blink"""

        dummy_head = LinkedListNode("-1", head)

        prev, current, next_ = dummy_head, head, head._next

        while current:
            if (
                length := len(current.value)
            ) & 1:  # the number of digits of value is odd
                if current.value == "0":
                    current.value = "1"
                else:
                    current.value = str(int(current.value) * 2024)

                prev, current, next_ = current, next_, next_._next if next_ else None
            else:  # the number of digits of value is even
                right = LinkedListNode(current.value[length // 2 :], None)
                left = LinkedListNode(current.value[: length // 2], right)

                prev._next = left
                right._next = next_

                prev, current, next_ = right, next_, next_._next if next_ else None

        return dummy_head._next

    def part2(self) -> int:
        """part2"""

        return -1


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
