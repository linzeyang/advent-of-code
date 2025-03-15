"""
2023 Day 07
https://adventofcode.com/2023/day/7
"""

from collections import Counter
from functools import cmp_to_key
from pathlib import Path


class Solution:
    """solution"""

    INPUT_FILE_PATH: Path = Path(__file__).parent / "data" / "07.txt"

    def part_one(self) -> int:  # noqa: C901
        """part one answer"""

        five_of_a_kind: list[str] = []
        four_of_a_kind: list[str] = []
        full_house: list[str] = []
        three_of_a_kind: list[str] = []
        two_pair: list[str] = []
        one_pair: list[str] = []
        high_card: list[str] = []

        hand_val_mapping: dict[str, int] = {}

        def classify(hand: str) -> None:
            cou = Counter(hand)

            freq = sorted(cou.values(), reverse=True)

            if len(freq) == 1:
                five_of_a_kind.append(hand)
            elif len(freq) == 2:
                if freq[0] == 4:
                    four_of_a_kind.append(hand)
                else:
                    full_house.append(hand)
            elif len(freq) == 3:
                if freq[0] == 3:
                    three_of_a_kind.append(hand)
                else:
                    two_pair.append(hand)
            elif len(freq) == 4:
                one_pair.append(hand)
            elif len(freq) == 5:
                high_card.append(hand)

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                hand, val = line.split(" ")
                hand_val_mapping[hand] = int(val)
                classify(hand)

        strength = dict(
            zip(
                ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"],
                list(range(13))[::-1],
                strict=True,
            )
        )

        def cmp_func(hand1: str, hand2: str) -> int:
            for idx in range(5):
                if strength[hand1[idx]] < strength[hand2[idx]]:
                    return -1
                if strength[hand1[idx]] > strength[hand2[idx]]:
                    return 1

            return 0

        five_of_a_kind.sort(key=cmp_to_key(cmp_func))
        four_of_a_kind.sort(key=cmp_to_key(cmp_func))
        full_house.sort(key=cmp_to_key(cmp_func))
        three_of_a_kind.sort(key=cmp_to_key(cmp_func))
        two_pair.sort(key=cmp_to_key(cmp_func))
        one_pair.sort(key=cmp_to_key(cmp_func))
        high_card.sort(key=cmp_to_key(cmp_func))

        answer = 0
        rank = 1

        for hand in high_card:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in one_pair:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in two_pair:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in three_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in full_house:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in four_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in five_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        return answer

    def part_two(self) -> int:  # noqa: C901
        """part two answer"""

        five_of_a_kind: list[str] = []
        four_of_a_kind: list[str] = []
        full_house: list[str] = []
        three_of_a_kind: list[str] = []
        two_pair: list[str] = []
        one_pair: list[str] = []
        high_card: list[str] = []

        hand_val_mapping: dict[str, int] = {}

        def classify(hand: str) -> None:  # noqa: C901
            cou = Counter(hand)

            freq = sorted(cou.values(), reverse=True)

            num_j = cou["J"] if "J" in cou else 0

            if num_j == 5 or num_j == 4:
                five_of_a_kind.append(hand)
                return

            if num_j == 3:
                if len(freq) == 2:
                    five_of_a_kind.append(hand)
                else:
                    four_of_a_kind.append(hand)
                return

            if num_j == 2:
                if len(freq) == 2:
                    five_of_a_kind.append(hand)
                elif len(freq) == 3:
                    four_of_a_kind.append(hand)
                else:
                    three_of_a_kind.append(hand)
                return

            if num_j == 1:
                if len(freq) == 2:
                    five_of_a_kind.append(hand)
                elif len(freq) == 3:
                    if freq[0] == 3:
                        four_of_a_kind.append(hand)
                    else:
                        full_house.append(hand)
                elif len(freq) == 4:
                    three_of_a_kind.append(hand)
                else:
                    one_pair.append(hand)
                return

            if len(freq) == 1:
                five_of_a_kind.append(hand)
            elif len(freq) == 2:
                if freq[0] == 4:
                    four_of_a_kind.append(hand)
                else:
                    full_house.append(hand)
            elif len(freq) == 3:
                if freq[0] == 3:
                    three_of_a_kind.append(hand)
                else:
                    two_pair.append(hand)
            elif len(freq) == 4:
                one_pair.append(hand)
            elif len(freq) == 5:
                high_card.append(hand)

        with self.INPUT_FILE_PATH.open(mode="r", encoding="utf-8") as file:
            while line := file.readline().strip():
                hand, val = line.split(" ")
                hand_val_mapping[hand] = int(val)
                classify(hand)

        strength = dict(
            zip(
                ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"],
                list(range(13))[::-1],
                strict=True,
            )
        )

        def cmp_func(hand1: str, hand2: str) -> int:
            for idx in range(5):
                if strength[hand1[idx]] < strength[hand2[idx]]:
                    return -1
                if strength[hand1[idx]] > strength[hand2[idx]]:
                    return 1

            return 0

        five_of_a_kind.sort(key=cmp_to_key(cmp_func))
        four_of_a_kind.sort(key=cmp_to_key(cmp_func))
        full_house.sort(key=cmp_to_key(cmp_func))
        three_of_a_kind.sort(key=cmp_to_key(cmp_func))
        two_pair.sort(key=cmp_to_key(cmp_func))
        one_pair.sort(key=cmp_to_key(cmp_func))
        high_card.sort(key=cmp_to_key(cmp_func))

        answer = 0
        rank = 1

        for hand in high_card:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in one_pair:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in two_pair:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in three_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in full_house:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in four_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        for hand in five_of_a_kind:
            answer += rank * hand_val_mapping[hand]
            rank += 1

        return answer

    def print_answers(self) -> None:
        """Print both answers"""
        print(f"The answer for part one is: [[ {self.part_one()} ]]")
        print(f"The answer for part two is: [[ {self.part_two()} ]]")


if __name__ == "__main__":
    Solution().print_answers()
