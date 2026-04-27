dict1 = {1:"Java", 2:"Python", 3:"Js",4:"ML",5:"DA"}

print(dict1.keys())
print(dict1.values())
print(dict1.get(1))
dict2= dict1.copy()
print("new mem=", dict2)

dict2.update({5:"DS"})
print(dict2)
print(dict1)

print(dict2.items())
dict2.popitem()
print(dict2)
dict2.popitem()
print(dict2)

dict2.pop(2)
print(dict2)
dict2.clear()
print(dict2)

dict3 = {}
print(dict3.fromkeys([1,2,3,4,5]))

dict4 = {}
print(dict4.fromkeys("abcde"))

print(dict1)
dict1.setdefault(6,"AI")
print(dict1)