def encrypt_letter(let, key):
    num = ord(let)
    num -= key
    if num < 65:
        num += 26
    let = chr(num)
    return let

def encrypt_text(text, key):
    encr_text = ""
    for char in text:
        char = char.upper()
        if char.isalpha():
            char = encrypt_letter(char, key)
        encr_text += char
    return encr_text


text = input("Which text should be encrypted: ")
key = int(input("How many shifts should be taken: "))

print(encrypt_text(text, key))