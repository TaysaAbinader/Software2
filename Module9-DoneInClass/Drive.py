class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self, acce_speed):
        self.current_speed = min(max(self.current_speed + acce_speed, 0), self.max_speed)
        print(self.current_speed)

    def drive(self, hours):
        self.odometer+= self.current_speed*hours


if __name__== "__main__":
    tesla = Car("ABC 123", 142)

    tesla.accelerate(30)
    tesla.accelerate(50)
    tesla.accelerate(70)
    print(f"Current speed: {tesla.current_speed} km/h")
    tesla.accelerate(-200)
    print(f"Current speed: {tesla.current_speed} Km/h")
    tesla.accelerate(60)
    tesla.drive(1.5)
    print(f"Distance travelled: {tesla.odometer}")