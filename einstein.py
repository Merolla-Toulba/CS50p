def main():
    # get mass from user
    mass = int(input("m: "))
    equation(mass)


def equation(mass):
    # find energy baased on e = mc^2
    energy = mass * 300000000 ** 2
    print(energy)


main()
