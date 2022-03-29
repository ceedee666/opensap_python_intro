# Decipher the secret text
There is a file `secret.txt`, which contains one character per line. There is a second file `key.txt`, which contains two lines with one number per line (the number could have several digits). The first number `col` represents the number of columns of a grid, the second number `row` represents the number of rows of the grid. The characters of the first file should now be filled into this grid. Take the characters one by one and fill them into a string until the string contains `col` characters. Then create a new string the same way. Continue, until the number of strings is equal to `row`. (The strings could all be stored in list ...). Now, write all the strings into a file `public.txt`. Open the the file and check the content.

# Tests
- public.txt available and contains the expected outcome
- check if there are two open with modus "r" and one open with modus "w"
- check