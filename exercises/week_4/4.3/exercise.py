list_numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        i = line.strip()
        i = int(line)
        list_numbers.append(i)

list_numbers.sort()

for x in range(1, 4):
    print(list_numbers[-x])

        
