class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0
        self.breed = breed

    def increase_age(self):
        self.age = self.age + 1


dog = Dog("Musti", "Labrador")
dog2 = Dog("Fluffy", "Shetland Pony")

print(f"Dog name: {dog.name}, age {dog.age}, breed {dog.breed}")
print(f"Dog name: {dog2.name}, age {dog.age}, breed {dog.breed}")
dog.increase_age()
print(f"Dog name: {dog.name}, age {dog.age}, breed {dog.breed}")
print(f"Dog name: {dog2.name}, age {dog.age}, breed {dog.breed}")

class Dog:
    created = 0

    def __init__(self, name, breed, age = 0, height = 10):
        self.name = name
        self.breed = breed
        self.bark = ""
        Dog.created = Dog.created + 1

    def increase_age(self, years =1):
        self.age = self.age + years

    def bark (self, count):
        print(f"{self.name} is about to bark")
        for i in range (count):
            print(self.bark)

    def set_sound(self):
        self.sound = sound



print(f"Dog name: {dog2.name}, age {dog2.age}, breed {dog2.breed}")

print(Dog.created)

kennel = [dog, dog2]

dog3 = Dog


for i in range(10):
    dog = Dog(f"Dog{i}", ”shetland pony”, i)
    kennel.append(dog)


print(kennel[1].name)

for dog in kennel:
    dog.increase_age(random.randint(0, 15))

print(f"dogs created: {Dog.created}")

class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item (self, item: str):
        if not item in self.items:
            self.items.append(item)

    def longest_name(self):
        longest = ""
        length_longest = 0
        for intem in self.items:
            if len(item)>




