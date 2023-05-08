
class Planet:

    def __init__(self, name, place, temp):
        self.name = name
        self.place = place
        self.temp = temp

class Planet1(Planet):

    def intro(self):
        print(f"{self.name} - {self.place}  place to the sun| |temperature {self.temp}")

class Planet2(Planet):
    def intro(self):
        print(f"{self.name} - {self.place}  place to the sun| |temperature {self.temp}" )        
class Planet3(Planet):
    def intro(self):
        print(f"{self.name} - {self.place}  place to the sun| |temperature {self.temp} ")
class Planet4(Planet):
    def intro(self):
        print(f"{self.name} - {self.place}  place to the sun| |temperature {self.temp} ")

person = Planet1("Mercury", "|1", "-190 - 700°C |" )
person.intro()

person = Planet2("Venus", "|2", "-2 - 470°C |")
person.intro()

person = Planet3("Earth", "|3", "-90 - 6°C |")
person.intro()

person = Planet4("Mars", "|4", "-90 - 6°C |")
person.intro()
