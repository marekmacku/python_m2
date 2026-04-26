from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Capability to restore health.

    Deliberately does NOT inherit from Creature: a capability describes
    a contract that could, in principle, be mixed into any object — not
    only creatures.
    """

    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    """Capability to toggle a boosted form.

    Owns the `_transformed` flag so every implementer shares the same
    state contract. Concrete creatures read this flag in `attack` to
    return a stronger string while transformed.
    """

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
