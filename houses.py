name = input("What is your name? ")

match name:
    case "Harry" | "Ron":
        print("Gryfinddor")
    case "Draco":
        print("Sylranine")
    case _:
        print("Ravenclaw")