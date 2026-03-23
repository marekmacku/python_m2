def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 42
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print("Testing operation " + str(i) + "...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print("Caught " + e.__class__.__name__ + ": " + str(e))
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
