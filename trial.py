import sys

try:
    if len(sys.argv) > 2:
        sys.exit("Error")
except ValueError:
    sys.exit("Error")