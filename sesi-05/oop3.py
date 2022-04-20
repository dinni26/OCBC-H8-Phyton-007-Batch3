class Dog:
    # Class attributes
    # species = "Canis familiaris"
    species = "Canis familiaris 2000"
    fav_meal = "Brand meal 2022"
 
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed
 
    def __init__(self, name, age):
        # Instance attribute
        self.name = name
        self.age = age
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
 
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age} ) #REPR"
 
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old  #STR"
 
class JackRussellTerrier(Dog):
    # kalau didefinisikanya seperti ini
    # JRT ini tu meruapkan child class dari Dog class
    # parent classnya : Dog class
    # pass
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
        # return super().speak()
 
class Dachshund(Dog):
    pass
 
class Bulldog(Dog):
    #pass
    def __init__(self, name, age, weight_in_lbs):
        super().__init__(name, age )
        self.weight_in_lbs = weight_in_lbs
 
# instantiating new instance of Dog class
# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
 
# instantiating new instance of [breed] class
# instantiating new instance of JackRussellTerrier class
# miles = Dog("Miles", 4, "Jack Russell Terrier")
miles = JackRussellTerrier('Miles', 4)
 
# instantiating new instance of [breed] class
# instantiating new instance of Dachshund class
# buddy = Dog("Buddy", 9, "Dachshund")
buddy = Dachshund('Buddy', 9)
 
# instantiating new instance of [breed] class
# instantiating new instance of Bulldog class
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
jack = Bulldog('Jack', 3, 23)
jim = Bulldog('Jim', 5, 48)
 
 
# print(miles.name, miles.age, miles.breed)
# print(buddy.name, buddy.age, buddy.breed)
# print(jack.name, jack.age, jack.breed)
# print(jim.name, jim.age, jim.breed)
 
print(buddy.speak("Yap"))
print(jim.speak("Woof"))
 
print(miles.name, miles.age )
print(buddy.name, buddy.age )
print(jack.name, jack.age)
print(jim.name, jim.age)
 
print(buddy.description())
print(miles.description())
print(jack.description())
print(jim.description())
 
print(miles.species)
print(buddy.species)
print(jack.species)
print(jim.species)
 
print(miles.fav_meal)
print(buddy.fav_meal)
print(jack.fav_meal)
print(jim.fav_meal)

print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))

print(miles.speak("Before Arf"))
print(miles.speak()) #langsung ngambil speak dari class JRT
print(miles.speak("Arf Arf Arf"))
print(miles.speak("Grrr"))

print(jack.__dict__)
print(jim.__dict__)

print('REPR and STR part')
 
print(repr(miles))
print(miles.__repr__())
 
print(str(miles))
print(miles.__str__())

