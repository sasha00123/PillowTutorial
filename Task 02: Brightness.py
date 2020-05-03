from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2
    # Можно сделать SCALE = 0.5 для уменьшения

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            pixels[x, y] = min(255, round(r * SCALE)), min(255, round(g * SCALE)), min(255, round(b * SCALE))

    img.show()