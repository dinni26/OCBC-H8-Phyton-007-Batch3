print('========CONTOH 1========')
# Function
def nama_fungsi(parameter):
    pass

# Define Class
class Dog:
    #pass

    def __init__(self, name, age):
        # atribut = value (dari parameter)
        self.name = name
        self.age = age
    
    # IDEM (atas & bawah)

    # def __init__(self, inputted_name, inputted_age):
        # atribut = value (dari parameter)
        # self.name = inputted_name 
        # self.age = inputted_age
        
        # self.name = 'Miles'
        # self.age = '4'

# Instantianting
dog1 = Dog('Miles', 2)
dog2 = Dog('Abby', 2)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

print('aman')


