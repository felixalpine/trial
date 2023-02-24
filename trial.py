import sys


try:
    if len(sys.argv) < 2:
        sys.exit()
except ValueError:
    sys.exit("Error")
