x1 = "Python3"
x2 = "python"
x3 = "ß"

print(x1.isalnum())
print(x1.isalpha())
print("===========")
print(x2.isalpha())
print(x2.isalnum())
print(x2.islower())
print(x2.isupper())
print(x2.isascii())
print(x3.isascii())
print(x2.isdecimal())
print("================")
s1 = "12345"
s2 = "12.3"
s3 = "12 3"
s4 = " "
s5 = "²"

print(s1.isdecimal())
print(s2.isdecimal())
print(s3.isdecimal())

print(s1.isnumeric())
print(s2.isnumeric())
print(s3.isnumeric())

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s5.isdigit())

y1= "s1"
y2= "Hello, how are you?"
print(y1.isidentifier())
print(y2.istitle())

z1= "Hello 123"
print(z1.isprintable())

print(s4.isspace())
print(s3.isspace())
print(" ".isspace())

lang=["Python", 'Java', 'Perl','Php']
print(lang)

print('#'.join(lang))

print(x1.ljust(20))
res = x1.ljust(20)

print(res, " is a high level langauge")

print(x1.rjust(20))
x6 = "!@#$Python%^&*"
print(x6.strip('!@#$%^&*'))
print(x6.lstrip("!@#$"))
print(x6.rstrip('%^&*'))

print(x6.removeprefix('!@#$'))
print(x6.removesuffix('*'))
print(x6.rstrip('*'))

print(y2.replace('o','X'))
print(y2.replace('o','x',2))