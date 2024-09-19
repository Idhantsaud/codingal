c1 = int(input("Enter the speed of cyclist 1: "))
c2 = int(input("Enter the speed of cyclist 2: "))
c3 = int(input("Enter the speed of cyclist 3: "))

avg = (c1+c2+c3)/3
print("The average speed is: ", avg)
if avg > c1:
    print("Speed of cyclist 1 is less than the average speed. ")
if avg > c2:
    print("Speed of cyclist 2 is less than the average speed. ")
if avg > c3:
    print("Speed of cyclist 3 is less than the average speed.")