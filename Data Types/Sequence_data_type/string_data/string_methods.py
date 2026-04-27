st1 = "python"
st2 = "JAVASCRIPT"
st3 = "i am a data scientist and i know data analytics and i am dealing with data"
st4 = "I am a automation tester"

print(st1.upper())
print(st2.lower())
print(st3.capitalize())
print(st4.casefold())
print("straße".lower())
print("straße".casefold())

print(st3.title())
print(st4.swapcase())
print(st1.center(20,'*'))
print(len(st3))
print(st3.count('data'))
print(st3.count('data',25))
print(st3.count('data',25,50))

print(st3.endswith("data"))
print(st3.endswith("data",50))
print(st3.endswith("analyst",25,46))
print(st3.startswith("i am"))
print(st3.startswith("i am",0))
print(st3.startswith("i am",10,20))

print(st3.find("scientist"))
print(st3.find('data',25))
print(st3.find('data',40,70))

print(st3.index('data'))
print(st3.index('data', 25))
print(st3.index('data', 40,70))

print(st3.find('learning'))

x1= "Python3"
x2= "python"
x3 = "ß"

print(x1.isalnum())
print(x1.isalpha())
print("===========")