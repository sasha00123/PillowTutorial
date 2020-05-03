from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2

    r_values, g_values, b_values = [], [], []

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            r_values.append(r)
            g_values.append(g)
            b_values.append(b)

    r_values.sort()
    g_values.sort()
    b_values.sort()

    n = img.width * img.height

    MINI, MAXI = int(n * 0.05), int(n * 0.95)
    R_max, G_max, B_max = r_values[MAXI], g_values[MAXI], b_values[MAXI]
    R_min, G_min, B_min = r_values[MINI], g_values[MINI], b_values[MINI]

    fit = lambda x, l, r: max(l, min(r, x))

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            pixels[x, y] = (
                round((r - R_min) / (R_max - R_min) * 255) if R_min <= r <= R_max else fit(r, R_min, R_max),
                round((g - G_min) / (G_max - G_min) * 255) if R_min <= r <= R_max else fit(r, R_min, R_max),
                round((b - B_min) / (B_max - B_min) * 255) if R_min <= r <= R_max else fit(r, R_min, R_max),
                a
            )

    img.show()
