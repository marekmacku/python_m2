class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_plant_error():
    raise PlantError("The tomato plant is wilting!")


def raise_water_error():
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
