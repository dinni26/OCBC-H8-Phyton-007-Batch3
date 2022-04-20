#Generator
def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

# print(my_generator())
# print(next(my_generator()))

for char in my_generator():
  print(char)

def counter_generator(low, high): # 2 || 5, 10
    while low <= high:            # 3 || 5 6 7 8 9  10 11 x stopp
       yield low                  # 4 || 5 6 7 8 9  10
       low += 1                   # 6 || 6 7 8 9 10 11
 
for i in counter_generator(5,10): # 1 ||
  print(i, end=' ')               # 5 || .6. || .7.  || .8. || .9. || .10.

# ngeload infinite angka = ctrl+c (stop)
for i in infinite_sequence():
  print(i, end=" ")




