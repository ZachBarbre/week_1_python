encrypted_phrase = input("Encrypyed Message: ")
unencryped_phrase = ''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_alphabet = 'nopqrstuvwxyzabcdefghijklm'

for encrypt_letter in encrypted_phrase:
    if encrypt_letter == ' ':
        unencryped_phrase = unencryped_phrase + encrypt_letter
    else:
        unencrypt_letter = alphabet[encrypted_alphabet.rfind(encrypt_letter)]
        unencryped_phrase = unencryped_phrase + unencrypt_letter

print(unencryped_phrase)

message = 'lbh zhfg hayrnea jung lbh unir yrnearq'

