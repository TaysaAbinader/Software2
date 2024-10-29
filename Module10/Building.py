class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self,floor):
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
        if self.current_floor - 1 >= self.bottom_floor:
            previous_floor = self.current_floor
            self.current_floor -= 1
            print(f"{previous_floor} > floor_down > {self.current_floor}")

            
class Building:
    def __init__(self, lowest_floor, highest_floor, elevator_quantity):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.elevator_quantity = elevator_quantity
        self.list_elevators = []
        for i in range(self.elevator_quantity):
            self.list_elevators.append(Elevator(lowest_floor, highest_floor))

    def run_elevator(self, elevator_id, floor):
        self.list_elevators[elevator_id].go_to_floor(floor)
        print (f"Elevator {elevator_id}, floor {floor}")

building1 = Building(1,10,4 )
building1.run_elevator(3, 10)








