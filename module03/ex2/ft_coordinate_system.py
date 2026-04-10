import math


def get_player_pos() -> tuple[float, float, float]:
    """Ask user for 3D coordinates until valid input is provided."""
    while True:
        raw: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = raw.split(',')
        count: int = 0
        for _ in parts:
            count += 1
        if count != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        valid: bool = True
        for part in parts:
            stripped: str = part.strip()
            try:
                coords.append(float(stripped))
            except ValueError as e:
                print(f"Error on parameter '{stripped}': {e}")
                valid = False
        if valid:
            return (coords[0], coords[1], coords[2])


def calc_distance(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float]
) -> float:
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    dist_to_center: float = calc_distance(pos1, origin)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_between: float = calc_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")
