size = []
with open("key.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = int(line)
        size.append(line)

col, row = size

chars = []
with open("secret.txt", "r") as file:
    for line in file:
        line = line.strip()
        chars.append(line)

pub = []
word = ""
for char in chars:
    word += char
    if len(word) == col:
        pub.append(word)
        word = ""

with open("public.txt", "w") as file:
    for word in pub:
        word += "\n"
        file.write(word)
