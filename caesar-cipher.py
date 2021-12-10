# Learned something new today 2021-12-10
# ord(character) = returns unicode's numeric representation of the character
# chr(ord) = returns the character that corresponds to unicode's numeric representation
# ord(A) = 65
# chr(97) = a

alphabet = [chr(i) for i in range(97,123)]
alphabetUpperCase = [chr(i) for i in range(65,91)]

def run():
    invalidInput = True
    while invalidInput:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            invalidInput = False
        else:
            print("Invalid input! Try again.")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text,shift)
    else:
        decrypt(text,shift)

def encrypt(text,shift):
    plainText = text
    cipherText = ""
    for i in plainText:
        # print(f"Encrpyting '{i}'")
        if not(i.isalpha()):
            cipherText += i
        else:
            currentIndex = alphabet.index(i.lower())
            shiftedIndex = (currentIndex + shift) % 26
            if i.isupper():
                cipherText += alphabet[shiftedIndex].upper()
            else:
                cipherText += alphabet[shiftedIndex]
    print(cipherText)
    return None

def decrypt(text,shift):
    decryptText = text
    plainText = ""
    for i in decryptText:
        # print(f"Decrpyting '{i}'")
        if not(i.isalpha()):
            plainText += i
        else:
            currentIndex = alphabet.index(i.lower())
            shiftedIndex = (currentIndex - shift) % 26
            if i.isupper():
                plainText += alphabet[shiftedIndex].upper()
            else:
                plainText += alphabet[shiftedIndex]
    print(plainText)

if __name__ == "__main__":
    run()