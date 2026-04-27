st = "Pyhton is a high level language"

print(st)

print("=====String Example=====")
for i in st:
    print(i)

print("=====List Example=====")
lang = ["Python",'Java',"R","JS","C++"]
print(lang)

for j in lang:
    print(j)

print("=====Tuple Example=====")
lang1 = ("HTML","JS","Python","DJango","RESTAPI")
print(lang1)

for k in lang1:
    print(k)

print('=====Set Example====')
s1 = {"Chennai","Madurai","Coimbatore","Bangalore","Pune"}
print(s1)

for x in s1:
    print(x)

print("======Dictionary Example=====")

d1 = {"sId":1, "sName":"Rajesh","sCity":"Chennai"}
print(d1)

print("***printed only keys***")
for y1 in d1:
    print(y1)

print("***printed only keys using keys()***")

for y2 in d1.keys():
    print(y2)
    
print("***printed only values using values()***")

for y3 in d1.values():
    print(y3)

print("****printed keys and values using items()****")

for y4 in d1.items():
    
    print(y4)

print("================")

for z1, z2 in d1.items():
    
    print(z1, "==>", z2)