import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam',
    ]
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps: list[str] = [n for n in players if n[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")

    scores: dict[str, int] = {
        name: random.randint(50, 999) for name in all_caps
    }
    print(f"Score dict: {scores}")

    avg: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high: dict[str, int] = {
        n: scores[n] for n in scores if scores[n] > avg
    }
    print(f"High scores: {high}")
