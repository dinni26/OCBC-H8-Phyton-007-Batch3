'''Read File'''
try:
    f = open("Hack8_Sample_Text.txt", encoding='utf-8')
    print(f.read())
    # perform file operations
finally:
    f.close()

'''Write File'''
# w = write
with open("sample.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
    f.write("Dini")

f = open("sample.txt", 'r', encoding='utf-8')
print(f.read(4))
print(f.read(4))
print(f.read())

#read : print all
print("========================================")
try:
    f = open("Hack8_Sample_Text.txt", 'r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

#readline : print satu per satu dari  txt
print("========================================")
try:
    f = open("Hack8_Sample_Text.txt", 'r', encoding='utf-8')
    print(f.readline())
finally:
    f.close()