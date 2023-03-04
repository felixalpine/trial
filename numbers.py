def main():
    x = value("What is x? ")
    print(f"Value of x is {x}")


def value(prompt):
    while True:
        try:
            z = int(input(prompt))
            return z
        except ValueError:
            print(f"Value of {prompt} is not an integer")
        else:
            break

main()