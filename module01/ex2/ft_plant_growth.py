class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, growth: int) -> None:
        self.height += growth

    def age_one_day(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    days = 7

    print("=== Day 1 ===")
    print(rose.get_info())

    for day in range(2, days + 1):
        rose.grow(1)
        rose.age_one_day()

    print(f"=== Day {days} ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")
