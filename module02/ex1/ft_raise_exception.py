def input_temperature(data: str) -> int:
    temp = int(data)
    if temp > 40:
        raise ValueError(str(temp) + "°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(str(temp) + "°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    test_values = ["25", "abc", "100", "-50"]
    for value in test_values:
        print("Input data is '" + value + "'")
        try:
            temp = input_temperature(value)
            print("Temperature is now " + str(temp) + "°C")
        except ValueError as e:
            print("Caught input_temperature error: " + str(e))
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
