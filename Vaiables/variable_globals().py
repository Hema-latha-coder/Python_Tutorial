a,b = 1000, 2000

def m1():
    a,b = 10,20
    print("Local variable a = ", a)
    print("Local variable b = ", b)
    print("Global variable a = ", globals()['a'])
    print("Global variable b = ", globals()['b'])

def m2():
    x,y = 50,51
    print("Local variable x = ", x)
    print("Local variable y = ", y)
    print("Global variable a = ", globals()['a'])
    print("Global variable b = ", globals()['b'])

m1()
print("==========")
m2()