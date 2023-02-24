def main():
    M = int(input("Entet the mass: "))
    Joules(M)


def Joules(m):
    return print(f"E: {m * pow(300000000, 2)}")


main()