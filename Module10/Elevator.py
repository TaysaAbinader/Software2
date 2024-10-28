class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self, floor):
        while floor != self.current_floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor + 1 <= self.top_floor:
            previous_floor = self.current_floor
            self.current_floor += 1
            print(f"{previous_floor} > floor_up > {self.current_floor}")

    def floor_down(self):
        if self.current_floor -1 >= self.bottom_floor:
            previous_floor = self.current_floor
            self.current_floor -= 1
            print(f"{previous_floor} > floor_down > {self.current_floor}")


h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)


