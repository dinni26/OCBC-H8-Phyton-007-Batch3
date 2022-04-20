print('========CONTOH 1========')
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        #Instance Atribute
        self.name = name
        self.age = age

     # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
        #return self.name + ' is ' + str(self.age) + ' years old'

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
        #return self.name + ' says ' + sound

# Instantianting
dog1 = Dog('Miles', 2)
dog2 = Dog('Abby', 1)
# print(dog1.name, dog1.age, dog1.species)
# print(dog2.name, dog2.age, dog2.species)

dog3 = Dog('','')
# dog3 = Dog() #eror
# print(dog3.name, dog3.age, dog3.species)

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
# # Print Name
# print(buddy.name)
# print(miles.name)
# # Print Ages
# print(buddy.age)
# print(miles.age)
# # Print Species
# print(buddy.species)
# print(miles.species)

description_of_buddy = buddy.description()
print(description_of_buddy)
# IDEM (atas & bawah)
print(buddy.description())
print(dog1.description())
print(dog2.description())

sound_of_buddy = buddy.speak('Woof Woof')
print(sound_of_buddy)
# Perintah bisa atas atau bawah
print(miles.speak("Bow Wow"))   
