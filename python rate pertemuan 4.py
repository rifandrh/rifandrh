principal = 10000
rate = int(input('Enter the interest rate(0-100): '))
if rate < 0 or rate > 100:
    print ('ERROR')
else:
    interest = principal * rate/100
    print('Your interest is', interest)
    
