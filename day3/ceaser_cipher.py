def get_input():

    while True:
        encrypt_or_decrypt = input("Encrypt or Decrypt? ").lower()
        if encrypt_or_decrypt == 'encrypt' or encrypt_or_decrypt == 'decrypt':
            break
        else:
            print("Please enter \"encrypt\" or \"decrypt\"")

    while True:
        try:
            shift = int(input("Shift? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    message = input("Message? ")

    if encrypt_or_decrypt == 'encrypt':
        encrypt(shift, message)
    elif encrypt_or_decrypt == 'decrypt':
        decrypt(shift, message)
    else:
        print("this should not display")

def encrypt(shift, message):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_message = ''
    
    for letter in message.lower():
        if letter == ' ' or letter.isdigit():
            encrypt_message += letter
        else:
            encrypt_index = ALPHABET.rindex(letter)
            encrypt_message += ALPHABET[(encrypt_index + shift) % 26]
    return encrypt_message

def decrypt(shift, message):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    decrypt_message = ''
    
    for letter in message.lower():
        if letter == ' ' or letter.isdigit():
            decrypt_message += letter
        else:
            decrypt_index = ALPHABET.rindex(letter)
            decrypt_message += ALPHABET[(decrypt_index - shift) % 26]
    return decrypt_message

print(get_input())