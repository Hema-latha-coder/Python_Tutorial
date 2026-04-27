s1 = {10,20,55,45,60}

s2 = {100,500,10,45,80}

print(s1)
print(s2)

s3= s1.union(s2)
print("Union= ", s3)

s4= s1.intersection(s2)
print("Intersection= ",s4)

s5= s1.difference(s2)
print("Difference=", s5)

s6= s1.symmetric_difference(s2)
print("Symmetric difference = ", s6)