from abc import ABC, abstractmethod
from typing import cast

from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class StrategyError(Exception):
    """Raised when a BattleStrategy is asked to act on an incompatible
    Creature. Carries a human-readable message for the tournament log.
    """


class BattleStrategy(ABC):
    """Abstract battle behavior.

    `is_valid` answers whether a given Creature is compatible with the
    strategy without performing any side effect. `act` is the action
    the tournament runs; it MUST raise `StrategyError` if called on an
    incompatible Creature.
    """

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    """Works with any Creature — just attacks."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Needs a TransformCapability: transform → attack → revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"aggressive strategy"
            )
        transformable = cast(TransformCapability, creature)
        print(transformable.transform())
        print(creature.attack())
        print(transformable.revert())


class DefensiveStrategy(BattleStrategy):
    """Needs a HealCapability: attack → heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                f"defensive strategy"
            )
        healer = cast(HealCapability, creature)
        print(creature.attack())
        print(healer.heal())
