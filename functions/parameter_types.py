# positional parameter
def add(a,b):
    c= a+b
    print("Add result = ", c)
add(10,20)

# keyword parameter
def sub(x,y):
    z= x-y
    print("sub result = ", z)
sub(x=20,y=10)

#default parameter
def mul(p=10,q=10):
    r= p*q
    print("mul result = ", r)
mul()

# variable length parameter
def number(*x):
    print("Sum all the values = ", sum(x))
number(10,20,30,40,50)

#keyword length parameter (Variable length keyword parameter)
def user_info(**details):
    print(details)
user_info(uid=1,uname='Ram',age=30, city='Chennai')
user_info(uid=2,uname='Kavi', city='Bangalore')

#positional only
def greet(name,age):
    print("Name = ", name)
    print("Age = ", age)

greet("Hema", 27)

#keyword only
def greet(name, age):
    print("Name = ", name)
    print("Age = ", age)
greet(name= "Hema", age = 27)