"""
day_22.py

Day 22: Crab Combat

https://adventofcode.com/2024/day/22
"""

from collections import deque
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"


class Solution:
    def __init__(self) -> None:
        """initiation"""

        self.deck_1: deque[int] = deque([])
        self.deck_2: deque[int] = deque([])

        with DATA_PATH.joinpath("22.txt").open("r", encoding="utf-8") as file:
            target = self.deck_1

            for line in file:
                if line.startswith("Player"):
                    continue

                if line == "\n":
                    target = self.deck_2
                    continue

                target.append(int(line.strip()))

    def part1(self) -> int:
        """part1"""

        deck_1: deque[int] = self.deck_1.copy()
        deck_2: deque[int] = self.deck_2.copy()

        while deck_1 and deck_2:
            card_1 = deck_1.popleft()
            card_2 = deck_2.popleft()

            if card_1 > card_2:
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)

        target = deck_1 if not deck_2 else deck_2

        out = 0

        for idx, card in enumerate(reversed(target), 1):
            out += card * idx

        return out

    def part2(self) -> int:
        """part2"""

        deck_1: deque[int] = self.deck_1.copy()
        deck_2: deque[int] = self.deck_2.copy()

        target = (
            deck_1 if self._play_game(deck_1=deck_1, deck_2=deck_2) == 1 else deck_2
        )

        out = 0

        for idx, card in enumerate(reversed(target), 1):
            out += card * idx

        return out

    def _play_game(self, deck_1: deque[int], deck_2: deque[int]) -> int:
        """recursion method. play a game/sub-game until one player wins"""

        # take records of the *rounds* played in this game
        rounds_for_player_1: set[tuple[int, ...]] = set()
        rounds_for_player_2: set[tuple[int, ...]] = set()

        while deck_1 and deck_2:
            if (
                tuple(deck_1) in rounds_for_player_1
                or tuple(deck_2) in rounds_for_player_2
            ):
                # infinite loop, player 1 immediately wins
                return 1

            rounds_for_player_1.add(tuple(deck_1))
            rounds_for_player_2.add(tuple(deck_2))

            card_1 = deck_1.popleft()
            card_2 = deck_2.popleft()

            if card_1 <= len(deck_1) and card_2 <= len(deck_2):
                # enter the subgame to decide the winner
                winner = self._play_game(
                    deck_1=deque(list(deck_1)[:card_1]),
                    deck_2=deque(list(deck_2)[:card_2]),
                )
            else:
                # regular game, whoever has the highest card wins
                winner = 1 if card_1 > card_2 else 2

            if winner == 1:
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)

        if not deck_2:
            return 1

        return 2


def main() -> None:
    """main"""

    solution = Solution()

    print(f"Answer for part 1 is {solution.part1()}")
    print(f"Answer for part 2 is {solution.part2()}")


if __name__ == "__main__":
    main()
