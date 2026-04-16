def secure_archive(
    filename: str,
    mode: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename, "r") as f:
                data: str = f.read()
            return (True, data)
        elif mode == "write":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid mode: {mode}")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_archive.txt", "write", result[1]))


if __name__ == "__main__":
    main()
