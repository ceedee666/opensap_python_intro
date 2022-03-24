abc = "abcdefghijklmnopqrstuvwxyz"

correct_number_entered = False
shift = -1

while not correct_number_entered:
    shift_str = input("Please enter the number of places to shift: ")
    if shift_str.isdigit():
        shift = int(shift_str)
        if 0 <= shift <= 25:
            correct_number_entered = True
        else:
            print("The number must be between 0 and 25.")
    else:
        print("You didn't enter a number!")


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
