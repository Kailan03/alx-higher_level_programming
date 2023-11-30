#!/usr/bin/python3
def pow(a, b):
   if b == 0:
    return 1
result = 1
# Use a loop to multiply a by itself b times
        for _ in range(b):
            result *= a
            return result
