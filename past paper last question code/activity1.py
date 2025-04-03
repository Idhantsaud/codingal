clubs = ["a", "b", "c"]

statistics = [[12,0,0], [6,4,0], [10,15,2]]
points = 0

match_played = [12, 10, 15]
for i in range (3):
    if match_played[i] > 22:   
        print("Too many matches played")
        break

for x in range(3):
    m = 0
    for y in range(3):
        m = m + statistics [x][y]
    if m == match_played[x]:   
        print("VALIDATE")
    else:
        print("Error")
        break
