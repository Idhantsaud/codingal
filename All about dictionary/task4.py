weather = ("s", "r", "s", "r", "r", "s", "r")

sunny = 0
rainy = 0
for x in range(0,7): 
    if (weather[x] =="r"):
        rainy += 1
    else:
        sunny += 1

if sunny<rainy:
    print("It looks ike it's going to rain :(")
elif sunny> rainy:
    print("The weather looks good, Very sunny :)")