class Car:
    def __init__(self, registration,  max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, speed_change):
        self.speed_change = speed_change
        self.current_speed += self.speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
        return self.current_speed

    def drive(self, driven_hours):
        self.travelled_distance += self.speed_change*driven_hours
        return self.travelled_distance

registration = input("Registration number: ")
max_speed = int(input("Maximum speed (Km/h): "))
speed_change = int(input("What is your velocity (km/h)? "))
driven_hours = float(input("How many hours were driven? "))
testcar = Car(registration, max_speed)
testcar.accelerate(speed_change)
testcar.drive(driven_hours)
print(f"Car plate: {testcar.registration}, travelled distance: {testcar.travelled_distance}")


