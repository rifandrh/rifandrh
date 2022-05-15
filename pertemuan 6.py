Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(2 ** 2)
4
print(sqr(2))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(sqr(2))
NameError: name 'sqr' is not defined. Did you mean: 'str'?
print(sqr(3))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(sqr(3))
NameError: name 'sqr' is not defined. Did you mean: 'str'?
a = sqr(4)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a = sqr(4)
NameError: name 'sqr' is not defined. Did you mean: 'str'?
import math
c = math.sqrt(a+b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c = math.sqrt(a+b)
NameError: name 'a' is not defined
import math
a = sqr(4)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a = sqr(4)
NameError: name 'sqr' is not defined. Did you mean: 'str'?
b = sqr(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b = sqr(3)
NameError: name 'sqr' is not defined. Did you mean: 'str'?
print(c)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined
def kali(x):
    """Mengkalikan sebuah value dengan angka 5"""
    return x * 5

print(kali(5))
25
help(kali)
Help on function kali in module __main__:

kali(x)
    Mengkalikan sebuah value dengan angka 5

help(sqr)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    help(sqr)
NameError: name 'sqr' is not defined. Did you mean: 'str'?
help(str)

def sqr(n):
    return n ** 2

print(2 ** 2)
4
print(sqr(2))
4
print(sqr(3))
9
a = sqr(4)
b = sqr(3)
c = math.sqrt(a+b)
print(c)
5.0

======================= RESTART: Shell ======================
help(kali)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    help(kali)
NameError: name 'kali' is not defined
def getValidInteger(prompt, lower,upper):
    """ Repeat inputs"""
    while True:
        number = int(input(prompt))
        if number <lower or number> upper
        
SyntaxError: expected ':'
def getValidInteger(prompt, lower,upper):
    """ Repeat inputs"""
    while True:
        number = int(input(prompt))
        if number <lower or number> upper:
            print('Error:number must range from' +\str(lower) + 'sampai'+str(upper)
                  
SyntaxError: unexpected character after line continuation character
def getValidInteger(prompt, lower,upper):
    """ Repeat inputs"""
    while True:
        number = int(input(prompt))
        if number <lower or number> upper:
            print('Error:number must range from' +\
                  str(lower) + 'sampai'+str(upper)
        else:
            return number
help (getValidInteger)
help(getValidInteger)
rate = getValidInteger("Enter the rate: ", 1, 100)
print(getValidInteger))
SyntaxError: invalid syntax
help(getValidInteger)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    help(getValidInteger)
NameError: name 'getValidInteger' is not defined
rate = getValidInteger("Enter the rate: ", 1, 100)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    rate = getValidInteger("Enter the rate: ", 1, 100)
NameError: name 'getValidInteger' is not defined
def getValidInteger(prompt, lower,upper):
    while True:
        number = int(input(prompt))

help (getValidInteger)
Help on function getValidInteger in module __main__:

getValidInteger(prompt, lower, upper)

rate = getValidInteger("Enter the rate: ", 1, 100)
Enter the rate: 20
Enter the rate: 1
Enter the rate: 100
Enter the rate: 30
Enter the rate: 101
Enter the rate: 0
Enter the rate: 30
Enter the rate: 
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    rate = getValidInteger("Enter the rate: ", 1, 100)
  File "<pyshell#122>", line 3, in getValidInteger
    number = int(input(prompt))
ValueError: invalid literal for int() with base 10: ''
def encrypt(source):
    """Builds and returns an encrypted version of
    the source string."""
    code = ""
    for ch in source:
        code = code + str(ord(ch)) + " "
    return code

help(encrypt)
Help on function encrypt in module __main__:

encrypt(source)
    Builds and returns an encrypted version of
    the source string.

print(encrypt('Saya sedang mengajar'))
83 97 121 97 32 115 101 100 97 110 103 32 109 101 110 103 97 106 97 114 
def decrypt(code):
    """Builds and returns a decrypted version of the code string."""
    source = ""
    for word in code.split():
        source = source + chr(int(word))
    return source

help(decrypt)
Help on function decrypt in module __main__:

decrypt(code)
    Builds and returns a decrypted version of the code string.

print(decrypt(83,97))
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    print(decrypt(83,97))
TypeError: decrypt() takes 1 positional argument but 2 were given
print(decrypt(83))
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    print(decrypt(83))
  File "<pyshell#141>", line 4, in decrypt
    for word in code.split():
AttributeError: 'int' object has no attribute 'split'
print(decrypt(encrypt('Exam'))
print(decrypt(encrypt('Exam')))
print(decrypt(encrypt('Exam')
              
SyntaxError: invalid syntax. Perhaps you forgot a comma?
math.sqrt(2)
              
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    math.sqrt(2)
NameError: name 'math' is not defined
def sqr(n):
    return n ** 2

import math
math.sqrt(2)
1.4142135623730951
def main():
    radius = float(input('Enter the radius: "))
                         
SyntaxError: unterminated string literal (detected at line 2)
def main():
    radius = float(input('Enter the radius: ')
    area = math.pi * radius ** 2
                   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def main():
    radius = float(input('Enter the radius: '))
    area = math.pi * radius ** 2
    print('The area is', area, 'square units')

    
main()
Enter the radius: 10
The area is 314.1592653589793 square units
main()
Enter the radius: -3
The area is 28.274333882308138 square units
import math
def main():
    radius = float(input('Enter the radius: '))
    area = math.pi * radius ** 2
    print('The area is', area, 'square units')

    
if __name__ == '__main__':
    main()

    
Enter the radius: 5
The area is 78.53981633974483 square units
a = [1, 2, 3]
a[1] = 5
print(a[1])
5
list(a)
[1, 5, 3]
a[2]=7
list(a)
[1, 5, 7]
b = ['apple','banana','mango']
b[2]='durian'
list(b)
['apple', 'banana', 'durian']
b[0:1] = ['coconut','jeruk']
list(b)
['coconut', 'jeruk', 'banana', 'durian']
