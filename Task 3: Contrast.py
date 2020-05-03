from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2
    # Или можно сделать SCALE = 0.5

    L_avg = 0

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            L_avg += sum([r, g, b]) / 3

    n = img.width * img.height
    L_avg /= n

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                min(255, round(L_avg + (r - L_avg) * SCALE)),
                min(255, round(L_avg + (g - L_avg) * SCALE)),
                min(255, round(L_avg + (b - L_avg) * SCALE)),
                a
            )

    img.show()
