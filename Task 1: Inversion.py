from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = 255 - r, 255 - g, 255 - b, a
    img.show()