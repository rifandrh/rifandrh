principal = 10000

while True:
    rate = int(input('Enter the interest rate(0-100): '))
    if rate < 0 or rate > 100:
        print('ERROR: Rate must be between 0 and 100!')
    else:
        break
interest = principal * rate / 100
print('Your interest is', interest)
