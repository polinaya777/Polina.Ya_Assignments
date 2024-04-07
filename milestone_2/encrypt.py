key = int(input('Enter key: '))
message = input('Enter message: ')

def encrypt(message):
    encrypted_message = ''
    for symbol in message:
        if symbol.isupper():
            encrypted_message += chr((ord(symbol) + key))
        elif symbol.islower():
            encrypted_message += chr((ord(symbol) + key))
        else:
            encrypted_message += symbol
    return encrypted_message

print('Encrypted message: ', encrypt(message))