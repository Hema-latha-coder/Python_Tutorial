l1 = ['Python','JS','ML','Numpy','Pandas']
l2 = ['Python','JS','ML','Numpy','Pandas']
l3 = ['Python','ML','JS']
l4 = l1

print(id(l1))

print(id(l2))

print(id(l3))

print(id(l4))

# is checking the memory address not content

print(l2 is l1)  
print(l4 is l1)

print(l2 is not l1)
print(l4 is not l1)