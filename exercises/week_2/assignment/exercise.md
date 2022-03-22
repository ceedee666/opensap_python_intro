In this exercise you are going to simulate a sales and operations planning
using the [zero stock level](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/d853922bdd584e8e83027e5a0b8122f2/d06dbd534f22b44ce10000000a174cb4.html?locale=en-US)
strategy. Write a Python program that asks the user to enter the following data:

- An initial stock level for a product
- The number of month(s) to plan
- The planned sales quantity for each month

Based on this data, calculate the required production quantity as follows:

- If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
- If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

Below is an example execution of the program:

    Please enter an initial stock level: 500
    Please enter the number of month to plan: 5
    Please enter the planned sales quantity for month 1: 300
    Please enter the planned sales quantity for month 2: 250
    Please enter the planned sales quantity for month 3: 200
    Please enter the planned sales quantity for month 4: 400
    Please enter the planned sales quantity for month 5: 100

    The resulting production quantities are:
    Production quantity month 1: 0
    Production quantity month 2: 50
    Production quantity month 3: 200
    Production quantity month 4: 400
    Production quantity month 5: 100

Why are those production quantities calculated? The initial stock level is 500. In the first month 300 pieces are sold.
Therefore, nothing needs to be produced and the resulting stock is 200 (= 500 - 300).
In the second month 250 pieces are sold. The stock level after the previous month is 200. Therefore 50 pieces need to be
produced. The resulting stock level is 0 (= 200 + 50 - 250).
In the third month 200 pieces are sold. The stock level after the previous month is 0. Therefore 200 pieces need to be
produced. The resulting stock level is 0 (= 200 - 200).
