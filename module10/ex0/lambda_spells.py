"""Lambda Sanctum — anonymous functions for one-shot transformations."""

import sys


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level (descending) using a lambda key."""
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Keep mages whose power is at least min_power."""
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name with sparkle markers."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Compute max/min/avg power across the given mages."""
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        ),
    }


def main() -> int:
    """Demonstrate every lambda-based transformation."""
    artifacts: list[dict] = [
        {"name": "Crystal Orb", "power": 85, "type": "scrying"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Iron Ring", "power": 40, "type": "trinket"},
    ]
    mages: list[dict] = [
        {"name": "Aria", "power": 70, "element": "wind"},
        {"name": "Borin", "power": 95, "element": "earth"},
        {"name": "Cira", "power": 30, "element": "water"},
        {"name": "Dorn", "power": 55, "element": "fire"},
    ]
    spells: list[str] = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    top = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{top['name']} ({top['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("=" * 42)
    print("Testing power filter (min_power=60)...")
    strong = power_filter(mages, 60)
    for mage in strong:
        print(f"  {mage['name']} ({mage['power']} power, {mage['element']})")

    print("=" * 42)
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("=" * 42)
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"  max_power: {stats['max_power']}")
    print(f"  min_power: {stats['min_power']}")
    print(f"  avg_power: {stats['avg_power']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
