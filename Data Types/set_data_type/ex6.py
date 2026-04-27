x1 = {"Java","Python","Perl",'PHP'}

x2 = {"JS",'Python', "Ruby", "PHP"}

x1.update(x2)
print(x1)

print("=============")

y1 = {"Java","Python","Perl",'PHP'}

y2 = {"JS",'Python', "Ruby", "PHP"}
y1.intersection_update(y2)
print(y1)

print("===================")
z1 = {"Java","Python","Perl",'PHP'}

z2 = {"JS",'Python', "Ruby", "PHP"}
z2.difference_update(z1)
print(z2)

print("=================")

a1 = {"Java","Python","Perl",'PHP'}

a2 = {"JS",'Python', "Ruby", "PHP"}


a1.symmetric_difference_update(a2)
print(a1)