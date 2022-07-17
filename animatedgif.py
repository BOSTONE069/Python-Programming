import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)


