def m1():
    global a
    a=100
    print("Global variable=", a)

def m2():
    print("Global variable=", a)

m1()
m2()

 