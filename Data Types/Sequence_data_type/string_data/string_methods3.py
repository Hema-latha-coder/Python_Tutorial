st = "python"
st1 = "I Am A Automation Tester"
st2= "ß"
st3 = "I am a automation tester and i know python playwright"

print(st)
print(st.capitalize())
print(st1.casefold())
print(st1.upper())
print(st1.lower())

print(st2.lower())
print(st2.casefold())
print(st.center(10,'*'))
print(st1.count('A'))
print(st1.endswith("ster"))
print(st1.endswith("mation"))

print(st1.startswith("I Am"))
print(st1.startswith("i am"))
print(len(st3))
print(st3.find('a'))
print(st3.find('a', 20))
#print(st3.find('a', 30,40)) # sub string not found return -1
print(st3.find('a', 8,15))

print(st3.index('a'))
print(st3.index('a', 20))
#print(st3.index('a', 30,40)) # sub string not found through value error
print(st3.index('a', 8,15))

x1 ="python"
x2 = "x1"
print(x1.isalpha())
print("python3".isalnum())
print("Python3".isalpha())
print("python".isalnum())
print("3938485.987".isdecimal())
print("3938485987".isdecimal())
print("144554".isdigit())
print("a".isascii())
print("ß".isascii())
print(x2.isidentifier())
print("python".islower())
print('PYTHON'.isupper())
print("python".isupper())
print('PYTHON'.islower())
print("I A Am Automation Tester".istitle())
print("12345".isnumeric())
print("123a".isnumeric())
print("Hello Python".isprintable())
print("Hello \nPython". isprintable())
print("".isspace())
print(" ".isspace())
print("hello python". isspace())

print("python".ljust(10,'*'))
print("python".rjust(10,'*'))
print("python is a oops and python language".index('y'))
print('python is a oops and python language'.rindex('y'))
print("python is a high level language python".removeprefix("python"))
print("python is a high level language python".removesuffix("python"))

print("!@#$python%^&*".strip("!@#$%^&*"))
print("!@#$python%^&*".lstrip("!@#$%^&*"))
print("!@#$python%^&*".rstrip("!@#$%^&*"))
print("Python is a high level language".replace('a','A'))
print('Python is a high level language and oops language'.replace('a','A', 3))


