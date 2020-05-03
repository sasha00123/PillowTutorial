from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2

    R_max, G_max, B_max = 0, 0, 0
    R_min, G_min, B_min = 255, 255, 255

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            R_max, G_max, B_max = max(R_max, r), max(G_max, g), max(B_max, b)
            R_min, G_min, B_min = min(R_min, r), min(G_min, g), min(B_min, b)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                round((r - R_min) / (R_max - R_min) * 255),
                round((g - G_min) / (G_max - G_min) * 255),
                round((b - B_min) / (B_max - B_min) * 255),
                a
            )

    img.show()
