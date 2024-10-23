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

registration = input("Registration number: ")
max_speed = int(input("Maximum speed (Km/h): "))
testcar = Car(registration, max_speed)
testcar.accelerate(30)
print(f"Car plate: {testcar.registration}, current speed: {testcar.current_speed}")
testcar.accelerate(70)
print(f"Car plate: {testcar.registration}, current speed: {testcar.current_speed}")
testcar.accelerate(50)
print(f"Car plate: {testcar.registration}, current speed: {testcar.current_speed}")
testcar.accelerate(-200)
print(f"Car plate: {testcar.registration}, current speed: {testcar.current_speed}")


