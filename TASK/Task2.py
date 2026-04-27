a,b= 10,5
def add():
    c=a+b
    print("Add=", c)
    sub()

def sub():
    c=a-b
    print("Sub=", c)
    mul()

def mul():
    c=a*b
    print("Mul=", c)
    div()

def div():
    c=a/b
    print("Div=", c)
add()