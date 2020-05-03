from PIL import Image, ImageSequence, ImageFilter

from random import randint

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    out = Image.new(img.mode, img.size)
    out_pixels = out.load()

    DELTA = 5

    for x in range(img.width):
        for y in range(img.height):
            x_, y_ = x + randint(-DELTA, DELTA), y + randint(-DELTA, DELTA)

            x_ = max(0, min(x_, img.width - 1))
            y_ = max(0, min(y_, img.height - 1))

            out_pixels[x, y] = pixels[x_, y_]

    out.show()
