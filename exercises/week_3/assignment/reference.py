substitution = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

plain_text = input("Please enter a sentence: ")
plain_text = plain_text.lower()

encrypted_text = ""
for char in plain_text:
    if char in substitution:
        encrypted_char = substitution[char]
    else:
        encrypted_char = char

    encrypted_text += encrypted_char

print("The encrypted sentence is:", encrypted_text)
