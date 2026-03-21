class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        shade = int(self.height * self.trunk_diameter / 100)
        return shade


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 15, "yellow")
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1460, 35)
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 60, "autumn", "vitamin A")
    ]

    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, "
              f"{flower.age} days, {flower.color} color")
        flower.bloom()

    for tree in trees:
        print(f"{tree.name} (Tree): {tree.height}cm, "
              f"{tree.age} days, {tree.trunk_diameter}cm diameter")
        shade = tree.produce_shade()
        print(f"{tree.name} provides {shade} square meters of shade")

    for veg in vegetables:
        print(f"{veg.name} (Vegetable): {veg.height}cm, "
              f"{veg.age} days, {veg.harvest_season} harvest")
        print(f"{veg.name} is rich in {veg.nutritional_value}")
