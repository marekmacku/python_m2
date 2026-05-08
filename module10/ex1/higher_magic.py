"""Higher Realm — functions as first-class values: pass, return, compose."""

import sys
from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    """Sample spell: deal damage."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Sample spell: restore HP."""
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    """Sample spell: grant a barrier."""
    return f"Shield protects {target} with {power} barrier"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that fires spell1 and spell2 with the same args."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell that multiplies power before delegating."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition(target, power) is true."""
    def guarded(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return guarded


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a spell that casts every spell in order and collects results."""
    def sequenced(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequenced


def main() -> int:
    """Demonstrate every higher-order combinator."""
    print("Testing spell combiner...")
    fire_and_heal = spell_combiner(fireball, heal)
    print(f"  callable? {callable(fire_and_heal)}")
    result = fire_and_heal("Dragon", 30)
    print(f"  {result[0]}")
    print(f"  {result[1]}")

    print("=" * 42)
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"  Original: {fireball('Goblin', 10)}")
    print(f"  Amplified: {mega_fireball('Goblin', 10)}")
    print("  Original: 10, Amplified: 30")

    print("=" * 42)
    print("Testing conditional caster (power must be >= 20)...")
    strong_only = conditional_caster(lambda t, p: p >= 20, fireball)
    print(f"  power=15 -> {strong_only('Slime', 15)}")
    print(f"  power=25 -> {strong_only('Slime', 25)}")

    print("=" * 42)
    print("Testing spell sequence...")
    barrage = spell_sequence([fireball, heal, shield])
    for line in barrage("Hero", 20):
        print(f"  {line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
