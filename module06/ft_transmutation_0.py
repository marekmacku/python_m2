import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
