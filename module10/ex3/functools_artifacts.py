"""Ancient Library — functools and operator treasures in action."""

import functools
import operator
import sys
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combine spell powers via functools.reduce + an operator function."""
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Pre-bind power=50 and an element for three specialized enchantments."""
    default_power = 50
    elements = ("fire", "ice", "lightning")

    specialized: dict[str, Callable] = {}
    for element in elements:
        specialized[element] = functools.partial(
            base_enchantment, default_power, element
        )
    return specialized


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number; lru_cache turns O(2^n) into O(n)."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Build a singledispatch caster keyed on the spell argument's type."""
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def main() -> int:
    """Demonstrate every functools artifact end-to-end."""
    spells: list[int] = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"  Sum: {spell_reducer(spells, 'add')}")
    print(f"  Product: {spell_reducer(spells, 'multiply')}")
    print(f"  Max: {spell_reducer(spells, 'max')}")
    print(f"  Min: {spell_reducer(spells, 'min')}")
    print(f"  Empty: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spells, "divide")
    except ValueError as err:
        print(f"  Unknown op error: {err}")

    print("=" * 42)
    print("Testing partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.title()} {target} (+{power})"

    enchanters = partial_enchanter(base_enchantment)
    for name, enchant in enchanters.items():
        print(f"  {name}: {enchant('Sword')}")

    print("=" * 42)
    print("Testing memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"  Fib({n}): {memoized_fibonacci(n)}")
    memoized_fibonacci(15)
    info = memoized_fibonacci.cache_info()
    print(f"  cache_info: hits={info.hits}, misses={info.misses}")

    print("=" * 42)
    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(f"  {cast(42)}")
    print(f"  {cast('fireball')}")
    print(f"  {cast(['fireball', 'heal', 'shield'])}")
    print(f"  {cast(3.14)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
