from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    SCALE = 2

    R_max, G_max, B_max = 0, 0, 0
    R_min, G_min, B_min = 255, 255, 255

    counter = [0] * 256

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]

            # Skip empty pixels
            if a == 0:
                continue

            counter[r] += 1
            counter[g] += 1
            counter[b] += 1

    MIN, MAX = min(counter), max(counter)

    print(*counter)
    for i in range(256):
        counter[i] = round((counter[i] - MIN) / (MAX - MIN) * 255)
    print(*counter)

    out = Image.new(img.mode, (256, 256))
    out_pixels = out.load()

    for x in range(out.width):
        for y in range(out.height):
            r, g, b, a = out_pixels[x, y]

            out_pixels[x, y] = (0, 0, 0, 255) if y >= 255 - counter[x] else (255, 255, 255, 255)

    out.show()
