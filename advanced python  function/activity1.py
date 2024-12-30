num1 = [2, 3, 4]
num2 = [8, 1, 5]

a = map(lambda a, y: a + y, num1, num2 )

print(tuple(a))

num3 = [1, 5, 9, 7]
s = map(lambda x: x*x, num3)
print(tuple(s))

