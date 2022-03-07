rows = int(input("Please enter the number of rows in the matrix: "))
cols = int(input("Please enter the number of clumns in the matrix: "))

print("Enter the matrix values: ")

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Value: "))
        row.append(value)
    matrix.append(row)

for row in matrix:
    print("Sum of row:", sum(row))
