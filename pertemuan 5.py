Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'apple'
b = 'banana'
print (a == b)
False
print (a<b)
True
a = 'coconut'
print (a<b)
False
print (a>b)
True
for ch in b:print (ch)

b
a
n
a
n
a
for ch in b:print (ch, end= '')

banana
noVowels - ''
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    noVowels - ''
NameError: name 'noVowels' is not defined
noVowels = ''
for ch in 'Hi there!':
    if not ch in('a', 'e', 'i', 'o', 'u',
                 'A', 'E', 'I', 'O', 'U')
    
SyntaxError: expected ':'
for ch in 'Hi there!':
    if not ch in 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        
SyntaxError: unmatched ')'
for ch in 'Hi there!':
    if not ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        noVowels += ch
print(noVowels)
SyntaxError: invalid syntax
for ch in 'Hi there!':
    if not ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        noVowels += ch
    print(noVowels)

    
H
H
H 
H t
H th
H th
H thr
H thr
H thr!
print(noVowels)
H thr!
b = 'saya sedang belajar dengan teman di rumah dan ibu sedang menjahit'
for ch in b:
    if not ch in ('dan'):
        print(b)

        
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
saya sedang belajar dengan teman di rumah dan ibu sedang menjahit
'Hi there'[3]
't'
len(b)
65
s = 'Hi there!'
for i in range(len(s)): print(i, s[i])

0 H
1 i
2  
3 t
4 h
5 e
6 r
7 e
8 !
len(s[len(s)-1])
1
print(s)
Hi there!
print(s[len(s) - 1])
!
m = 'mahasiswa'
print(m[-5])
s
print(s,split())
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(s,split())
NameError: name 'split' is not defined
print(s.split())
['Hi', 'there!']
print(ord('A'))
65
print(chr(65))
A
print(chr(99))
c
print(chr(36))
$
source = "I won't be here!"
code = ""
for ch in source:
    code = code + str(ord(ch)) + " "
    print(code)

    
73 
73 32 
73 32 119 
73 32 119 111 
73 32 119 111 110 
73 32 119 111 110 39 
73 32 119 111 110 39 116 
73 32 119 111 110 39 116 32 
73 32 119 111 110 39 116 32 98 
73 32 119 111 110 39 116 32 98 101 
73 32 119 111 110 39 116 32 98 101 32 
73 32 119 111 110 39 116 32 98 101 32 104 
73 32 119 111 110 39 116 32 98 101 32 104 101 
73 32 119 111 110 39 116 32 98 101 32 104 101 114 
73 32 119 111 110 39 116 32 98 101 32 104 101 114 101 
73 32 119 111 110 39 116 32 98 101 32 104 101 114 101 33 
print(chr(73, 32, 119, 111))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(chr(73, 32, 119, 111))
TypeError: chr() takes exactly one argument (4 given)
print(chr(73))
I
for ascii in code.split(): print(ascii)

73
32
119
111
110
39
116
32
98
101
32
104
101
114
101
33
source = ''
source = ""
for ascii in code.split():
    source += chr(int(ascii))
    print(source)

    
I
I 
I w
I wo
I won
I won'
I won't
I won't 
I won't b
I won't be
I won't be 
I won't be h
I won't be he
I won't be her
I won't be here
I won't be here!
for ascii in code.split(): print(ascii)

73
32
119
111
110
39
116
32
98
101
32
104
101
114
101
33
filename = input('Enter a file name:')
Enter a file name:buku
print(filename)
buku
filename = input('Enter a file name:')
Enter a file name:kamus
import os.path
filename = input('Enter a file name: ')
Enter a file name: python break pertemuan 4.py
if not os.path.exists(filename):
    print('Error: the file not exist!')
else:
    myfile = open(filename, 'r')
    print(myfile.read())
    myfile.close()

    
total = 0
count = 0

while True:
    data = input("Enter a score or just return to quit: ")
    if data == " " :
        break
    total += int(data)
    count += 1

if count == 0:
    print("No scores were entered.")
else:
    print("The average is", total / count)

