def exercise():
    ###BEGIN SOLUTION
    
    for nummer in range(1, 101):
        if nummer % 3 == 0 and nummer % 5 == 0:
            print("FizzBuzz")
        elif nummer % 3 == 0:
            print("Fizz")
        elif nummer % 5 == 0:
            print("Buzz")
        else:
            print(nummer)
            
    
    ###END SOLUTION
    
    
exercise()