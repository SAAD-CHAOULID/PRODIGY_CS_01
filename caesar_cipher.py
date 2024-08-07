
def encrypt(message,shift) :
    encrypted_message = ""
    for letter in message :
        if letter.isalpha() :
            base = 65 if letter.isupper() else 97
            encrypted_letter = chr((ord(letter) - base + shift) % 26 + base)
        else :
            encrypted_letter = letter
        encrypted_message += encrypted_letter
    return encrypted_message

def decrypt(message,shift) :
    decrypted_message = ""
    for letter in message :
        if letter.isalpha() :
            base = 65 if letter.isupper() else 97
            decrypted_letter = chr((ord(letter) - base - shift) % 26 + base)
        else :
            decrypted_letter = letter
        decrypted_message += decrypted_letter
    return decrypted_message

message = input("insert the message you want to encrypt or decrypt : ")
question = ""

while question != 'e' and question != 'd':
    question = input("If you want to encrypt the message, type 'e'. If you want to decrypt it, type 'd': ")

shift = int(input("insert the shift value for the encryption or the decryption : "))


if question == 'e' :
    print("The encrypted message is : ", encrypt(message,shift))
elif question == 'd' :
    print("The decrypted message is : ", decrypt(message,shift))
