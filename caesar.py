def encrypt(plain, shift):
    encrypted = ''
    for char in plain:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += str(char)
    return encrypted


def decrypt(plain, shift):
    return encrypt(plain, -shift)


