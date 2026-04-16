import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f: typing.IO[str]
    try:
        f = open(filename, "r")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}",
            file=sys.stderr
        )
        return

    content: str = f.read()
    print("---")
    print(content, end="")
    print("---")
    f.close()
    print(f"File '{filename}' closed.")

    lines: list[str] = content.rstrip('\n').split('\n')
    transformed_content: str = '\n'.join(line + '#' for line in lines) + '\n'

    print("Transform data:")
    print("---")
    print(transformed_content, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename: str = sys.stdin.readline().rstrip('\n')

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    out: typing.IO[str]
    try:
        out = open(new_filename, "w")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{new_filename}': {e}",
            file=sys.stderr
        )
        print("Data not saved.")
        return

    out.write(transformed_content)
    out.close()
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
