Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello')
Hello
print('Hello')
Hello
print('Hello')
Hello
for count in range(5): print('Hello')

Hello
Hello
Hello
Hello
Hello
for hitung in range(3): print('Apa kabar')

Apa kabar
Apa kabar
Apa kabar
for count in range(3):
    print('Hello!')
    print('goodbye')

    
Hello!
goodbye
Hello!
goodbye
Hello!
goodbye
for count in range(5):
    print(count)

    
0
1
2
3
4
list(range(5))
[0, 1, 2, 3, 4]
for count in range(5):
    print(range)

    
<class 'range'>
<class 'range'>
<class 'range'>
<class 'range'>
<class 'range'>
print(print)
<built-in function print>
for hitung in range(3):
    print(hitung +1)

    
1
2
3

========================== RESTART: Shell ==========================
for count in range(1,6):
    print(count)

    
1
2
3
4
5
for count in range(5):
    print(count +1):
        
SyntaxError: invalid syntax
for count in range(5):
    print(count +1)

    
1
2
3
4
5
for count in range(1, 10):
    print('Hasil dari count', count)

    
Hasil dari count 1
Hasil dari count 2
Hasil dari count 3
Hasil dari count 4
Hasil dari count 5
Hasil dari count 6
Hasil dari count 7
Hasil dari count 8
Hasil dari count 9
for count in range(1,11,2):
    print(count)

    
1
3
5
7
9
for count in range(2,10,2):
    print(count)

    
2
4
6
8
list(range(1,6,2))
[1, 3, 5]
for count in range(4,1,-1):
    print(count)

    
4
3
2
total = 0

total=0
for n in range(1,6):
    total=total+n
    print(total)

    
1
3
6
10
15
for n in range(1,6):
    n += n
    print(n)

    
2
4
6
8
10
for n in range(1,6):
    n += 1
    print(n)

    
2
3
4
5
6
total=1
for n in range(1,6):
    total += n
    print(total)

    
2
4
7
11
16
for n in range(1,6):
    total += n
    print(n)

    
1
2
3
4
5
print(total)
31
mulai=5
for n range(1,5):
    
SyntaxError: invalid syntax
for n in range(1,5):
    mulai+=n
    print(n)

    
1
2
3
4
print(mulai)
15
for n in range(1,6):
    product = product * n
    print(product)

    
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    product = product * n
NameError: name 'product' is not defined
product = 1
for n in range(1,6):
    product = product * n
    print(product)

    
1
2
6
24
120
y=0
x=1

========================== RESTART: Shell ==========================
y = 0
k = 1
b = 0
for x in range(1,10):
    y = kx + b
    print(y)

    
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    y = kx + b
NameError: name 'kx' is not defined. Did you mean: 'k'?
for x in range(1,10):
    y = k*x + b
    print(y)

    
1
2
3
4
5
6
7
8
9
initial_balance = 10000
current = initial_balance
rate = 0.06
for i in range(1, 6):
    interest = current * rate
    print('{} {:.2f} {:.2f}'.format(i, current, interest))
    current += interest

total_interest = current - initial_balance
print("Total interest: {:.2f} Total principal: {:.2f}".format(total_interest, current))
SyntaxError: multiple statements found while compiling a single statement


========================== RESTART: Shell ==========================
initial_balance = 10000
current = initial_balance
rate = 0.06
for i in range(1, 6):
    interest = current * rate
    print('{} {:.2f} {:.2f}'.format(i, current, interest))
    current += interest

total_interest = current - initial_balance
print("Total interest: {:.2f} Total principal: {:.2f}".format(total_interest, current))
SyntaxError: multiple statements found while compiling a single statement

intial_balance = 10000
current = initial_balance
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    current = initial_balance
NameError: name 'initial_balance' is not defined. Did you mean: 'intial_balance'?

===================================================================== RESTART: Shell ====================================================================
x=10000
y=0.06
z=0
for untung in range (1,6):
    z = x + untung * x * y
    print (z)
    
SyntaxError: multiple statements found while compiling a single statement
x=10000
y=0.06
z=0
for untung in range(1,6):
    z = x + untung * x * y
    print(z)

    
10600.0
11200.0
11800.0
12400.0
13000.0
d=10000
y=6/100
i=0
for n in range(1,6):
    d = d + i
    i = d * y
    print(d)
    print(i)

    
10000
600.0
10600.0
636.0
11236.0
674.16
11910.16
714.6096
12624.7696
757.486176
d=10000
y=6/100
i=0
for n in range(1,6):
    d = d + i
    i = d * y
    print(d)
    print(i)
    
SyntaxError: multiple statements found while compiling a single statement
d=10000
y=6/100
i=0
for n in range(1,6):
    d = d + i
    i = d * y
    print(d)
    print(i)
    i += d

    
10000
600.0
20600.0
1236.0
42436.0
2546.16
87418.16
5245.0896
180081.4096
10804.884576
x=10000
y=0.06
z=0
for profit in range(1,6):
    z=x+profit*x*y
    print(z)

    
10600.0
11200.0
11800.0
12400.0
13000.0
print
<built-in function print>
print(10600)
10600
print(10600+10600*0.06)
11236.0

========================== RESTART: Shell ==========================
principal=10000
rate=.06
term=5
totalinterest=0
for year in range(term):
    interest = principal*rate
    print(round(principal, 2), round(interest, 2))
    principal=principal+interest
    totalinterest=totalinterest+interest
print('Total interest:', round(totalinterest, 2))
SyntaxError: invalid syntax
    print('Total interest:', round(totalinterest, 2))
    
SyntaxError: unexpected indent

principal=10000

rate=.06

term=5

totalinterest=0

for year in range(term):
    interest = principal*rate
    print(round(principal, 2), round(interest, 2))
    principal=principal+interest
    totalinterest=totalinterest+interest
    
SyntaxError: multiple statements found while compiling a single statement
principal=10000
rate=.06
term=5
totalinterest=0
for year in range(term):
    interest = principal*rate
    print(round(principal, 2), round(interest, 2))
    principal=principal+interest
    totalinterest=totalinterest+interest
    print('Total interest:', round(totalinterest, 2))
    print('Total principal:', round(principal, 2))

    
10000 600.0
Total interest: 600.0
Total principal: 10600.0
10600.0 636.0
Total interest: 1236.0
Total principal: 11236.0
11236.0 674.16
Total interest: 1910.16
Total principal: 11910.16
11910.16 714.61
Total interest: 2624.77
Total principal: 12624.77
12624.77 757.49
Total interest: 3382.26
Total principal: 13382.26
