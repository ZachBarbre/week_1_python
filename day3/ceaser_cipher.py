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
        decrypt()
    else:
        print("this should not display")

def encrypt(shift, message):
    print('encrypt')

def decrypt():
    print('decrypt')

