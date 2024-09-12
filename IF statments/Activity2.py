actual_cost = int(input("Enter the actual cost to make the product: "))
selling_price = int(input("Enter the selling price for the product: "))

if (selling_price>actual_cost):
     profit = selling_price-actual_cost
     print("The profit you made is: ", profit)
elif (selling_price == actual_cost):
     print("You did not lose any money but you also didn't make any profit")
elif (selling_price<actual_cost):
     loss = selling_price-actual_cost
     print("You lost:", loss)
     


