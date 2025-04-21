




accounts = [["Ryan", "123d"], ["bob", "thebuilder"], ["joe", "2313"]]
ac_id = [1,2,3]

AccDetails = [[550,1000,600],[720,1000,600], [680,1000,600]]

a = int(input("Enter the accound Id"))
b = input("Enter the account name")
c = int(input("Enter the password"))

for x in range(len(ac_id)):
    if ac_id[x] == a:
        print("The user exists")
        if accounts[x][1] == b and accounts[x][2]== c:
             print("Correct password")
        else:
            print("Wrong password")

display = 1
while display:
    print("1. display balance ")
    print("2. withdraw money")
    print("3. deposit money")
    choice = int(input("Enter the choice"))
    if choice == 1:
        choice_acc = input("Which persons balance do you want to see")
        for x in range(len(ac_id)):
            if choice_acc == ac_id[x]:
                print (AccDetails[x][0])

    


            






             
