The file `numbers.txt` contains numbers. (Actually, the same numbers from the last exercise.) There is exactly one
number per line. Read the numbers from the file and write only the even numbers into a new file named
`even_numbers.txt`. Again, there should be one number per line. The order of the numbers shall be unchanged. To
indicate that the program is finished, print the following output: "List of even numbers created!"

# Hint
First read all the numbers as explained in the last exercise and put them into a list. Open the new file for writing. Go
through the list and check if a number is even. If this is case, change the integer into a string and do not forget to
add a line break. Write this string into the file. Finally implement the print statement.

# Tests, structural
- Check if open(.. "r") exists
- Check if open(.. "w") exists