"""ex2 — Strategy pattern for battle behavior.

The tournament code talks only to `BattleStrategy`, never to concrete
Creature classes. Adding a new battle behavior = one new strategy
subclass, no other change.
"""

from .strategies import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
    StrategyError,
)

__all__ = [
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy",
    "StrategyError",
]
