def add(a,b,c):
    d= a+b+c
    return d

def sub(a,b):
    c= a-b
    return c

def mul(x,y):
    z= x*y
    return z

def div(p,q):
    r= p/q
    return r

r1 = add(10,6,2)
print("Add result = ", r1)

r2 = sub(5,4)
print("Sub result = ", r2)

r3 = mul(r1,r2)
print("Mul result = ", r3)

r4 = div(r1,r2)
print("Div result = ", r4)