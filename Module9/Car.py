class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

registration = input("Car registration number: ")
max_speed = input("Maximum speed (Km/h): ")
testcar = Car(registration, max_speed)

print(f"Car plate: {testcar.registration}")
print(f"Maximum speed: {testcar.max_speed}")
print(f"Current speed: {testcar.current_speed}")
print(f"Travelled distance: {testcar.travelled_distance}")
