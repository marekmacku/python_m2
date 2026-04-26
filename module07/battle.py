"""ex0 test script — abstract factory in action."""

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Build both forms through the factory and exercise them."""
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    """Pit the base creature of each factory against the other."""
    print("Testing battle")
    c1 = f1.create_base()
    c2 = f2.create_base()
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    try:
        flame = FlameFactory()
        aqua = AquaFactory()
        test_factory(flame)
        test_factory(aqua)
        battle(flame, aqua)
    except Exception as exc:
        print(f"battle.py error: {exc}")


if __name__ == "__main__":
    main()
