class SecurePlant:
    def __init__(self, name: str):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")
