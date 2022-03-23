list_num = []
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        i = int(line)
        list_num.append(i)

with open("even_numbers.txt", "w") as file:
    for i in list_num:
        if i % 2 == 0:
            i = str(i) + "\n"
            file.write(i)
