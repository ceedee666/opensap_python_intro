abc = "abcdefghijklmnopqrstuvwxyz"


shift_str = input("Please enter the number of places to shift: ")
if shift_str.isdecimal():
    shift = int(shift_str)

    if 0 <= shift <= 25:
        plain_text = input("Please enter a sentence: ")
        plain_text = plain_text.lower()

        enrypted_text = ""
        for char in plain_text:
            if char in abc:
                index = abc.find(char)
                encrypted_char = abc[(index + shift) % 26]
            else:
                encrypted_char = char

            enrypted_text += encrypted_char

        print("The encrypted sentence is:", enrypted_text)

    else:
        print("You need to enter a number between 0 and 25!")
else:
    print("You need to enter a number between 0 and 25!")
