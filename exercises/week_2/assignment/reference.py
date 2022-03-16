initial_stock = int(input("Please enter an initial stock level: "))
number_of_month = int(input("Please enter the number of month to plan: "))

sales_plan = []
for i in range(number_of_month):
    sales = int(input(f"Please enter the planned sales quantity for month {i+1}: "))
    sales_plan.append(sales)

production_plan = []
stock = initial_stock

for i in range(number_of_month):
    if sales_plan[i] > stock:
        production = sales_plan[i] - stock
    else:
        production = 0

    production_plan.append(production)

    stock = stock + production - sales_plan[i]

print("The resulting production quantities are:")
for i in range(number_of_month):
    print(f"production quantity month {i+1}: {production_plan[i]}")
