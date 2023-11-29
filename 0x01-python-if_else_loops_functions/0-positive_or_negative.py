#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
# extract the last digit of the number
lastDigit = number % 10
# print the required output
print(lastDigit, end=" ")
if lastDigit > 0:
    print("is positive")
elif lastDigit < 0:
    print("is negative")
else:
    print("is zero")
