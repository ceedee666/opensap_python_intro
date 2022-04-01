# Beautify the print out
The file "invoice_data.txt" contains raw data for an invoice. More precisely, each line contains

- the name of an item
- how many items are bought
- the unit price of the item

The three values are separated by a single blank. Prepare a beautified output of the file which contains

- the name of the item formatted with 15 characters
- the number of units with 3 digits
- the price per item with 7 digits, two digits after the decimal point
- the total price (number of items * price per item) with 8 digits in total, two digits after the decimal point.

If there are two lines with the following content "Apple 5 0.99" and "Ananas 2 11.99", then the beautified output should look as follows:

    Apple           15   0.99   14.85
    Ananas           2  11.99   23.98 

# Hint
Read the file line by line and create a list of tuples. Each tuple contains the item (string), the number of items (integer) the price per item (float). To identify the individual parts per line, use the method `.split()`. Prepare an f-string to output the data as specified.

# Proposed tests
- check for `open()`
- check for `.split()`
- check for f-string
- check the output
