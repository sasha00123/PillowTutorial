from PIL import Image

with Image.open("virus.png") as img:
    img = img.convert("RGBA")
    pixels = img.load()

    center_x, center_y = img.width // 2, img.height // 2
    radius = img.width // 2
    diff_center, diff_border = 2, 0.1

    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            distance = ((center_x - x) ** 2 + (center_y - y) ** 2) ** 0.5
            if distance < radius:
                scale = diff_center + (diff_border - diff_center) * distance / radius
            else:
                scale = 1
            pixels[x, y] = min(255, round(r * scale)), min(255, round(g * scale)), min(255, round(b * scale)), a

    img.show()
