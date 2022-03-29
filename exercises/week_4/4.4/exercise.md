# Find the three biggest numbers
The file `numbers.txt` contains random integer numbers. There is exactly one number per line. Read the file and output the three biggest numbers in the following form:

	2345
	223
	89
	
# Hint
Read the file line by line, delete the line break. As files can only contain strings, the number must now be converted into an integer. Add the number into a list. When all numbers are in the list, sort the list. Then print out the biggest numbers.


# Tests
- Check the output (should be: 9853\n9760\n9745)
- Check if there is an open() statement
- Check if there is either read() or readlines()
- Check if there is a .strip()
- Check if there is a int() casting