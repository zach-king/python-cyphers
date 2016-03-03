# Transposition Cipher Test
# http://inventwithpython.com/hacking (BSD Licensed)

import random, sys
import transposition_encrypt as enc
import transposition_decrypt as dec

def main():
    random.seed(42)

    for i in range(20):
        # Generate random messages to test

        # random length
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 20)

        # Convert message to list and shuffle it, then re-string it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i+1, message[:50]))

        # Check all possibile keys for each message
        for key in range(1, len(message)):
            encrypted = enc.encrypt_message(key, message)
            decrypted = dec.decrypt_message(key, encrypted)

            # If the decryption doesn't match the original message, display
            # an error message and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()


