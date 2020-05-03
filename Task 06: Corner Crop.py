from PIL import Image

with Image.open("virus.png") as img:
    L, R, T, B = 150, 150, 150, 150
    img.crop((L, T, img.width - R, img.height - B)).show()