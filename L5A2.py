actual_cost = float(input("Please Enter the Actual Product Price:"))
sale_cost = float(input("Please Enter the Actual Sales Amount:"))
if (sale_cost > actual_cost):
    amount = sale_cost - actual_cost
    print("Total Profit = {0}".format(amount))
else: 
    print("No Profit!!!")