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

race = []

for i in range (10):
    registration = f"ABC-" + str(i+1)
    max_speed = random.randint(100, 200)
    car = Car(registration, max_speed)
    race.append(car)

stop_race = False
while stop_race == False:
    for car in race:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive_for_one_hour()
        if car.travelled_distance >= 10000:
            stop_race = True
            break

table = PrettyTable()
table.field_names = ["Registration", "Max. Speed", "Current Speed", "Travelled Distance"]

for car in race:
    table.add_row([car.registration, car.max_speed, car.current_speed, car.travelled_distance])

print(table)