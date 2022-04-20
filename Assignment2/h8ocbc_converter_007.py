'''Program Konversi Suhu Celcius, Kelvin, Fahrenheit'''
'''
Fitur:
    1. Convert from Celcius to Kelvin
    2. Convert from Kelvin to Celcius
    3. Convert from Kelvin and Celcius to Fahrenheit
    4. Convert from Fahrenheit to Kelvin and Celcius 
    5. Perulangan dalam memilih menu
'''

print("============== ASSIGNMENT 2 ==============")
print("========= Dini Tri Widianingsih ==========")
print("============= FSDO003ONL007 ==============")

'''Function untuk convert kelvin ke celcius atau celcius ke kelvin.'''
def convertSuhuTo(suhu, tipe) :
    if (tipe.upper() == 'K') :
        result = suhu + 273.15
    elif (tipe.upper() == 'C') :
        result = suhu - 273.15
    
    return result

'''function toFahrenheit() digunakan untuk mengubah suhu Kelvin dan Celcius ke Fahrenheit.
Terdapat 2 parameter, yaitu kelvin dan celcius :
parameter kelvin untuk menerima value suhu dengan satuan Kelvin.
parameter celcius untuk menerima value suhu dengan satuan Celcius.'''
def toFahrenheit(kelvin, celcius) :
    '''dari kelvin ke fahrenheit'''
    temp = convertSuhuTo(kelvin, 'C') #convert dari kelvin ke celcius
    kelv = (( 9 / 5 ) * temp) + 32

    '''dari celcius ke fahrenheit'''
    celc = (( 9 / 5 ) * celcius) + 32

    print("\nFrom Kelvin to Fahrenheit : ")
    print('Result: ', '{:.3f}°'.format(kelv), 'Fahrenheit')
    
    print("From Celcius to Fahrenheit : ")
    print('Result: ', '{:.3f}°'.format(celc), 'Fahrenheit')


'''function fromFahrenheit() digunakan untuk mengubah suhu Fahrenheit ke Kelvin dan Celcius.
Terdapat parameter, yaitu suhu.'''
def fromFahrenheit(suhu) :
    celc = (suhu - 32) * 5 / 9
    kelv = convertSuhuTo(celc, 'K')

    print("\nFrom Fahrenheit to Kelvin : ")
    print('Result: ', '{:.3f}°'.format(kelv), 'Kelvin')
    print("From Fahrenheit to Celcius : ")
    print('Result: ', '{:.3f}°'.format(celc), 'Celcius')

ulang = True

while (ulang == True) :
    print("Menu :")
    print("1. Convert from Celcius to Kelvin")
    print("2. Convert from Kelvin to Celcius")
    print("3. Convert from Kelvin and Celcius to Fahrenheit")
    print("4. Convert from Fahrenheit to Kelvin and Celcius")
    menu = int(input("Silahkan Pilih Nomor Menu (1 s/d 4) : "))

    print('')
    if (menu == 1) :
        print("1. Convert from Celcius to Kelvin")
        celc = float(input('Masukan suhu (Celcius): '))
        result = convertSuhuTo(celc, 'K')
        print(f'Result: {result}° Kelvin')
    elif (menu == 2) :
        print("2. Convert from Kelvin to Celcius")
        kelv = float(input('Masukan suhu (Kelvin): '))
        result = convertSuhuTo(kelv, 'C')
        print(f'Result: {result}° Celcius')
    elif (menu == 3) :
        print("3. Convert from Kelvin and Celcius to Fahrenheit")
        kelv = float(input('Masukan suhu (Kelvin): '))
        celc = float(input('Masukan suhu (Celcius): '))
        toFahrenheit(kelv, celc)
    elif (menu == 4) :
        print("4. Convert from Fahrenheit to Kelvin and Celcius")
        suhu = float(input('Masukan suhu (Fahrenheit): '))
        fromFahrenheit(suhu)
    else:
        print('Choose right menu!')
    
    if(input('\nBack to Menu [y/n]? ') == 'y'):
        ulang=True
    else:
        ulang=False
        print("TERIMA KASIH!")