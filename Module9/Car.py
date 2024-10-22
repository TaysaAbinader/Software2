class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_speed = 0

registration = input("Car registration number: ")
max_speed = input("Maximum speed (km/h): ")
car = Car(registration, max_speed)

print(f"Car plate: {car.registration}, maximum speed {car.max_speed}, current speed {car.current_speed}, travelled speed: {car.travelled_speed}.")

