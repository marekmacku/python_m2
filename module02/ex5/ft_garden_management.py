class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict = {}

    def add_plant(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": 0, "sun": 0}
        print(f"Added {name} successfully")

    def water_plant(
        self, name: str, water: int, sun: int
    ) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found!")
        print(f"Watering {name} - success")
        self.plants[name]["water"] = water
        self.plants[name]["sun"] = sun

    def check_plant_health(
        self, name: str, water: int, sun: int
    ) -> None:
        if water < 1:
            raise ValueError(
                f"Water level {water} is too low (min 1)"
            )
        if water > 10:
            raise ValueError(
                f"Water level {water} is too high (max 10)"
            )
        if sun < 2:
            raise ValueError(
                f"Sunlight hours {sun} is too low (min 2)"
            )
        if sun > 12:
            raise ValueError(
                f"Sunlight hours {sun} is too high (max 12)"
            )
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    try:
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        print("Opening watering system")
        garden.water_plant("tomato", 5, 8)
        garden.water_plant("lettuce", 15, 6)
    finally:
        print("Closing watering system (cleanup)")

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error checking tomato: {e}")
    try:
        garden.check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
