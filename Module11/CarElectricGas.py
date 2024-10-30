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
        return self.current_speed

    def drive(self, driven_hours):
        self.travelled_distance += self.current_speed*driven_hours
        return self.travelled_distance

class Electric(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        self.battery_capacity_kwh = battery_capacity
        super().__init__(registration, max_speed)

    def print_info(self):
        print(f"Car: {self.registration}, Odometer: {self.travelled_distance}")

class Gasoline(Car):
    def __init__(self, registration, max_speed, tank_volume):
        self.tank_volume_l = tank_volume
        super().__init__(registration, max_speed)

    def print_info(self):
        print(f"Car: {self.registration}, Odometer: {self.travelled_distance}")

car1 = Electric("ABC - 15", 180, 52.5)
car2 = Gasoline("ACD - 123", 165, 32.3)
car1.accelerate(80)
car2.accelerate(60)
car1.drive(3)
car2.drive(3)
car1.print_info()
car2.print_info()



