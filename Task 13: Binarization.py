from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    L_avg = 0

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            L_avg += sum([r, g, b]) / 3

    n = img.width * img.height
    L_avg /= n

    TRESHOLD = L_avg

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            avg = sum([r, g, b]) // 3
            # Or avg = max(r, g, b)
            if avg < TRESHOLD:
                pixels[x, y] = (0, 0, 0, 255)
            else:
                pixels[x, y] = (255, 255, 255, 255)
    img.show()
