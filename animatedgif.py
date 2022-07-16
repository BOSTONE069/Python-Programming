import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)


