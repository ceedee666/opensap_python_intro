size = []
with open("key.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = int(line)
        size.append(line)

col = size[0]
row = size[1]

chars = []
with open("secret.txt", "r") as file:
    for line in file:
        line = line.strip()
        chars.append(line)

pub = []
word = ""
count = 1
for char in chars:
    word += char
    count += 1
    if count == 50:
        pub.append(word)
        word = ""
        count = 1

with open("public.txt", "w") as file:
    for word in pub:
        word += "\n"
        file.write(word)
    
