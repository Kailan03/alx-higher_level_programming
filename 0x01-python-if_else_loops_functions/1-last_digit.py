#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# extract last digit
lastDigit = number % 10
# Print the required output
print("Last digit of", number, "is", lastDigit, "and is", end=" ")

if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
