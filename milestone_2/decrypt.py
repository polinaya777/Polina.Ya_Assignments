key = int(input('Enter key: '))
message = input('Enter message: ')

def decrypt(message):
    decrypted_message = ''
    for symbol in message:
        if symbol.isupper():
            decrypted_message += chr((ord(symbol) - key))
        elif symbol.islower():
            decrypted_message += chr((ord(symbol) - key))
        else:
            decrypted_message += symbol
    return decrypted_message

print('Decrypted message: ', decrypt(message))