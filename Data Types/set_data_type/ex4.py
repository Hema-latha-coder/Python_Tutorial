s1= {'Python','Java','Php','Js'}

s2 = {"C","Kotlin",'Php',"Java","C#"}
print(s1)
print(s2)

x1= s1.union(s2)
print(x1)

x2= s1.intersection(s2)
print(x2)

print("*****************")

x1 = {"Python","Java",'Php',"Js"}

x2 = {"C","Kotlin",'Php',"Java","C#"}

print(x1)
print(x2)
print("*************")
x1.update(x2)
print(x1)

print("****************")

y1 = {"Python","Java",'Php',"Js"}

y2 = {"C","Kotlin",'Php',"Java","C#"}

print(y1)

y1.intersection_update(y2)
print(y1)