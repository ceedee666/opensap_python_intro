import string


def encrypt_letter(letter, shift):
    if letter in string.ascii_lowercase:
        ind = string.ascii_lowercase.index(letter)
        ind = (ind + shift) % 26
        secret_letter = string.ascii_lowercase[ind]
    else:
        secret_letter = letter
    return secret_letter


def calculate_shifts(letter):
    ind = string.ascii_lowercase.index(letter)
    return ind


def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()

    encrypted_text = ""

    for index, letter in enumerate(text):
        key_letter = keyword[index % len(keyword)]
        shift = calculate_shifts(key_letter)
        if letter.isalpha():
            encrypted_text += encrypt_letter(letter, shift)
        else:
            encrypted_text += letter
    return encrypted_text


text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used? ")

print(encrypt_text(text, keyword))
