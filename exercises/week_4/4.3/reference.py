def filesummer():
    sum = 0
    with open("/Users/user/Documents/Codes/Arbeit/codeocean/4.3/numbers2.txt", "r") as file:
        for i in file:
            i = i.strip()
            sum = sum + int(i)
        print(sum)

filesummer()