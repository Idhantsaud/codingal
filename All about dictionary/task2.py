a = int(input("Enter the amount: "))
note_100 = a//100
note_50 = (a%100)//50
note_10 = ((a%100)%50)//10

print("Number of 100 rupees are: ", note_100)
print("Number of 50 rupees are: ", note_50)
print("Number of 10 rupees are: ", note_10)

