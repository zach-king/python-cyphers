# Transposition Cipher Encryption
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

def main():
    message = input("Enter message: ")
    key = int(input("Enter key: "))

    ciphertext = encrypt_message(key, message)

    # Print the encrypted string in ciphertext to the screen
    # with | after it in case there are spaces at the end
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)


def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    # Loop through each column in ciphertext
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message
        while pointer < len(message):
            # Place the character at pointer in message at the end of the 
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # Move pointer over
            pointer += key

    # Convert the ciphertext list into a single string
    return ''.join(ciphertext)


# If transposition_encrypt.py is run (instead of imported as a module),
# call the main() function
if __name__ == '__main__':
    main()

