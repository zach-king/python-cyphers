# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = input("Enter cypertext: ")

LETTERS = '''
!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''


# Try every possible key (brute force)
for key in range(len(LETTERS)):
    # Clear translated
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) 
            num -= key

            # Handle wrap-around
            if num < 0:
                num += len(LETTERS)

            # Add number's symbol at end of translated
            translated += LETTERS[num]

        else:
            translated += symbol

    # Display current key and its decryption
    print('Key #%s: %s' % (key, translated))
