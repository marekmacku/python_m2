"""ex1 test script — creatures with capabilities."""

from typing import cast

from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healer(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        print(cast(HealCapability, creature).heal())


def test_transformer(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        transformable = cast(TransformCapability, creature)
        print(transformable.transform())
        print(creature.attack())
        print(transformable.revert())


def main() -> None:
    try:
        test_healer(HealingCreatureFactory())
        test_transformer(TransformCreatureFactory())
    except Exception as exc:
        print(f"capacitor.py error: {exc}")


if __name__ == "__main__":
    main()
