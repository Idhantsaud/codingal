l1 = [5, 3, 6]
l2 = {'a', 'j', 'e'} #This is a set
d = zip(l1, l2)
print(list(d))

x = zip(l1[::-1], l2)
print(list(x))

l3 = ["Apple", "Starlink", "Amazon"]
l4 = [2500, 5000, 3200]

new_dict = {key1:val1 for key1, val1 in zip(l3,l4)}
print(new_dict)