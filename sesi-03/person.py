name = 'zack 123456'
devices = ['laptop', 'smartphone', 'tablet']

def display(arg):
    print(f'arg = {arg}')
    # print('arg = ' + arg)

if (__name__ == '__main__'):                #agar pas import person tidak langsung muncul
    print('Executing as standalone script')

    print(name)
    print(devices)
    print(display('Good Morning'))