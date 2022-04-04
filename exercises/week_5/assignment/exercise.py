def encrypt_letter(letter, shift):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ind = abc.index(letter)
    ind = (ind + shift) % 26
    secret_letter = abc[ind]
    return secret_letter


def calculate_shifts(letter):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ind = abc.index(letter)
    return ind


def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()

    encrypted_text = ""

    for i in range(len(text)):
        key_letter = keyword[i % len(keyword)]
        shift = calculate_shifts(key_letter)
        if text[i].isalpha():
            encrypted_text += encrypt_letter(text[i], shift)
        else:
            encrypted_text += text[i]
    return encrypted_text


text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used? ")

print(encrypt_text(text, keyword))
