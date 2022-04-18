print ('hello world')

print(123123123123123123123123123123123123123123123123 + 1)
print(type(123123123123123123123123123123123123123123123123 + 1))

print(4.2)

print(type(4.2))

print(4.)

print(.2)

print(.4e7)

print(4.2e-4)

print("Hacktiv8")
print(type("Hacktiv8"))

print('')
print(type(''))

print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

print('This string contains a double quote (\") character.')
print("This string contains a single quote (\') character.")

print(True)
print(type(True))

print(type(True))
print(type(False))

var = 23.5
print(var)
print(type(var))

var = "Now I'm a String"
print(var)
print(type(var))

name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
has_5laptops = False
print(has_5laptops)

# 9_kepala_naga = True 

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)


a = 10
b = 20
print(a + b)

a = 10
b = 20
print(a + b – 5)

a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #integer division atau floor division (pembulatan koma)
print(a % b)
print(a ** b) #pangkat 2

a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)

s = 'foo'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4) #nilai s diulang 4 kali

s = 'foo'
t = 'bar'
u = 'baz'
# + and * Operators
print(s + t )
print(s + t + u)
print('Hactiv 8' + 'Inalum')

s = 'foo.'
print(s * 4)

s = 'us'
print(s in 'That Food For Us')
print(s in 'That Food For Us')

#Case Conversion
s = 'HacTIV8'
print(s.capitalize())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.upper())

a = ['foo', 'bar', 'baz', 'qux']
print(a)
print(type(a))

a = ['foo', 'bar', 'baz', 'qux']
b = ['baz', 'qux', 'bar', 'foo']
print(a == b)

a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[5])
print(a[-1]) #-1 dari belakang yaitu corge
print(a[-6])

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
#      0      1      2      3       4        5
print (a[2:5]) #yang tampil 2,3,4
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a + ['grault', 'garply'])
print(a)
a = a * 2
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(len(a))
print(min(a))
print(max(a))

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
a[2] = 10
a[-1] = 20
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a)
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(type(t))
print(t[0])
print(t[-1])

# packing and unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
t4 = ('foo', 'bar', 'baz', 'qux')
(s1, s2, s3, s4) = t4
print(s1) #s1 = foo
print(type(s))

t4 = ('aa','bb','cc')
print(t4)

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
print(MLB_team)
print(type(MLB_team))
print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])

#Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

# If you want to update an entry, you can just assign a new value to an existing key:
MLB_team['Seattle'] = 'Seahawks'
print(MLB_team)

# To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Seattle']

person = {}
type(person)
 
person['fname'] = 'Hack'
person['lname'] = 'Inalum'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey'] # list
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'} # dictionary

print(person['fname'])
print(person['lname'])
print(person['children'])
print(person['children'][1])
print(person['pets'])
print(person['pets']['cat'])

# Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30}
# items = a,10 dll
print(d.items()) 
# keys = a,b,c
print(d.keys())
# values = 10,20,30
print(d.values())

#PYTHON STATEMENT
print('Hello, World!')

x = [1, 2, 3]
print(x)

person1_age = 42
person2_age = 16
person3_age = 71
print(person1_age, person2_age, person3_age)

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age

#IDEM = CARA AGAR LEBIH MUDAH DI BACA
someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)       #True
    or (person2_age >= 18 and person2_age <= 65)    #False
    or (person3_age >= 18 and person3_age <= 65)    #False
) #True or .. false or .. false

print(someone_is_of_working_age)

