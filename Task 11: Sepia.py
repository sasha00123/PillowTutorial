from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    k = 10

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            m = sum([r, g, b]) // 3
            pixels[x, y] = min(255, m + 2 * k), min(255, m + k), m, a
    img.show()