num = int(input("Enter a three digit number: "))

sum = 0 
temp = num 
while temp > 0:
    digit = temp % 10
    sum = sum+digit**3
    temp = temp//10

if sum == num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")