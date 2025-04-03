import random 
def getfruit():
    a = ["apple", "Heart", "bird"]

    rnd = random.randit(0, len(a)-1)
    return a[rnd]

def printFruits(selected):
    print(selected [0] + "  I  " +selected[1]+"  I  "+selected[2])

def checkWin(selected):
    if selected[0] == selected[1]== selected==[2]:
        return True
    else:
        return False
    
selected = [None]*3
play = "yes"
while play == "yes":

    for x in range(0, len(selected)):
        selected[x] = getfruit()

    print(selected)
    print(checkWin(selected))

    play = input("Do you want to play again yes/no")