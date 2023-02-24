# create main func and use hello and math func
def main():
    user = input("Name please? ")
    hello(user)

    print()

    math()
# create hello function which takes user name input 
def hello(x):
    print(f"Hello, {x}")
# create math function which takes basic math solving for 2 variables
def math():
    x, y, z = (input()).split()

    if y == "+":
        print(f"Total is {float(x) + float(z):,.2f}")


main()