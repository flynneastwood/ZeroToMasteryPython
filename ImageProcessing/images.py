from PIL import Image, ImageFilter

img = Image.open("./images/Pikachu.jpg")

filtered_img = img.convert("L")
size = filtered_img.resize((300, 300))
size.save("thumbnail.png", "png")
size.show()