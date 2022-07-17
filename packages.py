import cowsay
import sys

if len(sys.argv) == 2:
    # noinspection PyUnresolvedReferences
    cowsay.cow("Hello and welcome to CS50 ", + sys.argv[1])
