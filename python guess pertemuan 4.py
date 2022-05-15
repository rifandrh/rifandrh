import math

x = float(input("Enter a number: "))
count = int(input("Enter the number of iterations: "))

guess = x/2
i = 0
while i < count:
    guess = (guess + x / guess) / 2
    i += 1
print("Guess: %0.15f" % guess)
print("Actual: %0.15f" % math.sqrt(x))
