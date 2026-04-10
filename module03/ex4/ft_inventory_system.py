import sys


def find_colon(s: str) -> int:
    """Find position of first colon in string. Return -1 if not found."""
    i: int = 0
    for ch in s:
        if ch == ':':
            return i
        i += 1
    return -1


def count_char(s: str, c: str) -> int:
    """Count occurrences of character c in string s."""
    count: int = 0
    for ch in s:
        if ch == c:
            count += 1
    return count


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse command-line args in format item:quantity into a dict."""
    inventory: dict[str, int] = {}
    for arg in args:
        colon_pos: int = find_colon(arg)
        if colon_pos == -1 or count_char(arg, ':') != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name: str = arg[:colon_pos]
        qty_str: str = arg[colon_pos + 1:]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def find_most_abundant(inventory: dict[str, int]) -> str:
    """Find the most abundant item (first in case of tie)."""
    best: str = ""
    best_qty: int = 0
    first: bool = True
    for name in inventory.keys():
        qty: int = inventory[name]
        if first or qty > best_qty:
            best = name
            best_qty = qty
            first = False
    return best


def find_least_abundant(inventory: dict[str, int]) -> str:
    """Find the least abundant item (first in case of tie)."""
    best: str = ""
    best_qty: int = 0
    first: bool = True
    for name in inventory.keys():
        qty: int = inventory[name]
        if first or qty < best_qty:
            best = name
            best_qty = qty
            first = False
    return best


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for name in inventory.keys():
        qty: int = inventory[name]
        if total > 0:
            pct: float = round(qty / total * 100, 1)
        else:
            pct = 0.0
        print(f"Item {name} represents {pct}%")

    if len(inventory) > 0:
        most: str = find_most_abundant(inventory)
        print(
            f"Item most abundant: {most} "
            f"with quantity {inventory[most]}"
        )
        least: str = find_least_abundant(inventory)
        print(
            f"Item least abundant: {least} "
            f"with quantity {inventory[least]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
