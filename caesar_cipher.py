# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted
message = input("Enter message: ")

# The ecrytpion/decryption key
key = int(input("Enter key: "))

# Encyprt or Decrypt?
mode = input("1) Encrypt\n2) Decrypt\n: ")

# All possible symbols that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Stores the encrypted/decrypted form of message
translated = ''

# Capitalize message
message = message.upper()

# Encyprt/Decrypt each symbol in message
for symbol in message:
    if symbol in LETTERS:
        # Get the encrypted/decrypted number for this symbol
        num = LETTERS.find(symbol)
        if mode == '1' or mode.lower() == 'encrypt':
            num += key
        elif mode == '2' or mode.lower() == 'decrypt':
            num -= key

        # Handle the wrap-around if num is > len(LETTERS)
        if num >= len(LETTERS):
            num -= len(LETTERS)
        elif num < 0:
            num += len(LETTERS)

        # Add encrypted/decrypted number's symbol to translated
        translated += LETTERS[num]

    else:
        # Just add the symbol without encrypted/decrypting
        translated += symbol


# Print the encrypted/decrypted string to the screen
print(translated)

# Copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)
