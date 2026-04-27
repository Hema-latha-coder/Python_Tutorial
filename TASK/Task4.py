a=150
b=100

def get():
    a=15
    b=10
    print("Local variable=", a)
    print("Local variable=", b)
    print("Global variable=", globals()['a'])
    print("Global variable=", globals()['b'])
get()

