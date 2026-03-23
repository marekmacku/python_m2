def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        plants = {"rose": "red"}
        _ = plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("Testing multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
