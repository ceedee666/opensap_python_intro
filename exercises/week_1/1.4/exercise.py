number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))
number_3 = int(input("Please enter the third number: "))

largest_number = number_1

if number_2 > largest_number:
    largest_number = number_2
if number_3 > largest_number:
    largest_number = number_3

print("The largest number is", largest_number)
