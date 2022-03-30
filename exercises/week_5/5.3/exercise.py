def iseven(i):
    if i % 2 == 0:
        return True
    else: 
        return False

for i in range(100):
    if iseven(i):
        print(i, "is even")
    else:
        print(i, "is not even")

    
