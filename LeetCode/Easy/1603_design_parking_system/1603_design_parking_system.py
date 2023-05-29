from enum import Enum


class CarSize(Enum):
    BIG = 1
    MEDIUM = 2
    SMALL = 3


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def __park_big_car(self):
        if self.big:
            self.big -= 1
            return True
        return False

    def __park_medium_car(self):
        if self.medium:
            self.medium -= 1
            return True
        return False

    def __park_small_car(self):
        if self.small:
            self.small -= 1
            return True
        return False

    def addCar(self, carType: int) -> bool:
        if carType == CarSize.BIG.value:
            return self.__park_big_car()
        elif carType == CarSize.MEDIUM.value:
            return self.__park_medium_car()
        elif carType == CarSize.SMALL.value:
            return self.__park_small_car()


obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
