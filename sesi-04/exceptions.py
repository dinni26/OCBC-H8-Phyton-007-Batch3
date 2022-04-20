try:
    f = open("Hack8_Sample_Text.txt", encoding='utf-8')
    # perform file operations
except FileNotFoundError :
    print('That file is not found')
finally:
    #f.close()
    print('already tried')

x = 10
if x > 5:    
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

print("=====TRY & EXPECT BLOCK=====")
try:    
    with open('file.log') as file:        
        read_data = file.read()
except:    
    print('Could not open file.log')


import sys

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems. Custom exception line 38"
    assert ('win' in sys.platform), "This code runs on Windows only. Custom exception line 38"
    print('Doing something.')

try:
    os_interaction()
except:
    print('ini error')
    print('Windows function was not executed')

print("======================")

try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('could not open file.log')

print(176, 332, 'Asal ngeprint')

print('\n== File nor found! ===')
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

print("======================")
# all
try:
    os_interaction()
    with open('file.log') as file:
        read_data = file.read()
        print(read_data)
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')

#Masuk ke dalam blok except
import sys
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems." # 2 raised an Assertion Error
    assert ('win' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
 
# Have a look at the following example:
try:
    os_interaction() # 1
except AssertionError as error: # 3
    print(error)  #4
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally: # 5
    print('Cleaning up, irrespective of any exceptions.') #6

#Masuk ke blok else
import sys
def os_interaction():
    # assert ('linux' in sys.platform), "Function can only run on Linux systems." # 2 raised an Assertion Error
    assert ('win' in sys.platform), "This code runs on Windows only." # 2
    print('Doing something.')  #3
 
# Have a look at the following example:
try:
    os_interaction()  #1
except AssertionError as error:
    print(error)
else: #4
    try: #5
        with open('file.log') as file: #6
            read_data = file.read()
    except FileNotFoundError as fnf_error: #7
        print(fnf_error) #8
finally: # 9
    print('Cleaning up, irrespective of any exceptions.')  #10


