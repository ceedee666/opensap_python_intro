invoice_items = []
with open("invoice_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        words = line.split()
        item = (words[0], int(words[1]), float(words[2]))
        invoice_items.append(item)

for item in invoice_items:
    print(f"{item[0]:15s}{item[1]:3d}{item[2]:7.2f}{item[1] * item[2]:8.2f}")
