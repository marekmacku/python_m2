"""Master's Tower — decorators, decorator factories, and staticmethod."""

import functools
import sys
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Print elapsed wall-clock time around the wrapped call."""
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory: gate a power-first function on min_power."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int, *args: object, **kwargs: object) -> object:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory: retry on any Exception, up to max_attempts times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# Standalone, power-first function so power_validator applies cleanly.
@power_validator(10)
def _do_cast(power: int, spell_name: str) -> str:
    """Inner caster for MageGuild.cast_spell, guarded by power_validator."""
    return f"Successfully cast {spell_name} with {power} power"


class MageGuild:
    """Guild facade exposing a static name check and an instance caster."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True for names of 3+ chars containing only letters/spaces."""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Delegate to the decorated standalone caster."""
        return _do_cast(power, spell_name)


def main() -> int:
    """Demonstrate every decorator and the MageGuild class."""
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("=" * 42)
    print("Testing retrying spell (always fails)...")

    @retry_spell(3)
    def doomed_spell() -> str:
        raise RuntimeError("magic dispersed")

    print(f"  {doomed_spell()}")

    print("=" * 42)
    print("Testing retrying spell (succeeds on 2nd try)...")

    attempts = {"n": 0}

    @retry_spell(3)
    def flaky_spell() -> str:
        attempts["n"] += 1
        if attempts["n"] < 2:
            raise RuntimeError("misfire")
        return "Waaaaaaagh spelled !"

    print(f"  {flaky_spell()}")

    print("=" * 42)
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    return 0


if __name__ == "__main__":
    sys.exit(main())
