#!/usr/bin/python3
# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

message = input('Enter message: ') 
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)
