# Filter the even numbers from the file
The file "numbers.txt" contains some random  numbers. Again, there is one number per line. Go through this list, and write all numbers into a new file "even_numbers.txt". 

# Hint
Go through the file "numbers.txt" line by line, read the input, delete the line break and cast it into an integer. Then append the number into a list. When the file is read completely, all numbers are now stored in the list. Open the new file "even_numbers.txt" and iterate through the list. If a number is even, then write it into the file.


# Tests
- Check the output (should be: 9853\n9760\n9745)
- Check if there is an open() statement
- Check if there is either read() or readlines()
- Check if there is a .strip()
- Check if there is a int() casting