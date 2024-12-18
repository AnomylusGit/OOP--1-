class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
glu = Parrot("Glu", 15)

print("Blu is a {}" .format(blu.species))
print("Glu is also a {}" .format(glu.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(glu.name, glu.age))