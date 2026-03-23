class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print("Caught PlantError: " + str(e))

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print("Caught WaterError: " + str(e))

    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print("Caught GardenError: " + str(e))
    try:
        raise_water_error()
    except GardenError as e:
        print("Caught GardenError: " + str(e))

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
