def display(a, b, c=10, *args, **kwargs):
    print("Positional parameters:")
    print("a =", a)
    print("b =", b)

    print("\nDefault parameter:")
    print("c =", c)

    print("\nVariable length arguments (*args):")
    for i in args:
        print(i)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(key, "=", value)


# Function call
display(1, 2, 3, 4, 5, 6, name="John", age=20, city="Chennai")