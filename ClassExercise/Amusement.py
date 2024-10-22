class Visitor:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

class Attractions:
   def __init__(self, name:str, min_heigth: int):
       self.visitor_num = 0
       self.name = name
       self.min_height = min_height
   def check_height(self, person:Visitor):
       if person.height >= self.min_height:
            self.visitor_num += 1
           print(f"{person.name}: Welcome Aboard!")
       else:
            print(f"{person.name}: You need to drink more milk! Oopsi")

   def __str__(self):
       return f"{self.name} ({self.visitor_num} visitors)"

helicopter = Attractions("Helicopter Run", 120)
emmi = Visitor("Emmi", 158)

helicopter.check_height(emmi)

print(helicopter)


name = input("Type your name")
height = input("Type your height")

Attractions.minimun_height(Visitor, height)


