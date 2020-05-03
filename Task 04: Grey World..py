from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2
    # Можно сделать SCALE = 0.5 для уменьшения
    R_avg, G_avg, B_avg = 0, 0, 0
    for x in range(img.width):
        for y in range(img.width):
            r, g, b, a = pixels[x, y]
            R_avg += r
            G_avg += g
            B_avg += b

    n = img.width * img.height
    R_avg /= n
    G_avg /= n
    B_avg /= n
    L_avg = (R_avg + G_avg + B_avg) / 3

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                min(255, round(r * L_avg / R_avg)),
                min(255, round(g * L_avg / G_avg)),
                min(255, round(b * L_avg / B_avg)),
                a
            )

    img.show()
