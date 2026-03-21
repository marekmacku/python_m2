def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(F"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(F"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(F"{name} seeds: covers {quantity} square meters")
    else:
        print(F"{name} seeds: {quantity} Unknown unit type")