list_items = []
with open("invoice_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.split()
        line[1] = int(line[1])
        line[2] = float(line[2])
        line = tuple(line)
        list_items.append(line)

for item in list_items:
    print(f"{item[0]:15s}{item[1]:3d}{item[2]:7.2f}{item[1] * item[2]:8.2f}")
