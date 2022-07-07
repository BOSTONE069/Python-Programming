import system2

if len(sys.argv) < 2:
    sys.exit("There is no argument provided")
elif len(sys.argv) > 2:
    sys.exit("Too many argument provided")

print("Hello welcome to CS50 ", sys.argv[1])
