There is a file `secret.txt`, which contains one character per line. There is a second file `key.txt`, which contains
two lines with one number per line (the number could have several digits). The first number `col` represents the number
of columns of a grid, the second number `row` represents the number of rows of the grid.

The characters of the first file should now be filled into this grid. Take the characters one by one and fill them into
a string until the string contains `col` characters. Append the string to a list. Then create a new string the same way.
Continue, until the number of strings is equal to `row`.  Now, write all the strings into a file `public.txt`. Open the
the file and check the content.

# Example

If the file `secret.txt` contains the following input:

    #
    #
    #
    .
    #
    .
    .
    #
    .
    .
    #
    .

<br/>

and the file `key.txt` contains the following numbers:

    3
    4

<br/>

then the content in the file `public.txt` should be as follows:

    ###
    .#.
    .#.
    .#.
