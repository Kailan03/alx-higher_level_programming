#!/usr/bin/python3
def pow(a, b):
   if b == 0:
    return 1
result = 1
for _ in range(b):
    result *= a
return result
