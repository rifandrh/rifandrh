Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
verbs = ['hit', 'threw', 'pushed', 'ate', 'dragged', 'jumped']

import random
print(random.choice(verbs))
hit
print(random.choice(verbs))
jumped
nouns = ['bat','boy','girl','dog','cat','chair','fence','table','computer','cake','field','pie']
sentence = nounphrase verbphrase
SyntaxError: invalid syntax
def sentence():
    return nounphrase() + ' ' + verbphrase()

def nounphrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

for x in range(10): print(sentence())

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for x in range(10): print(sentence())
  File "<pyshell#9>", line 2, in sentence
    return nounphrase() + ' ' + verbphrase()
  File "<pyshell#12>", line 2, in nounphrase
    return random.choice(articles) + ' ' + random.choice(nouns)
NameError: name 'articles' is not defined

===================== RESTART: Shell ====================
import random
articles = ['a', 'the']
nouns = ['bat','boy','girl','dog','cat','chair']
def sentence():
    return nounphrase()

def nounphrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

for x in range(5): print(sentence())

a boy
the chair
a dog
a cat
a boy
for x in range(10): print(sentence())

a girl
the bat
a bat
a bat
the dog
a dog
a chair
a cat
a girl
a chair
hexdigits = ('A': 10, 'B': 11)
SyntaxError: invalid syntax
hexdigits = ('A':10, 'B':11)
SyntaxError: invalid syntax
hexdigits = {'A':10, 'B':11)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
hexdigits = {'A':10, 'B':11}
database = {'name':'Ken', 'age':67}
database{'name'}
SyntaxError: invalid syntax
database{'name'}
SyntaxError: invalid syntax
database['name']
'Ken'
hexdigits['S']
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    hexdigits['S']
KeyError: 'S'
hexdigits['B']
11
database = {'name':'Ken', 'age':67, 'name':'Ken'}
database['name']
'Ken'
if 'hair color' in database:
    database['hair color']

    
if 'name' in database:
    database['name']

    
'Ken'
database.get('hair color', None)
database.get('age', None)
67
database = {'name':'Ken', 'age':67, 'occupation':'Teacher'}
for key in database:
    print(key,database[key])

    
name Ken
age 67
occupation Teacher
database = {'name':'Ken', 'age':67, 'gender':'H', 'occupation':'Teacher'}
for key in database:
    print(key,database[key])

    
name Ken
age 67
gender H
occupation Teacher
database = {'name':'Ken', 'age':67, 'gender':'M', 'occupation':'Teacher'}
for key in database:
    print(key,database[key])

    
name Ken
age 67
gender M
occupation Teacher
database['hair color'] = 'gray'
for key in database:
    print(key,database[key])

    
name Ken
age 67
gender M
occupation Teacher
hair color gray
database['hair color'] = 'black'
for key in database:
    print(key,database[key])

    
name Ken
age 67
gender M
occupation Teacher
hair color black
database.pop('age',None)
67
database
{'name': 'Ken', 'gender': 'M', 'occupation': 'Teacher', 'hair color': 'black'}
