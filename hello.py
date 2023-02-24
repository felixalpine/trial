# Hello without user input and escape sequence
print("Hello, \'Danish\'")

# Hello with user input and fstring with strip and capitalize
user = input("Name please? ").strip().capitalize()
print(f"Hello, {user}")

# Hello with end func
print("Hello, ", end="")
print("Danish")

# Hello with sep func
print("Hello, ", user,  sep="Mr ")
