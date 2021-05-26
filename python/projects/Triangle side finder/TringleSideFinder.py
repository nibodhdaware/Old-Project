import math

find = input("What to find(h, s1, s2): ")


def hypotenuse():
    side1 = int(input("Side1: "))
    side2 = int(input("Side2: "))
    answer = math.pow(side1, 2) + math.pow(side2, 2)
    print(math.sqrt(answer))


def s1():
    hypo = int(input("Hypotenuse: "))
    side2 = int(input("Side2: "))
    answer = math.pow(hypo, 2) - math.pow(side2, 2)
    print(math.sqrt(answer))


def s2():
    hypo = int(input("Hypotenuse: "))
    side1 = int(input("Side1: "))
    answer = math.pow(hypo, 2) - math.pow(side1, 2)
    print(math.sqrt(answer))


if find == "h":
    hypotenuse()

elif find == "s1":
    s1()

elif find == "s2":
    s2()

else:
    print('''
h to find hypotenuse
s1 to find first side
s2 to find second side''')
