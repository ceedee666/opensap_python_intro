p1 = []
with open("player1.txt", "r") as file:
    for line in file:
        line = line.strip()
        p1.append(line)

p2 = []
with open("player2.txt", "r") as file:
    for line in file:
        line = line.strip()
        p2.append(line)

result = [0, 0, 0]

for i in range(100):
    if p1[i] == "R":
        if p2[i] == "R":
            result[2] += 1
        elif p2[i] == "S":
            result[0] += 1
        else:
            result[1] += 1
    elif p1[i] == "S":
        if p2[i] == "R":
            result[1] += 1
        elif p2[i] == "S":
            result[2] += 1
        else:
            result[0] += 1
    else:
        if p2[i] == "R":
            result[0] += 1
        elif p2[i] == "S":
            result[1] += 1
        else:
            result[2] += 1

with open("result.txt", "w") as file:
    file.write("Player1 wins: " + str(result[0]) + "\n")
    file.write("Player2 wins: " + str(result[1]) + "\n")
    file.write("Draws: " + str(result[2]) + "\n")

    
    
