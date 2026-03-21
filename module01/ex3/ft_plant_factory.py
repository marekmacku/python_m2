class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    print("=== Plant Factory Output ===")
    for data in plant_data:
        p = Plant(*data)
        plants.append(p)
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")
    print(f"Total plants created: {len(plants)}")
