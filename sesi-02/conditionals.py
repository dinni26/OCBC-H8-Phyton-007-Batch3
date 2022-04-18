print('Conditions, Control Flow')
print('\n===Contoh-1===')
x = 0
y = 5

if x < y:                            # Truthy
    print('yes 1')

if y < x:                            # Falsy
    print('yes 2')

if x:                                # Falsy
    print('yes 3')

if y:                                # Truthy
    print('yes 4')

if 'aul' in 'grault':                # Truthy
    print('yes aul in grault')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes quux in array')

weather = 'nice'
weather = 'not so nice'
# nice == nice? True
# not so nice -- nice? False
if weather == 'nice'
    print('Mow The Lawn')
    print('Weed The Garden')
    print('Take The Dog For A Walk')   
print('some following statements ....') 

print('\n===Contoh-2===')
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After conditional')

print('\n===Contoh-3===')
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:         # x
    print('Outer condition is true')       # x

    if 10 > 20:                            # x
        print('Inner condition 1')                # x

    print('Between inner conditions')      # x

    if 10 < 20:  # x
        print('Inner condition 2')         # x

    print('End of outer condition')        # x
print('After outer condition')             # x

print('\n===Contoh-4===')
x = 20

if x < 50: #Output
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

print('==>')
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else: #Output
    print('(second suite)')
    print('x is large')

print('==>')
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else: #Output
    print("uang tidak cukup")

print('\n===Contoh-5===')
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else: #Output
    print("uang tidak cukup")

print('==>')
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

print('==>')
if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

print('\n===Contoh-6===')
if 'f' in 'foo':
    print('1')
    print('2')
    print('3')
print('==>')
if 'z' in 'foo': #False karna gaada huruf z di foo
    print('1')
    print('2')
    print('3')
print('==>')

x = 2
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
print('==>')

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
print('==>')

print('\n===Contoh-7===')
raining = False #False + False = True
print("Let's go to the", 'beach' if not raining else 'library')
print('==>')
raining = True #False + True = False
print("Let's go to the", 'beach' if not raining else 'library')
print('==>')

age = 12
s = 'age is teen' if age < 21 else 'age is adult'
print(s) #age is teen 12 < 21
print('==>')
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no') #No 

print('\n===Contoh-8===')
a = 99
b = 23
if a > b: #True
    m = a
else:
    m = b
print (m)

print('\n===Contoh-9===')
# kalau gaada (pass) akan eror
if True:
    pass
print('foo')

