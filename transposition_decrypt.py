# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math, pyperclip

def main():
    message = input("Enter message: ")
    key = int(input("Enter key: "))

    plaintext = decrypt_message(key, message)

    # Print with a | after it in case there are spaces at the end
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    num_of_columns = math.ceil(len(message) / key)
    
    # The number of "rows" we'll need in our grid:
    num_of_rows = key

    # The number of "shaded boxes" (unused cells at end of grid):
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    # Each string in plaintext represents a column in the grid
    plaintext = [''] * num_of_columns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we hit a shaded box,
        # go back to the first column and next row
        if (col == num_of_columns) or (col == num_of_columns - 1 and
            row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


if __name__ == '__main__':
    main()

