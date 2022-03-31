# Filter even numbers
The file `numbers.txt` contains numbers. (Actually, the same numbers from the last exercise.) There is exactly one number per line. Read the numbers from the file and write those numbers into a new file named `even_numbers.txt`. Again, there should be one number per line. The order of the numbers shall be unchanged. To indicate, that the program is finished, print the following output: "List of even numbers created!"

# Hint
First read all the numbers as explained in the last exercise and put them into a list. Open the new file for writing. Go through the list and check if a number is even. If this is case, change the integer into a string and do not forget to add a line break. Write this string into the file. Implement the final print statement.

# Tests
- Check, if a file of even numbers exists. (How to do that?)
- Compare the content of the file with the existing file (How to do that?)
- Check if open(.. "r") exists
- Check if open(.. "w") exists
- Check if there is an if-statement
