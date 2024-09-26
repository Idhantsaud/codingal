num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print("The values of num1 is: ", num1)
print("The value of num2 is: ", num2)
print("The value of num3 is: ", num3)

num1, num2, num3, = num2, num3, num1
print("After swaping the values")
print("The values of num1 is: ", num1 )
print("The value of num2 is: ", num2)
print("The value of num3 is: ", num3)
