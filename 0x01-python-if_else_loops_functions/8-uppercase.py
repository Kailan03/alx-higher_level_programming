#!/usr/bin/python3
def uppercase(str):
    #initializing result 
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            # convert charcter to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)
            print(result, end="\n")
