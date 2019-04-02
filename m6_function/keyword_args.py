def msg(name, age):
    print("{0} is {1} years old".format(name, age))

msg("Maaya", 29)
msg(name = "Maaya", age = 29)
msg(age = 29, name = "Maaya")
msg("Maaya", age = 29)
#msg(name = "Maaya", 29) #positional argument follows keyword argument
