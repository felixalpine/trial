def main():
    statement = input()
    print(playback(statement))


def playback(words):
    return words.replace(" ", "...")


main()