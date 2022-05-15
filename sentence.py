Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
articles = ['a', 'the']
nouns = ['bat', 'boy', 'girl', 'dog', 'cat', 'chair']
def sentence():
    return nounphrase()

def nounphrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

for x in range(5): print(sentence())

the dog
the dog
the cat
a cat
a bat
verbs = ['hit', 'threw', 'pushed', 'ate', 'dragged', 'jumped']
def sentence():
    return nounphrase() + ' ' + verbphrase()

def verbphrase():
    random.choice(articles) + ' ' + random.choice(nouns) + random.choice(verbs)

    

for x in range(5): print(sentence())

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for x in range(5): print(sentence())
  File "<pyshell#14>", line 2, in sentence
    return nounphrase() + ' ' + verbphrase()
TypeError: can only concatenate str (not "NoneType") to str
def sentence():
    return nounphrase() + ' ' + verbphrase()

def nounphrase():
    return random.choice(articles) + ' ' + random.choice(nouns)

def verbphrase():
    return random.choice(verbs)

for x in range(5): print(sentence())

a cat jumped
the chair ate
the boy dragged
a dog threw
a dog jumped
