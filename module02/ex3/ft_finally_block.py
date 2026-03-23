def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    valid_input = ["tomato", "lettuce", "carrots"]
    invalid_input = ["tomato", None, "carrots"]
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    water_plants(valid_input)
    print("Watering completed successfully!")
    print("Testing with error...")
    water_plants(invalid_input)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
