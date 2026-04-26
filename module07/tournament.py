"""ex2 test script — a round-robin tournament."""

from typing import List, Tuple

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    """Run one tournament: every opponent fights every other opponent.

    Each opponent fields the *base* creature produced by its factory,
    acting through the strategy it was paired with. A `StrategyError`
    from any `act` aborts the tournament but not the whole script.
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    pairs = [(factory.create_base(), strategy)
             for factory, strategy in opponents]

    for i, (c1, s1) in enumerate(pairs):
        for c2, s2 in pairs[i + 1:]:
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                s1.act(c1)
                s2.act(c2)
            except StrategyError as exc:
                print(
                    f"Battle error, aborting tournament: {exc}"
                )
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    tournaments: List[Tuple[str, List[Opponent]]] = [
        (
            "Tournament 0 (basic)\n"
            "[ (Flameling+Normal), (Healing+Defensive) ]",
            [
                (FlameFactory(), normal),
                (HealingCreatureFactory(), defensive),
            ],
        ),
        (
            "Tournament 1 (error)\n"
            "[ (Flameling+Aggressive), (Healing+Defensive) ]",
            [
                (FlameFactory(), aggressive),
                (HealingCreatureFactory(), defensive),
            ],
        ),
        (
            "Tournament 2 (multiple)\n"
            "[ (Aquabub+Normal), (Healing+Defensive), "
            "(Transform+Aggressive) ]",
            [
                (AquaFactory(), normal),
                (HealingCreatureFactory(), defensive),
                (TransformCreatureFactory(), aggressive),
            ],
        ),
    ]

    for header, opponents in tournaments:
        print(header)
        try:
            battle(opponents)
        except Exception as exc:
            print(f"tournament.py error: {exc}")


if __name__ == "__main__":
    main()
