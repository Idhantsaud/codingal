x = 5
if (type(x)is int):
    print(True)
else:
    print(False)
b = 5.5
if (type(b)is not float):
    print(True)
else:
    print(False)

c = 20 
y = 20
if (c is y):
    print('c and y have the same identity ')

h = 30
if (c is not h):
    print("c and h don't have the same indentity")