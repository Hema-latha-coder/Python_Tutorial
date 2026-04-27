list1 = ["Python",'JS','Java','Python','ML','DS']

print(len(list1))
print(list1.__len__())
print(list1)

list1.append("Python")
print(list1)
list1.append("AI")
print(list1)

print(list1)
print(list1.count('Python'))
print(list1.count('ML'))
list1.insert(2,'AI')
print(list1)


print(list1.index('Python'))
print(list1.index('Python',2))
print(list1.index('Python',5,8))

print("====================")
print(list1)
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

list1.pop()
print(list1)

list1.remove('AI')
print(list1)

list2 = list1.copy()

print(list2)

list2.clear()

print(list2)

l1 = [1,2,3]
l2 = [4,5,6]

print(l1)
print(l2)
l1.extend(l2)
print(l1)
