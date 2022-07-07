import sys

if len(sys.argv) < 2:
    print("There is no argument provided")
elif len(sys.argv) > 2:
    print("Too many argument provided")
else:
    print("Hello welcome to CS50 ", sys.argv[1])
