student_name = ["Bob", "Carl", "Alex"]
screen_time =[[322, 450, 123], [120, 500, 340], [145, 390, 190]]
class_size = len(student_name)
print(class_size)

count = []
for x in range(3):
    total = 0 
    for i in range(3):
        total = total + screen_time[x][i]
    count.append(total)

print(total)

day_count = []
for n in range(3):
    m = 0
    for j in range(3):
        m = m + screen_time[n][j]
        if screen_time[n][j] > 300:
            day_count.append(screen_time[n][j])

avg = 0
for l in range(3):
    avg = avg + count[l]

avg = avg/3

min = 99999
for t in range(3):
    if min > count[t]:
        min = count[t]
    


    
            
