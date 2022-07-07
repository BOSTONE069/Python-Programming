import sys
from emoji import emojize

if len(sys.argv) != 2:
    sys.exit()
else:
    print("Inputting %s" % sys.argv)
    print(emojize("Outputting %s" % sys.argv))


