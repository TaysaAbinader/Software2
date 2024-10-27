class Elevator:
    def __init__(self):
        self.bottom_floor = 1
        self.top_floor = 10

    def go_to_floor(self, floor):
        self.floor = floor
        if self.floor > self.bottom_floor:
            self.floor_up()
            self.floor = self.
        elif self.floor < self.top_floor:
            self.floor_down()

    def floor_up(self):
        if self.floor > self.bottom_floor:
            for i in range(self.floor):
                print(f"Floor {self.bottom_floor + i}")
                self.floor = self.top_floor

    def floor_down(self):
        if self.floor < self.top_floor:
            for i in range(self.floor):
                print(f"Floor {self.top_floor - i}")
                self.floor = self.bottom_floor

h = Elevator()
floor = int(input("What floor you want to go? "))
h.go_to_floor(floor)


