from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base for every Creature card.

    Holds the name and the elemental type shared by every card, plus a
    concrete `describe` helper. Subclasses must implement `attack`.
    """

    def __init__(self, name: str, type_: str) -> None:
        self.name: str = name
        self.type_: str = type_

    def describe(self) -> str:
        return f"{self.name} is a {self.type_} type Creature"

    @abstractmethod
    def attack(self) -> str:
        ...
