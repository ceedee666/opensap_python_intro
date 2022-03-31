list_numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        i = line.strip()
        i = int(line)
        list_numbers.append(i)

list_numbers.sort()
list_numbers.reverse()

for x in list_numbers[:3]:
    print(x)
