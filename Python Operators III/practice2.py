mark1 = int(input("Enter your first grade: "))
mark2 = int(input("Enter your second grade: "))
mark3 = int(input("Enter your third grade: "))
mark4 = int(input("Enter your fourth grade: "))
mark5 = int(input("Enter your fifth grade: "))

total = (mark1+mark2+mark3+mark4+mark5)
avg = total/5

if avg>= 91 and avg<=100:
    print("Your grade is an a 9A* keep it up!!")
elif avg>=81 and avg<=91:
    print("Your grade is 8A well donee !!")
elif avg>=71 and avg<=81:
    print("Your grade is 7A well donee ")
elif avg>=61 and avg<=71:
    print("Your grade is 6B keep it up ")
elif avg>=51 and avg<=61:
    print("Your grade is 5B getting there !!")
elif avg>=41 and avg<=51:
    print("Your grade is 4C not there yet but keep it up !!")
elif avg>=33 and avg<=41:
    print("Your grade is 3D  !!")
elif avg>=21 and avg<=33:
    print("Your grade is a 1E you really need to try harder !")
elif avg>=0 and avg<=21:
    print("Your grade is 1G REVISEE MORE !!")
else:
    print("You failed you need to take this seriuosly !!")