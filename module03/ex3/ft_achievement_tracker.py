import random


ALL_ACHIEVEMENTS: list[str] = [
    "Master Explorer", "Boss Slayer", "Collector Supreme",
    "Speed Runner", "Strategist", "Crafting Genius",
    "World Savior", "Untouchable", "First Steps",
    "Treasure Hunter", "Sharp Mind", "Survivor",
    "Unstoppable", "Hidden Path Finder",
]


def gen_player_achievements(
    achievements: list[str],
) -> set[str]:
    """Randomly assign a set of achievements to a player."""
    count: int = random.randint(4, 8)
    return set(random.sample(achievements, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    achievement_sets: list[set[str]] = []
    for _ in names:
        achievement_sets.append(
            gen_player_achievements(ALL_ACHIEVEMENTS)
        )

    i: int = 0
    for name in names:
        print(f"Player {name}: {achievement_sets[i]}")
        i += 1

    all_distinct: set[str] = achievement_sets[0].union(
        *achievement_sets[1:]
    )
    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = achievement_sets[0].intersection(
        *achievement_sets[1:]
    )
    print(f"Common achievements: {common}")

    all_master: set[str] = set(ALL_ACHIEVEMENTS)

    i = 0
    for name in names:
        others: set[str] = set()
        j: int = 0
        for other_name in names:
            if j != i:
                others = others.union(achievement_sets[j])
            j += 1
        unique: set[str] = achievement_sets[i].difference(others)
        print(f"Only {name} has: {unique}")
        i += 1

    i = 0
    for name in names:
        missing: set[str] = all_master.difference(achievement_sets[i])
        print(f"{name} is missing: {missing}")
        i += 1
