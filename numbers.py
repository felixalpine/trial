def main():
    z = value()
    print(f"Value of z is {z}")


def value():
    try:
        z = int(input("Enter value of z: "))
        return z
    except ValueError:
        print("Value of z is not an integer")

main()