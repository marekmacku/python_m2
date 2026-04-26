"""ex0 — Abstract Factory for Creature families.

Only the abstract types and the concrete factories are exposed. Concrete
Creature classes are intentionally hidden: clients must go through a
factory to obtain a Creature, which is the whole point of the pattern.
"""

from .creature import Creature
from .factories import AquaFactory, CreatureFactory, FlameFactory

__all__ = [
    "Creature",
    "CreatureFactory",
    "FlameFactory",
    "AquaFactory",
]
