import random
from prettytable import PrettyTable

class Car:
    def __init__(self, registration,  max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
            self.current_speed += speed_change
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
            elif self.current_speed < 0:
                self.current_speed = 0

    def drive_for_one_hour(self):
        self.travelled_distance += self.current_speed

class Race:
    def __init__(self, name, distance_km, race_list):
        self.distance_km = distance_km
        self.race_list = race_list
        self.table = PrettyTable()
        self.table.title = name
        self.table.field_names = ["Registration", "Max. Speed", "Current Speed", "Travelled Distance"]

    def hour_passes(self):
        for car in self.race_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive_for_one_hour()

    def print_status(self):
        for car in self.race_list:
            self.table.add_row([car.registration, car.max_speed, car.current_speed, car.travelled_distance])
        print(self.table)

    def race_finished(self):
        for car in self.race_list:
            if car.travelled_distance >= self.distance_km:
                return True
        return False

race_list = []

for i in range (10):
    registration = f"ABC-" + str(i+1)
    max_speed = random.randint(100, 200)
    car = Car(registration, max_speed)
    race_list.append(car)

race1 = Race("Grand Demolition Derby", 8000, race_list)

while race1.race_finished() != True:
    race1.hour_passes()
race1.print_status()

