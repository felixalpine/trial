def main():
    Nowadays = input("> ")
    print(Oldto(Nowadays))


def Oldto(emoji):
    return emoji.replace(":)", "🙂").replace(":(", "🙁")


main() 