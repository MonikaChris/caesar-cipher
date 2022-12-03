import ssl
import nltk
from nltk.corpus import words, names


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


def crack(plain):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("words", quiet=True)
    nltk.download('names', quiet=True)

    word_list = words.words()
    name_list = names.words()

    encodings = []
    percent_words = []

    # Brute force - try all decryption keys, store results
    for i in range(1, 26):
        encodings.append(decrypt(plain.lower(), i))

    # Compare encrypted results to word list to determine percent of words
    for text in encodings:
        hit = 0
        miss = 0

        parsed_text = text.split()
        for word in parsed_text:
            if word.lower() in word_list:
                hit += 1
            else:
                miss += 1
        percent_words.append(hit/(hit + miss))
        hit = 0
        miss = 0

    # Find best percentage
    max_percent = max(percent_words)

    if max_percent > .6:
        return decrypt(plain, percent_words.index(max_percent) + 1)
    else:
        return ""
