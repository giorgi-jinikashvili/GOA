x = [1,2,3,4,5,6,7,8,9,10]
x.append(11)
x.append(12)
x.append(13)
x.append(14)
print(x)

x.remove(1)
x.remove(2)
print(x)

x.count(10)
print(x.count(10))

x.reverse()
print(x)

x.sort(reverse = True)
print(x)

y = ["gio", "mate", "toko"]
x.extend(y)
print(x) 

x.copy()
x_copy = x.copy
print(x)
print(x_copy)

x.clear()
print(x)