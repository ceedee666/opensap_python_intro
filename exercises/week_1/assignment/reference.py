angle_1 = int(input("Please enter the first angle: "))
angle_2 = int(input("Please enter the second angle: "))
angle_3 = int(input("Please enter the third angle: "))

if angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0:
    print("Angles smaller than 0 are not valid.")
elif angle_1 + angle_2 + angle_3 == 180:
    if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("The triangle is a right triangle.")
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        print("The triangle is an obtuse triangle.")
    else:
        print("The triangle is an acute triangle.")
else:
    print("The entered values are not valid.")
