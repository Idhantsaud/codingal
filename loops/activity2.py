b = input("Enter a string to reverse: ")
rev_sum = ""

for n in b:
    rev_sum = n + rev_sum
print("The reversed string is: ", rev_sum)