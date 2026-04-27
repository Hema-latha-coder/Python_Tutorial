
def pm(a,b,c=4, *y, **names):
    print("pos pm a = ", a)
    print("pos pm b = ", b)
    print("key pm c = ", c)
    print("default d = ", d)
    print("\nVariable length arguments (*y):")
    for i in y:
        print(i)
    print("Keyword arguments (**names):")
    for key, value in names.items():
        print(key, "=", value)
   

pm(10,4,7, 1,2,3 , names ='hema, raphael, ranjith')
