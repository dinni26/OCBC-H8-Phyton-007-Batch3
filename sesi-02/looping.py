print('Looping')
print('\n===Contoh-1===')
n = 5
while n > 0:     # 5 4 3 2 1 0 ==> 0 > 0 False? Maka Stop
    # n = n - 1
    n -= 1       # 4 3 2 1 0
    print(n)     # 4 3 2 1 0

print('==>')
i = 1
while i < 6:     # 1 2 3 4 5 6 ==> 6 > 6? False maka stop
    print(i)     # 1 2 3 4 5
    i += 1       # 2 3 4 5 6

print('\n===Contoh-2===')
n = 5
while n > 0:                        # 5         4           3
    n -= 1                          # 4         3           2
    if n == 2:                      # False     False       True (Stopped)
        break  # Break Statement    # Skipped   Skipped     Break
    print(n)                        # 4         3
print('Loop ended.')
print('==>')
n = 5
while n > 0:                        # 5 4 3                 2 1 0 > 0 ? False maka stop
    n -= 1                          # 4 3 2                 1 0 
    if n == 2:                      # x x n == 2 ? True     x x
        continue                    # Continue         
    print(n)                        # 4 3 ..                1 0
print('Loop ended.')

print('\n===Contoh-3===')
n = 5
while n > 0:    # 5 4 3 2 1 0 stopped
    n -= 1      # 4 3 2 1 0
    print(n)    # 4 3 2 1 0
else:
    print('Loop done.')

print('==>')
n = 5
while n > 0:    # 5 4 3 2 == 2 ? stopped
    n -= 1      # 4 3 2
    print(n)    # 4 3 2
    if n == 2:
        break
else:
    print('Loop done.')

# while break else
keyword = 'ab'
fruits = ['aa','ab','ac','ad','ae','af']
n = 0
while n < len (fruits):    # 5 4 3 2 == 2 ? stopped
    if keyword == fruits[n]:
        print('Found in index ', n)
        break
    n += 1
else: # muncul kalau 'aj' tidak ketemu
    print('Loop done.')
    print('Could Not Be Found Any Index.')

print('\n===Contoh-4===')
age = 25
gender = 'M'
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

print('==>')
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))

    b = ['baz', 'qux']

    while len(b):
        print('>', b.pop(0))

print('\n===Contoh-5===')
n = 5
while n > 0:
    n -= 1
    print(n)

print('\n===Contoh-6===')
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

print('==>')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    #keys = foo , bar , baz
    print(k)

print('==>')
for k in d:
    #numb = 1 , 2 , 3
    print(d[k])

print('==>')
for k in d.values():
    #values = 1 , 2 , 3
    print(k)

print('==>')
for k, v in d.items():
    #items = all 
    print(k, ":", v)

print('\n===Contoh-8===')
for n in (0, 1, 2, 3, 4):
    print(n)

# IDEM CODE ATAS
print('==>')
x = range(5) # dimulai dari 0
for n in x:
    print(n)

print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# for else
print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

# for break else
print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break   # break stop di foo
  print(i)
else:
  print('Done.') 





