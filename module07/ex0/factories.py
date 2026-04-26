from abc import ABC, abstractmethod

from ._creatures import Aquabub, Flameling, Pyrodon, Torragon
from .creature import Creature


class CreatureFactory(ABC):
    """Abstract factory for a Creature family (base + evolved form)."""

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
