s1 = {"Python",'Perl','Php','Java','Js','Ruby','Python'}

print(s1)

s1.add('ML')
print(s1)
s1.add('JS')
print(s1)

s2= s1.copy()
print("New memory = ", s2)

s2.remove('Python')
print(s2)

s2.discard("JS")
print(s2)

#s2.remove('Python')
#print(s2) throws error

s2.pop()
print(s2)

s2.pop()
print(s2)

s2.clear()
print(s2)