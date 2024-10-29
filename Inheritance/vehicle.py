class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class SportsItem:
    def __init__(self, weight):
        print("Is a sport item")
        self.weight = weight

    def is_sport_item(self):
        return True

class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsItem.__init__(self, weight)
        self.gears = gears


    def print(self):
        print(self.is_sport_item())
        print(self.speed)
        print(self.weight)


bike = Bicycle(120, 10, 8)
bike.print()


