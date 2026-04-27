s1 = {10,20,25,30,40,50, 60,70,75}

s2 = {10,25,40,50,60, 75}

print(s1.issubset(s2))
print(s2.issubset(s1))

x1 = {10,25,40,50,60, 75}

x2 = {10,20,25,30,40,50, 60,70,75}

print(x1.issuperset(x2))
print(x2.issuperset(x1))

print("===============")

y1 = {1,2,3,4,5}

y2 = {5,10,15,20,25,30}

print(y1.isdisjoint(y2))

z1 = {1,2,3,4,5}

z2 = {10,15,20,25,30}

print(z1.isdisjoint(z2))