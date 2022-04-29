The file *invoice_data.txt* contains raw data for an invoice. More precisely, each line contains

- the name of an item
- how many items are bought
- the unit price of the item

The three values are separated by a single whitespace. Prepare a beautified output of the file which contains

- the name of the item formatted with 15 characters
- the number of units with 3 digits
- the price per item with 7 digits, 2 digits after the decimal point
- the total price *(number of items * price per item)* with 8 digits in total, 2 digits after the decimal point

If there are two lines with the following content "Apple 5 0.99" and "Cherry 2 11.99", then the beautified output should
look as follows:

    Apple           15   0.99   14.85
    Cherry           2  11.99   23.98

<br/>

---

# Hint
Read the file line by line and create a list of tuples. Each tuple contains the item (`string`), the number of items
(`integer`) the price per item (`float`). To identify the individual parts per line, use the method `.split()`. Prepare
an `f-string` to output the data as specified.