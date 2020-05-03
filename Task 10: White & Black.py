from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            avg = sum([r, g, b]) // 3
            # Or avg = max(r, g, b)

            pixels[x, y] = avg, avg, avg, a
    img.show()