from image import *
import base64


with open("test2.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())

analyze_image(str)