"""Memory Depths — closures that remember their creation environment."""

import sys
from collections.abc import Callable


def mage_counter() -> Callable:
    """Return an independent counter; each call yields the next integer."""
    count: int = 0

    def tick() -> int:
        nonlocal count  # rebind the enclosing local, not a global
        count += 1
        return count

    return tick


def spell_accumulator(initial_power: int) -> Callable:
    """Return an accumulator seeded with initial_power."""
    total: int = initial_power

    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies a fixed enchantment label to any item."""
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a private store/recall pair sharing one hidden dict."""
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> int:
    """Demonstrate that each closure carries its own private state."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"  counter_a call 1: {counter_a()}")
    print(f"  counter_a call 2: {counter_a()}")
    print(f"  counter_b call 1: {counter_b()}")
    print(f"  counter_a call 3: {counter_a()}")

    print("=" * 42)
    print("Testing spell accumulator...")
    pool = spell_accumulator(100)
    print(f"  Base 100, add 20: {pool(20)}")
    print(f"  Base 100, add 30: {pool(30)}")

    print("=" * 42)
    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(f"  {flaming('Sword')}")
    print(f"  {frozen('Shield')}")

    print("=" * 42)
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("  Store 'secret' = 42")
    print(f"  Recall 'secret': {vault['recall']('secret')}")
    print(f"  Recall 'unknown': {vault['recall']('unknown')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
