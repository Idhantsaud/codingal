unit = int(input("Enter number of Units consumed: "))
if unit <= 50:
    amount = unit * 2.60
    tax = 25

elif unit <= 100:
    amount = (50 * 2.60)+((unit-50)*3.25)
    tax = 35

elif unit <= 200:
    amount = (50*2.60)+(50*3.25)+((unit-100)*5.26)
    tax = 45

else:
    amount = (50*2.60)+(50*3.25)+(100*5.26)+((unit-200)*8.45)
    tax = 75
print("Your total bill amount is: ", amount+tax)