def exercise():
    sentence = input("What sentence should be output? ")
    letter = input("Which letter should be removed? ")
    result = ""
    for char in sentence:
        if char != letter:
            result += char
    print(result)

exercise()

