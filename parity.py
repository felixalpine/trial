def main():
    num = int(input("What is the number: "))
    even(num)


def even(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


main()