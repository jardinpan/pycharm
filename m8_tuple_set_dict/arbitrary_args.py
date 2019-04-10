def greet(*names):
    for name in names:
        print("Hello,", name)
greet("Maaya", "Ayana", "Saori")
print()

tuple1 = ("Maaya", "Ayana", "Saori")
greet(tuple1)
greet(*tuple1)
print()

list1 = ("Maaya", "Ayana", "Saori")
greet(list1)
greet(*list1)
print()

str1 = "Maaya"
greet(str1)
greet(*str1)
print()

def stu(**data):
    for key, value in data.items():
        print("{0} is {1}".format(key, value))

stu(name = "RRR", age = 24, mobile = "0912368423")
print()
student = {'name':'Maaya', 'age':29, 'mobile':'0958817222', 'email':'MayaaMyWife@gmail.com'}
stu(**student)