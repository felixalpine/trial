# Basic addition with float and round func
x = float(input("Enter x: "))
y = float(input("Enter y: "))

z = round(x + y)

print(f"Total: {z}")

print()

# Basic addition with nesting using round method with fstring
x = float(input("Enter x: "))
y = float(input("Enter y:"))

print(f"Total: {x + y:.2f}")
