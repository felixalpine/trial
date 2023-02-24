import emoji

def main():
    gitmoji = input("Input ")
    convert(gitmoji)


def convert(emojize):
    return print(f"Output: {emoji.emojize(emojize)}")


main()