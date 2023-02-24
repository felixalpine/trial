import emoji

def main():
    gitmoji = input("Input ")
    convert(gitmoji)


def convert(emojize):
    return print(emoji.emojize(emojize))


main()