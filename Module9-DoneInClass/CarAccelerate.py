class Car:
    def __init__(self, registration, max_speed, current_speed, odometer):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self, acce_speed):
        self.current_speed = min(max(self.current_speed + acce_speed, 0), self.max.speed)


if __name__== "__main__":
    tesla = Car("ABC 123", 142)

    tesla.accelerate(30)
    tesla.accelerate(50)
    tesla.accelerate(70)
    print(f"Current speed: {tesla.current_speed} km/h")
    tesla.accelerate(-200)
    print(f"Current speed: {tesla.current_speed} Km/h")
