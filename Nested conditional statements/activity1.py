print("Do you have a certificate ?")
print("1. Yes")
print("2. No")
a = input("Do you have Medical ceritficate ? ")
if a == "1":
    print("Is eligible for the test")
else:
    att = float(input("Enter your attendance %: "))
    if att > 75:
        print("Eligible for the test")
    else:
        print("Not eligible for the test")
 