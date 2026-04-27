t1 = ("Python",'JS',"Java","Python","JS","Kotlin",'Python')

print(len(t1))
print(t1.__len__())
print(id(t1))

print(t1.count('Python'))

print(t1.index('Java'))

print(t1.index('Python',1))

print(t1.index('Python', 4,7))

print(t1[0])
# t1[0]="DataScience" # cannot modify
print(t1)