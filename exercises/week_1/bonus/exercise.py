a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))

discriminat = (b * b) - (4 * a * c)

if discriminat < 0:
    print("The quadratic equation has 2 complex solutions.")
elif discriminat == 0:
    print("The quadratic equation has 1 real solution.")
else:
    print("The quadratic equation has 2 real solutions.")
