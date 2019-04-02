def greet(*names):
    for name in names:
        print("Hello,", name)

greet("Maaya", "Ayana", "Saori")
print()
def stu(**data):
    for key, value in data.items():
        print("{0} is {1}".format(key, value))

stu(name = "RRR", age = 24, mobile = "0912368423")
print()
stu(name = "ZZZ", age = 45, email = "ZZZ@gmail.com", mobile = "0912368423")