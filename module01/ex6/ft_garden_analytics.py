class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def bloom(self) -> str:
        return "blooming"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    gardens = []

    class GardenStats:
        def __init__(self, plants: list):
            self.plants = plants

        def count_types(self) -> tuple:
            prize = 0
            flowering = 0
            regular = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)

        def garden_score(self) -> int:
            height = 0
            for plant in self.plants:
                height += plant.height
            return height

    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list = []
        self.total_growth = 0
        GardenManager.gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.get_info()}, "
                      f"{plant.color} flowers ({plant.bloom()}), "
                      f"Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.get_info()}, "
                      f"{plant.color} flowers ({plant.bloom()})")
            else:
                print(f"- {plant.get_info()}")
        stats = GardenManager.GardenStats(self.plants)
        regular, flowering, prize = stats.count_types()
        print(f"Plants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> list:
        alice = cls("Alice")
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
        bob = cls("Bob")
        bob.add_plant(Plant("Bamboo", 90))
        return [alice, bob]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    gardens = GardenManager.create_garden_network()
    alice = gardens[0]
    bob = gardens[1]
    alice.grow_all()
    alice.report()
    print(f"Height validation test: "
          f"{GardenManager.validate_height(10)}")
    print(f"Garden scores - "
          f"Alice: {GardenManager.GardenStats(alice.plants).garden_score()}"
          f", Bob: {GardenManager.GardenStats(bob.plants).garden_score()}")
    print(f"Total gardens managed: {len(GardenManager.gardens)}")
